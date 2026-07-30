# Runnable example: testing numerical integration

This small exercise complements the
[temperature-analysis running example](../../running_example.md).  The running
example already demonstrates input validation, scientific properties,
interpretable output, automation, and provenance.  This exercise does not
repeat those topics.  It concentrates on three aspects of numerical software:

* comparison with an analytical result;
* a tolerance derived from discretization error; and
* verification of the expected convergence rate.

The implementation uses the composite trapezoidal rule and Python's standard
library.  The testing ideas transfer directly to other languages and numerical
methods.

An instructor can run the reference tests as a short demonstration during the
scheduled testing block.  Writing the tests is an optional exercise that
participants can complete afterwards; it does not require an additional slot
in the four-hour timetable.


## Scientific problem

The function `composite_trapezoidal` approximates an integral by dividing the
interval into equal subintervals.  For a sufficiently smooth function, its
discretization error should decrease in proportion to the square of the step
size.

For the integral of `x²` from zero to one:

* the analytical result is `1/3`;
* with `n` subintervals, the trapezoidal result has error `1 / (6 n²)`; and
* doubling `n` should therefore reduce the error by a factor of approximately
  four.

These facts provide stronger tests than comparing one output with an
arbitrarily chosen number of decimal places.


## Prepare the exercise

From the root of this repository, create a disposable working copy:

```bash
exercise_directory=$(bash \
    docs/testing/numerical_integration/prepare_exercise.sh)
cd "$exercise_directory"
```

Run the starter tests:

```bash
python3 -m unittest -v
```

The starter contains one passing analytical test for a linear function and
three skipped test skeletons.  Remove each `@unittest.skip` annotation as you
complete the corresponding task.


## Task 1: compare with an analytical result

Complete `test_quadratic_matches_analytical_result`.

Use 100 subintervals to integrate `x²` from zero to one.  Compare the result
with `1/3` using `math.isclose` with

```text
relative tolerance = 0
absolute tolerance = 1.01 / (6 × 100²)
```

The factor `1.01` leaves a small margin for floating-point rounding around the
known discretization-error bound.  It is not a number chosen after observing a
failure.

This test shows that one calculation is consistent with an analytical result
at the selected resolution.  It does not show that refinement behaves
correctly.


## Task 2: check convergence

Complete `test_quadratic_converges_at_second_order`.

1. Calculate the absolute errors for 20 and 40 subintervals.
2. Divide the coarse-grid error by the fine-grid error.
3. Check that the ratio is close to four, using a relative tolerance of two
   percent.

The expected ratio comes from second-order convergence: halving the step size
should reduce an error proportional to the step-size squared by a factor of
four.  The two-percent interval is tight enough to distinguish the expected
order from first-order behavior while allowing minor floating-point effects.

The test checks observed behavior at two resolutions.  A production solver may
need several resolutions to establish that it has entered the asymptotic
convergence regime.


## Task 3: test a relation between runs

Complete `test_reversing_bounds_changes_the_sign`.

Calculate the same integral with forward and reversed bounds.  Check that the
two results have opposite signs within an absolute tolerance of `1e-14`.

This relation does not depend on storing a reference result.  It can reveal
some defects that a single analytical comparison might miss, but it cannot
establish the convergence order.


## Task 4: evaluate the test collection

Run the complete test suite:

```bash
python3 -m unittest -v
```

All four tests should pass.  For each test, write down

1. the numerical claim it supports;
2. one implementation defect it could reveal; and
3. one defect or scientific limitation it would not reveal.

Then introduce one temporary defect in `integration.py`, such as using
`intervals - 1` when calculating the step size or omitting an interior sample.
Run the tests, record which ones fail, and restore the implementation.

The purpose is to assess the evidence supplied by the tests, not merely to
obtain four green results.


## Reference solution

The [reference tests](reference_implementation/test_integration.py) implement
the analytical, convergence, and reversal checks.  Compare them with your tests
after making your own tolerance choices and documenting your reasoning.

The reference uses `unittest` to avoid third-party dependencies.  In a real
project, use the test framework that fits the language and repository.


## Scope and extensions

This example addresses deterministic serial integration of a smooth function.
It does not cover

* singular or discontinuous integrands;
* adaptive quadrature and its stopping criterion;
* stochastic integration;
* round-off-dominated refinement; or
* consistency between serial and parallel implementations.

Those cases require different oracles and acceptance criteria.  For an optional
extension, repeat the exercise for another quadrature method, derive its
expected order, and choose resolutions that expose that order.
