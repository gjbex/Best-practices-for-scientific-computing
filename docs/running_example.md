# Running example: trustworthy temperature analysis

The training revisits one small scientific analysis to connect its topics.  The
analysis asks:

> Given a set of sensor measurements, what was the mean experimental
> temperature, and can we trust and reproduce that result?

The [reference implementation](running_example/reference_implementation/README.md)
reads timestamped temperature observations, applies an explicit quality and
calibration configuration, calculates a summary in kelvin, and can write a run
manifest.  It uses Python's standard library so that it remains easy to run,
but the design questions and practices apply to every language track.


## How the example develops

| Stage | Question illustrated by the example |
|-------|-------------------------------------|
| readable code | Can another researcher identify the units, constants, validation rules, and steps of the analysis? |
| traceable changes | Can we find the change that altered the scientific result and recover the working version? |
| meaningful tests | What known result, physical bound, or relation between runs would reveal an incorrect analysis? |
| documented interfaces | Does the program state its required columns, units, parameters, failure conditions, and output meaning? |
| interpretable data | Can a future reader distinguish timestamps, sensors, units, quality decisions, and schema versions? |
| automated checks | Can the same fast checks run after each proposed change without depending on a developer's memory? |
| reproducible results | Can a result be connected to its inputs, configuration, code state, command, environment, and output? |

The stages are not independent.  A test depends on a clear interface; an
interpretable result depends on documented units; and a run manifest is useful
only if the recorded inputs and parameters have stable meanings.


## What participants see

The example is used as a short recurring illustration, not as a second course
inside the training.

1. In [code style](code_style.md), the implementation demonstrates descriptive
   names, small functions, explicit constants, and visible units.
2. In the [version-control demonstration](version_control_demo.md), an
   instructor changes the Kelvin conversion, inspects the difference, and
   restores the working result.
3. In [testing](testing/index.md), the checks combine a known answer, input
   validation, a physical bound, and relations that should hold when
   observations are reordered or shifted.
4. In [documentation](documentation.md), the CSV schema, configuration,
   command-line interface, assumptions, and limitations form an explicit
   contract.
5. In [scientific I/O](scientific_io.md), raw observations retain timestamps,
   sensor identifiers, units, and quality flags, while the result identifies
   its schema and unit.
6. In [continuous integration](continuous_integration.md), one fast command
   runs the same checks locally and in an automated workflow.
7. In [reproducibility](reproducibility.md), a manifest records checksums,
   effective parameters, code state, the interpreter, the command, and the
   output.

These revisits should take only a few minutes within each scheduled topic.  No
additional schedule block is needed.


## Optional hands-on follow-up

The [self-study exercise](running_example/exercise/README.md) lets participants
apply the narrative to an incomplete version of the analysis.  It provides a
starter state, progressive tasks, executable checks, differentiated routes,
and the complete implementation as a reference.

The exercise is **not part of the four-hour session**.  It is intended for
participants to complete afterwards, at their own pace, to consolidate the
ideas and practise the parts most relevant to their own work.  During the
taught session, the example remains a short recurring illustration rather than
a participant coding assignment.


## Scientific claims and limitations

The implementation and tests provide evidence that accepted observations are
processed according to the documented rules.  They do not demonstrate that the
sensor was calibrated correctly, that the quality flags are justified, or that
the mean is an appropriate answer to every scientific question.

That distinction is deliberate: trustworthy scientific software requires both
correct implementation and a defensible scientific method.


## Explore the complete example

Create a disposable copy with its own known-working Git revision:

```bash
example_directory=$(bash docs/running_example/prepare_example.sh)
cd "$example_directory"
```

Run the analysis and all checks:

```bash
python3 temperature_analysis.py measurements.csv
python3 -m unittest discover -s . -p 'test_*.py'
```

The [reference implementation
README](running_example/reference_implementation/README.md) shows how to write the
structured summary and provenance manifest.  Detailed Git practice remains in
the separate [Version control with
Git](https://gjbex.github.io/Version-control-with-git/) training.
