# Code coverage

Code coverage records which parts of a program execute while a selected test
suite or workload runs.  It is useful for locating unexercised code, but it
does not determine whether the executed code is correct or whether its results
were checked meaningfully.

Coverage is therefore structural evidence, not a certificate of software or
scientific correctness.  The [testing overview](index.md) discusses how it fits
with unit, functional, and scientific testing.


## What can be measured?

| Measure | Question it answers | Important limitation |
|---------|---------------------|----------------------|
| function coverage | Was each function entered? | A function may contain many untested decisions. |
| line or statement coverage | Was each instrumented line executed? | Executing a line does not show that its effect was asserted. |
| branch coverage | Were both outcomes of decisions such as `if` statements exercised? | It does not cover every combination of conditions or input values. |
| condition coverage | Did individual Boolean conditions evaluate both ways? | Interactions between conditions may still be missed. |

Branch coverage is often more informative than line coverage.  A conditional
line can be marked as executed even when only its normal path was taken and its
error path was never reached.


## State what the report covers

Coverage from unit tests answers a different question from coverage produced by
representative end-to-end workloads.  Record

* which tests or workloads ran;
* the build and instrumentation configuration;
* which source files and generated files were included;
* whether external, device, or dynamically loaded code was measurable; and
* any explicit exclusions.

Without this context, two percentages may describe different code and
execution environments.


## Use risk rather than a universal target

There is no percentage that is appropriate for every project.  An untested
branch in a unit conversion, numerical kernel, parameter validator, checkpoint
reader, or data transformation can be more important than many covered lines
of low-risk utility code.

When a line or branch is uncovered, decide whether to

1. add a test with an assertion that checks its intended behavior;
2. exercise it in a functional, platform-specific, or scheduled test;
3. remove genuinely dead or obsolete code;
4. refactor code whose decisions are too entangled to test clearly; or
5. document and narrowly exclude code that cannot be measured meaningfully.

Do not add a test that merely executes a line to increase a number.  Broadly
excluding difficult modules can also hide the numerical, parallel, or
error-handling code that most needs scrutiny.

High-risk components may justify demanding local expectations, while a lower
repository-wide value may be understandable when platform-specific regions are
tested elsewhere.  The reasoning matters more than a universal threshold.


## Coverage in continuous integration

Coverage can support review and regression detection when continuous
integration

* produces a browsable report rather than only a total percentage;
* highlights unexpected changes in modified or high-risk code;
* uses component-specific expectations where risks differ;
* reviews exclusions alongside source changes; and
* preserves the command, test selection, and build configuration used.

A threshold can prevent accidental loss of tests, but it is a project policy,
not a correctness claim.  A change to a scientific calculation still needs a
test with an appropriate oracle or property even when the coverage percentage
does not change.


## Instrumentation and environment limits

Coverage tools can only report code they can instrument and observe.

* Host-side reports may omit kernels executed on a GPU or accelerator.
* A generic CI runner may not reach MPI, scheduler, high-performance
  filesystem, or site-specific branches.
* Loading plugins or libraries dynamically can require additional
  configuration.
* Optimized, generated, or inlined code may be reported differently by
  different tools.

Use dedicated environments for behavior that matters but cannot run locally.
Do not interpret one report as representative of every supported platform.

Coverage builds are instrumented builds whose optimization and runtime behavior
may differ from production builds.  Do not use their timings for performance
conclusions.


## Practical workflow

1. Run the relevant tests or representative workloads with coverage enabled.
2. Inspect uncovered branches in high-risk code before considering the total
   percentage.
3. Add meaningful tests, route behavior to an appropriate test environment, or
   remove dead code.
4. Review exclusions and unexpected coverage changes.
5. Record important remaining gaps and the reason they are accepted.

The goal is to understand which important behavior has not been exercised, not
to make every report display 100 percent.
