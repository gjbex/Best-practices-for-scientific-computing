#!/usr/bin/env python3

import math
import subprocess
import sys
from pathlib import Path


EXPECTED_MEAN_KELVIN = 293.15
DATA_FILE = Path(__file__).with_name("measurements.csv")
ANALYSIS_FILE = Path(__file__).with_name("temperature_analysis.py")


def main() -> int:
    completed = subprocess.run(
        [sys.executable, str(ANALYSIS_FILE), str(DATA_FILE)],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        print("FAIL: temperature analysis did not run successfully")
        if completed.stderr:
            print(completed.stderr.rstrip())
        return 1

    output = completed.stdout.strip()
    try:
        observed = float(output.removeprefix("Mean temperature: ").removesuffix(" K"))
    except ValueError:
        print(f"FAIL: unexpected analysis output: {output!r}")
        return 1

    if math.isclose(
        observed,
        EXPECTED_MEAN_KELVIN,
        rel_tol=0.0,
        abs_tol=0.005,
    ):
        print(f"PASS: mean temperature is {observed:.2f} K")
        return 0

    print(
        f"FAIL: expected {EXPECTED_MEAN_KELVIN:.2f} K, "
        f"observed {observed:.2f} K"
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
