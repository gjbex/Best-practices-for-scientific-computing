# Testing

Testing provides evidence about software behavior.  Different tests answer
different questions, so a trustworthy project usually combines several kinds
of evidence rather than relying on one framework, test level, or percentage.


## Layers of evidence

| Evidence | Main question | Typical scope |
|----------|---------------|---------------|
| [unit tests](unit_testing.md) | Does a small unit of work behave as specified, including important edge and error cases? | a function, method, module, or small component |
| [functional tests](functional_testing.md) | Does the application or workflow behave as its user expects? | a command, interface, application, or end-to-end use case |
| [scientific tests](scientific_testing.md) | Does the numerical or scientific result satisfy a justified oracle, property, or acceptance criterion? | algorithms, models, simulations, and relations between runs |
| [code coverage](code_coverage.md) | Which instrumented code executed while selected tests or workloads ran? | functions, statements, conditions, and branches |

These categories overlap.  A unit test can contain a scientific assertion, and
a functional test can compare an end-to-end result with reference data.
Coverage is different: it describes execution structure but does not determine
whether the assertions are meaningful.

The section on [testing as experiments](testing_as_experiments.md) provides the
common mindset: formulate a claim, design a test that could reveal a defect,
and state what a passing result does and does not establish.


## Building a test strategy

A practical strategy normally combines

* fast, focused tests for calculations, edge cases, and expected failures;
* scientific checks based on analytical results, invariants, convergence,
  trusted data, or justified relations between runs;
* a smaller number of end-to-end tests for important user workflows; and
* platform-specific or scheduled tests for behavior that ordinary CI cannot
  exercise, such as MPI, accelerators, or HPC filesystems.

Run inexpensive tests frequently.  More costly statistical, convergence,
parallel, or multi-platform tests can run less often, provided their role and
schedule are explicit.

> **Running example — meaningful tests.**  The [temperature-analysis
> checks](../running_example.md) include a known small result, invalid-input and
> quality-filtering cases, a physical lower bound, and relations that should
> hold when observations are reordered or shifted.  The [numerical-integration
> exercise](numerical_integration/README.md) adds an analytical oracle,
> discretization-aware tolerance, and convergence test.


## Assessing test-suite quality

No single score establishes that a test suite is good.  Useful questions
include

* Do failures localize the behavior that changed?
* Are important normal, edge, and error cases represented?
* Do numerical assertions use scientifically justified acceptance criteria?
* Are important user workflows and supported environments exercised?
* Have past defects become regression tests?
* Which important risks remain untested, and why?

Several techniques provide additional evidence:

* **Coverage analysis** locates functions, statements, conditions, or branches
  that the selected tests did not execute.
* **Mutation testing** makes small changes to the program and checks whether the
  tests detect them.  A surviving change to a sign, constant, comparison, or
  branch can reveal a weak or missing assertion.  Equivalent mutations and
  execution cost limit how broadly it should be used.
* **Property-based testing** generates many inputs for a justified invariant or
  relation.  The property and input generator must still reflect the scientific
  domain.
* **Fuzz testing** searches for crashes, hangs, and malformed-input failures.
  Not crashing is useful, but it does not establish numerical correctness.

Use these techniques to answer specific questions about risk and evidence, not
as additional percentages to maximize.
