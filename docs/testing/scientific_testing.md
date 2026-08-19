# Testing scientific software

Tests for scientific software use the same frameworks and automation as tests
for other software, but choosing a meaningful expected result is often harder.
Floating-point results may vary slightly, an iterative method may have no simple
exact answer, and a stochastic simulation should not produce the same outcome
on every run.

A test that only checks whether the program completed, produced an array of the
right size, or wrote an output file is useful, but it does not establish that
the scientific result is credible.  Scientific tests should also ask whether
the result has the expected numerical and domain-specific properties.


## What does a test establish?

It is useful to distinguish three kinds of evidence.

* **Software behavior:** Does the program accept valid input, reject invalid
  input, and produce output in the documented form?
* **Numerical behavior:** Does the algorithm reproduce known solutions,
  converge as expected, and satisfy its stopping criteria?
* **Scientific behavior:** Does the result preserve relevant invariants, remain
  within physically meaningful bounds, and agree with trusted observations or
  reference calculations where appropriate?

No single test establishes all three.  Passing tests provide evidence for the
specific claims they check; they do not prove that the implementation, model,
or scientific interpretation is correct in every situation.

A coverage report cannot make this distinction.  It can show that a numerical
routine executed, but only the assertions reveal whether software behavior,
numerical behavior, or scientific behavior was examined.


## Finding an expected result

The value or property against which a result is checked is sometimes called a
*test oracle*.  Useful oracles for scientific software include the following.

| Oracle | Example | Main limitation |
|--------|---------|-----------------|
| analytical solution | compare a solver with a problem whose exact solution is known | exact solutions may cover only simple cases |
| invariant | check conservation of mass, symmetry, positivity, or boundedness | preserving one property does not guarantee the entire result is correct |
| convergence behavior | refine a time step or mesh and check that the error decreases at the expected rate | requires more than one calculation and a sufficiently resolved regime |
| independent implementation | compare with a simpler algorithm or separately developed code | the two implementations may share assumptions or defects |
| trusted reference data | compare selected quantities with a recorded result from a validated calculation | the provenance and validity range of the reference must be known |
| relation between runs | translate, rescale, reorder, or otherwise transform an input and predict how the output should change | only properties with a justified relation can be tested this way |

Prefer small cases that are easy to understand.  A large output file from an
old version of the same program is not automatically a reliable oracle: it may
preserve an old defect.


### Property-based testing

When an invariant or relation can be stated precisely, a property-based testing
tool can generate many inputs and check that property repeatedly.  Examples
include preserving positivity, obtaining the same result after reordering
independent observations, or predicting how an output changes when every input
is rescaled.

The property must be justified by the scientific problem, and the generated
inputs must cover the relevant domain.  Passing many generated cases does not
compensate for an invalid property or a generator that avoids difficult
regions.  Important analytical cases, boundaries, and previously observed
defects should still have explicit tests.


## Comparing floating-point results

Exact equality is appropriate for discrete results, such as an array size or
iteration status, but it is usually inappropriate for a value produced by
floating-point arithmetic.  A common comparison accepts a computed value
$a$ and reference value $b$ when

$$
  |a - b| \leq \mathrm{atol} + \mathrm{rtol}\,|b|.
$$

The absolute tolerance, `atol`, controls comparisons near zero.  The relative
tolerance, `rtol`, scales with the magnitude of the reference value.  Testing
frameworks generally provide an implementation of this comparison, so use
their assertion rather than writing a new one.

A tolerance should be justified by the calculation, not chosen merely to make
a failing test pass.  Relevant considerations include

* floating-point precision and the accumulation order;
* conditioning of the problem;
* discretization and truncation error;
* the stopping criterion of an iterative solver;
* reduction order in a parallel calculation; and
* differences between compilers and numerical libraries.

Different quantities may require different tolerances.  For arrays or fields,
consider both a norm of the overall error and local checks such as the maximum
absolute error.  Also test properties such as conservation or bounds when a
small norm could conceal a scientifically important local error.


## Example: testing numerical integration

Suppose a routine uses the composite trapezoidal rule to integrate $x^2$ from
zero to one.  The analytical answer is $1/3$, and the expected discretization
error is proportional to the square of the grid spacing.

A useful collection of tests could check that

1. integrating a constant or linear function gives the known result;
2. the result for $x^2$ agrees with $1/3$ within a tolerance appropriate
   for the chosen grid;
3. halving the grid spacing reduces the error by approximately a factor of
   four once the calculation is in the expected convergence regime;
4. reversing the integration limits changes the sign of the result; and
5. serial and parallel implementations agree within a justified tolerance.

These tests provide different evidence.  A single comparison with $1/3$
might pass even if the grid spacing were handled incorrectly.  The convergence
test is more likely to reveal that defect, while the sign-change test checks a
property that does not depend on a stored reference number.

The [runnable numerical-integration
exercise](numerical_integration/README.md) implements the serial tests above.
It focuses on analytical comparison, a tolerance derived from discretization
error, and observed second-order convergence.  Input handling, output metadata,
automation, and provenance remain in the [temperature-analysis running
example](../running_example.md) rather than being duplicated here.

This chapter provides an introduction suitable for the four-hour overview.  The
[Trustworthy Numerical Computing
training](https://gjbex.github.io/Trustworthy-numerical-computing/) develops a
more systematic workflow for distinguishing implementation defects, numerical
instability, and problem conditioning; choosing error measures and tolerances;
studying convergence; assembling validation evidence; and communicating the
limits of a numerical result.


## Iterative and stochastic calculations

For an iterative algorithm, test the quality of the final result rather than
requiring exactly the same sequence of intermediate values.  Suitable checks
include a residual below the documented threshold, reduction of an objective
function, preservation of an invariant, and convergence toward an analytical
or trusted solution.  An exact iteration count may vary with the platform or
library and is rarely the main scientific requirement.

A fixed random seed is useful for reproducing a defect and protecting against
unintended changes to a deterministic code path.  It does not demonstrate that
a stochastic method is statistically correct.  Depending on the claim being
tested, also check properties across multiple samples, such as

* whether values remain in the allowed range;
* whether an estimated mean or variance is consistent with a known result; or
* whether uncertainty decreases as the sample size increases.

Executing the stochastic code with one seed may give high line coverage, but it
does not establish the distributional behavior of the method.

Statistical acceptance criteria should state the sample size and expected
failure probability.  A test that fails randomly too often will be ignored,
while a very wide interval may fail to detect important regressions.


## Parallel calculations

Parallel execution can expose partitioning errors, incorrect halo exchanges,
races, and reductions whose results depend on execution order.  When practical,

* compare serial and parallel calculations on the same small input;
* test more than one thread or process count;
* check invariants that should be independent of the decomposition;
* include a case that exercises boundaries between subdomains; and
* allow justified rounding differences from non-associative floating-point
  reductions.

Executing every parallel line once does not explore different schedules,
decompositions, rank or thread counts, races, or accelerator execution paths.
These require deliberately selected configurations and acceptance criteria.

Bitwise-identical results are a separate requirement, not a sensible default
for every parallel program.  If bitwise reproducibility is required, document
the compiler, libraries, runtime settings, hardware assumptions, and reduction
strategy needed to provide it.


## Reference data and test cost

Keep reference inputs and outputs small enough for routine testing.  Record how
reference data was produced, including the source version, configuration,
units, relevant dependencies, and the reason it is trusted.  When full output
is too large, store scientifically meaningful summaries such as norms,
residuals, conserved quantities, or selected observables.

Most tests should run quickly on every change.  More expensive convergence,
statistical, multi-platform, or large-scale parallel tests can run in a
separate continuous-integration job or on a schedule.  A useful test strategy
therefore combines

* fast tests of small analytical cases, edge cases, and invariants;
* a few end-to-end regression and convergence tests; and
* less frequent validation on representative scientific workloads and
  supported computing environments.


## Short activity

Consider a simulation of diffusion in a periodic domain.  The program has a
serial and a parallel implementation and writes a field at a requested final
time.

In small groups, identify

1. one basic software-behavior test;
2. one invariant or physically meaningful bound;
3. one analytical or independently computable result;
4. one convergence test;
5. one parallel-consistency test; and
6. the acceptance criterion and provenance information each comparison needs.

For every proposed test, state what a passing result would demonstrate and one
defect or scientific problem that the test would not detect.
