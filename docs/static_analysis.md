# Static analysis

Static analysis examines source code without running the program.  It can find
potential defects early, often while the code is being written or compiled.
This makes it a useful complement to code review and testing.

Static analysis is especially valuable in scientific software.  A suspicious
conversion, an uninitialized value, or an inconsistent type can silently alter
a numerical result.  Finding such problems before a long simulation or
expensive HPC job starts saves both researcher time and computing resources.

However, a clean static-analysis report is not evidence that the scientific
method is correct.  An analyser cannot generally decide whether a physical
constant has the right value, a numerical method is appropriate, or a result
supports a scientific claim.


## Different tools provide different checks

Several related tools are commonly used during development.

| Tool | Main purpose | Typical findings |
|------|--------------|------------------|
| formatter | rewrites source into a consistent layout | indentation, spacing, line wrapping |
| compiler or interpreter diagnostics | reports problems understood by the language implementation | syntax errors, incompatible operations, unreachable code, suspicious conversions |
| linter | applies configurable rules to source code | likely mistakes, non-portable constructs, questionable idioms, and sometimes style |
| static type checker | checks whether values are used consistently with declared or inferred types | incompatible arguments, return values, assignments, and missing cases |
| broader static analyser | follows data and control flow without executing the program | uninitialized values, resource leaks, invalid memory use, and paths that may fail |

The boundaries are not exact.  A compiler may provide sophisticated static
analysis, while a linter may check types or correctness as well as style.  The
important question is not the tool's label, but which defects it can detect and
how it complements the other checks in the project.

A formatter is the exception in this table: it improves consistency but does
not normally look for correctness defects.  Formatting and static analysis can
be automated together, but they provide different kinds of feedback.


## A small example

The [running temperature analysis](running_example.md) uses type annotations
for its numerical values.  Suppose a change intended to format output
accidentally makes a conversion function return text:

```python
def kelvin_from_celsius(temperature_celsius: float) -> float:
    return f"{temperature_celsius + 273.15:.2f}"
```

This is valid Python syntax and the function can be called, but its annotation
says that it should return a number rather than a string.  A static type checker
can report that inconsistency before the value reaches a later calculation.

Now consider a different mistake:

```python
def kelvin_from_celsius(temperature_celsius: float) -> float:
    return temperature_celsius + 274.15
```

The types are consistent, so a type checker has no reason to object.  A test
using a known conversion or a scientifically meaningful relation is required
to expose the incorrect constant.  Static analysis and testing therefore
provide complementary evidence.


## Scientific relevance and limitations

Depending on the language and analyser, static checks can help detect

* variables that may be used before they are initialized;
* accidental integer arithmetic or narrowing conversions;
* inconsistent units represented by distinct types;
* ignored error conditions and missing cases;
* invalid memory access and resource-management mistakes;
* unreachable branches and conditions that are always true or false;
* non-portable or unsafe constructs; and
* interface mismatches between functions or modules.

These checks are useful, but they cannot normally establish that

* equations and physical constants are correct;
* units represented only as ordinary numbers are consistent;
* convergence criteria and numerical tolerances are justified;
* an algorithm is stable or appropriate for the problem;
* input data and reference results are scientifically valid; or
* parallel executions are free from every race or nondeterministic failure.

Some specialised analysers understand units, array shapes, memory access, or
parallel constructs, but only within the information and models they have been
given.  Their reports still need scientific and programming judgement.


## Use static analysis constructively

Enable the strongest practical compiler or interpreter diagnostics first, then
add tools that address important gaps.  A small project may need only a
formatter, compiler warnings, and one linter; a long-lived library may benefit
from type checking and deeper analysis as well.

For checks adopted by a project:

1. store their configuration in the repository;
2. run the same configuration locally and in continuous integration;
3. introduce new rules gradually when an existing code base has many findings;
4. investigate findings rather than changing code mechanically;
5. suppress a report only in the narrowest possible location and record why;
6. fix warnings in code you modify so that the warning baseline does not grow;
7. pin or record tool versions when changing versions could change the result.

Warnings are prompts for investigation, not proof of a defect.  Conversely,
silencing every warning does not prove correctness.  False positives, checks
that do not apply to a particular design, and defects outside the analyser's
model are all possible.


## Relationship to testing and continuous integration

Static analysis checks properties that can be inferred without executing the
software.  [Testing](testing/index.md) executes the software on selected inputs
and compares its behaviour with explicit expectations.  Scientific testing
adds known results, invariants, convergence evidence, and other domain
knowledge that a general-purpose analyser does not have.

[Continuous integration](continuous_integration.md) can run formatters, static
analysis, builds, and tests after each proposed change.  CI automates these
checks; it does not replace them or make their conclusions stronger.

See [choosing development tools](tools/choosing_tools.md) for selection
criteria and the language-specific [tool pages](tools/index.md) for candidate
formatters, linters, type checkers, and analysers.
