#!/usr/bin/env python3

"""Summarize quality-controlled temperature measurements."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from provenance import run_manifest, write_json

KELVIN_OFFSET = 273.15
ABSOLUTE_ZERO_CELSIUS = -KELVIN_OFFSET
REQUIRED_COLUMNS = {
    "timestamp",
    "sensor_id",
    "temperature_celsius",
    "quality_flag",
}


@dataclass(frozen=True)
class Measurement:
    timestamp: str
    sensor_id: str
    temperature_celsius: float
    quality_flag: str


@dataclass(frozen=True)
class AnalysisConfig:
    accepted_quality_flags: frozenset[str]
    calibration_offset_celsius: float


@dataclass(frozen=True)
class TemperatureSummary:
    total_measurements: int
    accepted_measurements: int
    minimum_kelvin: float
    mean_kelvin: float
    maximum_kelvin: float


def load_config(path: Path) -> AnalysisConfig:
    """Read the analysis decisions from a JSON file."""

    with path.open(encoding="utf-8") as config_file:
        values = json.load(config_file)
    try:
        raw_flags = values["accepted_quality_flags"]
        raw_offset = values["calibration_offset_celsius"]
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError("invalid analysis configuration") from error
    if not isinstance(raw_flags, list) or not all(
        isinstance(flag, str) for flag in raw_flags
    ):
        raise ValueError("accepted quality flags must be a list of strings")
    accepted_flags = frozenset(raw_flags)
    try:
        calibration_offset = float(raw_offset)
    except (TypeError, ValueError) as error:
        raise ValueError("calibration offset must be a number") from error
    if not accepted_flags or not all(accepted_flags):
        raise ValueError("at least one quality flag must be accepted")
    if not math.isfinite(calibration_offset):
        raise ValueError("calibration offset must be finite")
    return AnalysisConfig(accepted_flags, calibration_offset)


def read_measurements(path: Path) -> list[Measurement]:
    """Read CSV observations and reject malformed or impossible values."""

    measurements = []
    with path.open(newline="", encoding="utf-8") as csv_file:
        rows = csv.DictReader(csv_file)
        missing_columns = REQUIRED_COLUMNS.difference(rows.fieldnames or [])
        if missing_columns:
            missing = ", ".join(sorted(missing_columns))
            raise ValueError(f"measurement file is missing columns: {missing}")

        for line_number, row in enumerate(rows, start=2):
            try:
                timestamp = row["timestamp"].strip()
                sensor_id = row["sensor_id"].strip()
                quality_flag = row["quality_flag"].strip()
                temperature = float(row["temperature_celsius"])
                parsed_time = datetime.fromisoformat(
                    timestamp.replace("Z", "+00:00")
                )
            except (AttributeError, TypeError, ValueError) as error:
                raise ValueError(
                    f"invalid measurement on line {line_number}"
                ) from error
            if not sensor_id or not quality_flag or parsed_time.tzinfo is None:
                raise ValueError(
                    f"incomplete measurement metadata on line {line_number}"
                )
            if not math.isfinite(temperature):
                raise ValueError(
                    f"non-finite temperature on line {line_number}"
                )
            if temperature < ABSOLUTE_ZERO_CELSIUS:
                raise ValueError(
                    f"temperature below absolute zero on line {line_number}"
                )
            measurements.append(
                Measurement(timestamp, sensor_id, temperature, quality_flag)
            )

    if not measurements:
        raise ValueError("measurement file contains no observations")
    return measurements


def summarize_temperatures(
    measurements: list[Measurement],
    config: AnalysisConfig,
) -> TemperatureSummary:
    """Calculate a kelvin summary from accepted, calibrated observations."""

    accepted_kelvin = [
        observation.temperature_celsius
        + config.calibration_offset_celsius
        + KELVIN_OFFSET
        for observation in measurements
        if observation.quality_flag in config.accepted_quality_flags
    ]
    if not accepted_kelvin:
        raise ValueError("no measurements have an accepted quality flag")
    if min(accepted_kelvin) < 0.0:
        raise ValueError("calibration produces a value below absolute zero")
    return TemperatureSummary(
        total_measurements=len(measurements),
        accepted_measurements=len(accepted_kelvin),
        minimum_kelvin=min(accepted_kelvin),
        mean_kelvin=statistics.fmean(accepted_kelvin),
        maximum_kelvin=max(accepted_kelvin),
    )


def summary_document(summary: TemperatureSummary) -> dict[str, object]:
    """Attach units and a schema version to the numerical result."""

    return {
        "schema_version": 1,
        "measurements": {
            "total": summary.total_measurements,
            "accepted": summary.accepted_measurements,
            "rejected": (
                summary.total_measurements - summary.accepted_measurements
            ),
        },
        "temperature": {
            "unit": "K",
            "minimum": summary.minimum_kelvin,
            "mean": summary.mean_kelvin,
            "maximum": summary.maximum_kelvin,
        },
    }


def main() -> int:
    """Run the command-line analysis."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("measurements", type=Path)
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).with_name("analysis_config.json"),
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument("--manifest", type=Path)
    arguments = parser.parse_args()
    if arguments.manifest is not None and arguments.output is None:
        parser.error("--manifest requires --output")

    try:
        config = load_config(arguments.config)
        measurements = read_measurements(arguments.measurements)
        summary = summarize_temperatures(measurements, config)
        if arguments.output is not None:
            write_json(arguments.output, summary_document(summary))
        if arguments.manifest is not None:
            manifest = run_manifest(
                script_path=Path(__file__).resolve(),
                measurements_path=arguments.measurements,
                config_path=arguments.config,
                output_path=arguments.output,
                accepted_quality_flags=config.accepted_quality_flags,
                calibration_offset_celsius=config.calibration_offset_celsius,
                command=[
                    Path(sys.executable).name,
                    Path(__file__).name,
                    *sys.argv[1:],
                ],
            )
            write_json(arguments.manifest, manifest)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Mean temperature: {summary.mean_kelvin:.2f} K")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
