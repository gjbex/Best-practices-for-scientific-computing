#!/usr/bin/env python3

"""Starter implementation for the temperature-analysis exercise."""

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
    return AnalysisConfig(
        accepted_quality_flags=frozenset(
            values["accepted_quality_flags"]
        ),
        calibration_offset_celsius=float(
            values["calibration_offset_celsius"]
        ),
    )


def read_measurements(path: Path) -> list[Measurement]:
    """Read timestamped temperature observations from CSV."""

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

            # TODO: Reject a finite value below absolute zero.

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
    """Return a preliminary summary that still needs scientific corrections."""

    # TODO: Filter on quality, apply calibration, and convert to kelvin.
    temperatures = [
        observation.temperature_celsius for observation in measurements
    ]

    return TemperatureSummary(
        total_measurements=len(measurements),
        accepted_measurements=len(temperatures),
        minimum_kelvin=min(temperatures),
        mean_kelvin=statistics.fmean(temperatures),
        maximum_kelvin=max(temperatures),
    )


def summary_document(summary: TemperatureSummary) -> dict[str, object]:
    """Return an incomplete document for the output-metadata task."""

    # TODO: Add the schema, counts, statistics, and unit.
    return {"mean_temperature": summary.mean_kelvin}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("measurements", type=Path)
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).with_name("analysis_config.json"),
    )
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    try:
        config = load_config(arguments.config)
        measurements = read_measurements(arguments.measurements)
        summary = summarize_temperatures(measurements, config)
        if arguments.output is not None:
            arguments.output.write_text(
                json.dumps(summary_document(summary), indent=2) + "\n",
                encoding="utf-8",
            )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Mean temperature: {summary.mean_kelvin:.2f} K")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
