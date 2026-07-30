#!/usr/bin/env python3

"""Completion checks for the self-study temperature exercise."""

from __future__ import annotations

import math
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from temperature_analysis import (
    AnalysisConfig,
    Measurement,
    read_measurements,
    summarize_temperatures,
    summary_document,
)

CONFIG = AnalysisConfig(frozenset({"accepted"}), 0.0)
TOLERANCE = 1.0e-12


def observations(values: list[float]) -> list[Measurement]:
    return [
        Measurement(
            f"2026-04-12T{index:02d}:00:00Z",
            "test-sensor",
            value,
            "accepted",
        )
        for index, value in enumerate(values)
    ]


class TemperatureSummaryTests(unittest.TestCase):
    def assert_close(self, observed: float, expected: float) -> None:
        self.assertTrue(
            math.isclose(
                observed,
                expected,
                rel_tol=0.0,
                abs_tol=TOLERANCE,
            ),
            f"{observed} is not within {TOLERANCE} of {expected}",
        )

    def test_known_result_and_bounds(self) -> None:
        summary = summarize_temperatures(
            observations([18.0, 19.0, 20.0, 21.0, 22.0]),
            CONFIG,
        )

        self.assert_close(summary.mean_kelvin, 293.15)
        self.assertLessEqual(summary.minimum_kelvin, summary.mean_kelvin)
        self.assertLessEqual(summary.mean_kelvin, summary.maximum_kelvin)

    def test_reordering_does_not_change_the_mean(self) -> None:
        original = observations([18.0, 22.0, 19.0, 21.0, 20.0])

        forward = summarize_temperatures(original, CONFIG)
        reverse = summarize_temperatures(list(reversed(original)), CONFIG)

        self.assert_close(forward.mean_kelvin, reverse.mean_kelvin)

    def test_uniform_shift_changes_mean_by_the_same_amount(self) -> None:
        original = observations([18.0, 19.0, 20.0, 21.0, 22.0])
        shifted = [
            replace(item, temperature_celsius=item.temperature_celsius + 1.5)
            for item in original
        ]

        original_mean = summarize_temperatures(original, CONFIG).mean_kelvin
        shifted_mean = summarize_temperatures(shifted, CONFIG).mean_kelvin

        self.assert_close(shifted_mean - original_mean, 1.5)

    def test_rejected_observation_does_not_affect_the_mean(self) -> None:
        original = observations([18.0, 20.0, 22.0])
        rejected = replace(
            original[0],
            temperature_celsius=100.0,
            quality_flag="rejected",
        )

        summary = summarize_temperatures([*original, rejected], CONFIG)

        self.assertEqual(summary.accepted_measurements, 3)
        self.assert_close(summary.mean_kelvin, 293.15)

    def test_input_below_absolute_zero_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            data_path = Path(temporary_directory) / "impossible.csv"
            data_path.write_text(
                "timestamp,sensor_id,temperature_celsius,quality_flag\n"
                "2026-04-12T09:00:00Z,A17,-274.0,accepted\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "below absolute zero"):
                read_measurements(data_path)


class OutputTests(unittest.TestCase):
    def test_summary_document_records_meaning(self) -> None:
        summary = summarize_temperatures(
            observations([18.0, 20.0, 22.0]),
            CONFIG,
        )

        document = summary_document(summary)

        self.assertEqual(document.get("schema_version"), 1)
        self.assertEqual(document["measurements"]["accepted"], 3)
        self.assertEqual(document["measurements"]["rejected"], 0)
        self.assertEqual(document["temperature"]["unit"], "K")
        self.assert_close(document["temperature"]["mean"], 293.15)

    def assert_close(self, observed: float, expected: float) -> None:
        self.assertTrue(
            math.isclose(
                observed,
                expected,
                rel_tol=0.0,
                abs_tol=TOLERANCE,
            )
        )


if __name__ == "__main__":
    unittest.main()
