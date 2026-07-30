# Testing

Testing your software is an essential part of the development process.  It is
important to have tests in place before you start optimizing or rewriting your
code. The following sections deal with specific aspects of testing and types of
tests:

* [testing as experiments](testing_as_experiments.md);
* [testing scientific software](scientific_testing.md);
* [unit testing](unit_testing.md);
* [functional testing](functional_testing.md);
* [code coverage](code_coverage.md).

> **Running example — meaningful tests.**  The [temperature-analysis
> checks](../running_example.md) include a known small result, invalid-input and
> quality-filtering cases, a physical lower bound, and relations that should
> hold when observations are reordered or shifted.  Each test supports a
> particular claim; none proves that the experimental design is scientifically
> valid in every setting.
