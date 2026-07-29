#!/usr/bin/env python3

import csv
import sys
from pathlib import Path


KELVIN_OFFSET = 273.15


def read_temperatures(path: Path) -> list[float]:
    with path.open(newline="", encoding="utf-8") as csv_file:
        rows = csv.DictReader(csv_file)
        return [float(row["temperature_celsius"]) for row in rows]


def mean_temperature_kelvin(temperatures_celsius: list[float]) -> float:
    if not temperatures_celsius:
        raise ValueError("at least one temperature measurement is required")
    mean_celsius = sum(temperatures_celsius) / len(temperatures_celsius)
    return mean_celsius + KELVIN_OFFSET


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} MEASUREMENTS.csv", file=sys.stderr)
        return 2

    temperatures = read_temperatures(Path(sys.argv[1]))
    mean_kelvin = mean_temperature_kelvin(temperatures)
    print(f"Mean temperature: {mean_kelvin:.2f} K")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
