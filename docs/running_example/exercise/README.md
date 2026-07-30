# Optional self-study exercise

> **This exercise is not part of the four-hour training schedule.**  It is
> intended for participants to complete in their own time after the session.
> It reinforces the course narrative, but nobody is expected to finish it
> during the taught session.

The exercise develops the [running temperature
analysis](../../running_example.md) from an incomplete but runnable starter
into a trustworthy computational experiment.  The starting point provides the
CSV reader, configuration reader, command-line interface, and six checks.
Four checks initially fail because the scientific calculation, validation, and
output metadata are incomplete.

The work is deliberately self-paced.  Depending on your programming and
testing experience, allow roughly one to two hours.  Taking longer, completing
only the core tasks, or translating the exercise to your usual programming
language are all reasonable ways to use it.


## Learning purpose

By working through the exercise, you will practise how to

* make units and scientific decisions explicit in code;
* turn a scientific expectation into an executable check;
* distinguish a plausible-looking number from a supported result;
* document the interface between code, configuration, and data; and
* connect local checks with automation and reproducibility.

The exercise does not teach Git commands.  If you already use version control,
recording each completed stage is useful practice.  For hands-on Git
instruction, use the separate [Version control with
Git](https://gjbex.github.io/Version-control-with-git/) training.


## Prepare a working copy

From the root of this repository, create a disposable copy:

```bash
exercise_directory=$(bash docs/running_example/prepare_exercise.sh)
cd "$exercise_directory"
```

Only Python 3 and its standard library are required.

Run the incomplete analysis:

```bash
python3 temperature_analysis.py measurements.csv
```

It initially reports `22.50 K`.  That output is intentionally wrong: the
starter treats every value as though it were already expressed in kelvin and
does not apply the quality decision or calibration configuration.

Run the checks:

```bash
python3 -m unittest discover -s . -p 'test_*.py'
```

The starter should run six checks: two pass and four fail.  A failing starter is
expected here; it gives each task a visible completion criterion.


## Task 1: understand the scientific contract

Inspect `measurements.csv` and `analysis_config.json` before changing the code.
Answer these questions:

1. Which column states the input unit?
2. Why should the rejected observation remain in the raw data?
3. Which configuration values affect the result?
4. What result should the five accepted observations produce?
5. Which assumptions cannot be established from these files alone?

Write short answers in a `NOTES.md` file.  This makes the scientific decisions
visible before they become implementation details.


## Task 2: implement the accepted temperature summary

Complete the TODO in `summarize_temperatures`.

The calculation should

1. select observations whose quality flag is accepted by the configuration;
2. apply the calibration offset, which is expressed in degrees Celsius;
3. convert accepted values to kelvin;
4. reject a calculation with no accepted observations; and
5. compute the count, minimum, mean, and maximum.

Do not hard-code `293.15`: the program must calculate it from the observations
and configuration.

Verify this stage with:

```bash
python3 temperature_analysis.py measurements.csv
python3 -m unittest \
    test_temperature_analysis.TemperatureSummaryTests.test_known_result_and_bounds \
    test_temperature_analysis.TemperatureSummaryTests.test_rejected_observation_does_not_affect_the_mean
```


## Task 3: reject physically impossible input

Complete the validation TODO in `read_measurements`.  A finite temperature
below absolute zero must be rejected with a clear `ValueError`.

Then run:

```bash
python3 -m unittest \
    test_temperature_analysis.TemperatureSummaryTests.test_input_below_absolute_zero_is_rejected
```

Consider what this check establishes and what it does not.  A value above
absolute zero can still be caused by a faulty sensor, wrong unit, or unsuitable
quality decision.


## Task 4: make the output interpretable

Complete `summary_document` so that its structure includes

* a schema version;
* total, accepted, and rejected measurement counts;
* the minimum, mean, and maximum; and
* the unit `K`.

Run:

```bash
python3 -m unittest \
    test_temperature_analysis.OutputTests.test_summary_document_records_meaning
```

The important result is not the choice of JSON syntax.  It is that a reader
does not have to guess what a number represents.


## Task 5: assess and extend the tests

Run the complete suite:

```bash
python3 -m unittest discover -s . -p 'test_*.py'
```

All six supplied checks should now pass.  Read each test and identify the claim
it supports:

* comparison with a known small result;
* physical and numerical bounds;
* independence from observation order;
* a predictable response to shifting every input;
* exclusion of rejected observations; and
* input and output validation.

Add one further test of your own.  Useful possibilities include an empty file,
no accepted observations, a non-finite value, a calibration offset, or a
missing required column.  State in a comment what the test would and would not
detect.


## Task 6: document the interface

Create a short `README.md` for your completed program.  Document

* the command needed to run it;
* required CSV columns and their units;
* configuration keys and their meaning;
* the quality-filtering and calibration rules;
* the output fields;
* important failure conditions; and
* at least two scientific limitations.

Compare the result with the [reference implementation
README](../reference_implementation/README.md).  Clear documentation matters
more than using identical wording.


## Optional extension: automation and provenance

If you want a larger challenge, continue with one or more of these tasks:

1. Add command-line options for a structured output file.
2. Record the input, configuration, code, and output checksums in a run
   manifest.
3. Record the effective parameters, command, interpreter version, and Git
   revision.
4. Inspect the repository's running-example CI workflow and identify the local
   command it automates.
5. Port the calculation and its scientific checks to C, C++, Fortran, Rust,
   Julia, or R.

The [reference implementation](../reference_implementation/README.md) includes
the structured output and run-manifest extension.  Its implementation is a
reference, not the only valid solution.


## Routes for different experience levels

| If you... | Suggested route |
|-----------|-----------------|
| are new to automated testing | complete Tasks 1–4, use the supplied tests as guidance, and then compare with the reference |
| already write tests regularly | avoid the reference until Task 5 and add at least two edge-case or property tests |
| mainly use another language | answer Task 1, then reproduce Tasks 2–5 with that language's normal test framework |
| have limited time | complete Tasks 1–3; these contain the central scientific-code and testing lessons |
| want a larger project | complete all tasks and one automation or provenance extension |


## Completion check

Your core exercise is complete when

```bash
python3 temperature_analysis.py measurements.csv
python3 -m unittest discover -s . -p 'test_*.py'
```

reports `Mean temperature: 293.15 K` and all supplied checks pass.

Finishing the files is not the only goal.  You should also be able to explain
why the result is more trustworthy than the starter result and which scientific
uncertainties remain outside the program.


## Guidance for trainers

Introduce the exercise as an optional follow-up during the wrap-up and show
participants where to find the starter and reference implementation.  Do not
allocate it a slot in the four-hour timetable or make completion an implicit
requirement of the session.  Participants with questions can revisit the
relevant topic pages or compare one task at a time with the reference after the
session.
