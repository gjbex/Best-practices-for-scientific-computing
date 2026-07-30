# Quality-controlled temperature analysis

This small program supports the running example in the *Best practices for
scientific computing* training.  It asks a simple scientific question:

> Given a set of sensor measurements, what was the mean experimental
> temperature, and can we trust and reproduce that result?

The example is written in Python so that it can run without compilation or
third-party dependencies.  The underlying practices apply equally to compiled
and interpreted scientific software.


## Files

* `measurements.csv` contains timestamped observations, sensor identifiers,
  units encoded in the column name, and quality flags.
* `analysis_config.json` records the accepted quality flags and calibration
  offset.
* `temperature_analysis.py` validates the inputs, summarizes accepted
  observations, and provides the command-line interface.
* `provenance.py` provides helpers for atomic JSON output and run provenance.
* `test_temperature_analysis.py` checks a known result, scientific properties,
  invalid input, quality filtering, and the complete command-line workflow.
* `check_result.py` is the small end-to-end check used in the version-control
  demonstration.


## Run the analysis

The shortest invocation prints the mean of the five accepted observations:

```bash
python3 temperature_analysis.py measurements.csv
```

It should report:

```text
Mean temperature: 293.15 K
```

One additional observation is retained in the input but excluded by its
`rejected` quality flag.  Keeping it in the raw data makes that decision
visible instead of silently deleting the observation.


## Record a reproducible run

Use a new directory for an important run so that previous results are not
silently overwritten:

```bash
run_directory=$(mktemp -d)
python3 temperature_analysis.py measurements.csv \
    --config analysis_config.json \
    --output "$run_directory/temperature_summary.json" \
    --manifest "$run_directory/run_manifest.json"
```

The summary identifies its schema and unit.  The manifest records

* the command;
* the input and configuration file checksums;
* the effective analysis parameters;
* the analysis script checksum, Git revision, and modification state;
* the Python implementation, version, and platform; and
* the output file checksum.

This information makes the small example auditable and rerunnable.  It does not
prove that the sensor was calibrated correctly, that the accepted measurements
are representative, or that a different platform will always produce
bit-for-bit identical output.


## Run the checks

Run all software and scientific checks with one standard-library command:

```bash
python3 -m unittest discover -s . -p 'test_*.py'
```

The checks establish that

* the reference observations produce the expected mean;
* the mean lies between the minimum and maximum;
* reordering observations does not change the mean;
* shifting every observation shifts the mean by the same amount;
* rejected observations are excluded;
* physically impossible input is rejected; and
* a complete run writes interpretable output and matching provenance.

These checks provide evidence for specific claims.  They cannot establish that
the measurements, calibration decision, or scientific interpretation are
correct in every experimental setting.
