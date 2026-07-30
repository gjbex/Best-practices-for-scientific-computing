"""Reference scientific tests for composite trapezoidal integration."""

from __future__ import annotations

import math
import unittest

from integration import composite_trapezoidal


class CompositeTrapezoidalTests(unittest.TestCase):
    def test_linear_function_matches_analytical_result(self) -> None:
        result = composite_trapezoidal(
            lambda value: 3.0 * value + 2.0,
            lower_bound=0.0,
            upper_bound=2.0,
            intervals=12,
        )

        # The trapezoidal rule is exact for a linear function.  The small
        # absolute tolerance covers floating-point accumulation only.
        self.assertTrue(
            math.isclose(result, 10.0, rel_tol=0.0, abs_tol=1.0e-14)
        )

    def test_quadratic_matches_analytical_result(self) -> None:
        intervals = 100
        result = composite_trapezoidal(
            lambda value: value**2,
            lower_bound=0.0,
            upper_bound=1.0,
            intervals=intervals,
        )

        # For x² on [0, 1], the trapezoidal error is 1 / (6 n²).
        # The 1% margin covers rounding without hiding discretization error.
        absolute_tolerance = 1.01 / (6.0 * intervals**2)
        self.assertTrue(
            math.isclose(
                result,
                1.0 / 3.0,
                rel_tol=0.0,
                abs_tol=absolute_tolerance,
            )
        )

    def test_quadratic_converges_at_second_order(self) -> None:
        exact_result = 1.0 / 3.0
        coarse_result = composite_trapezoidal(
            lambda value: value**2,
            lower_bound=0.0,
            upper_bound=1.0,
            intervals=20,
        )
        fine_result = composite_trapezoidal(
            lambda value: value**2,
            lower_bound=0.0,
            upper_bound=1.0,
            intervals=40,
        )

        coarse_error = abs(coarse_result - exact_result)
        fine_error = abs(fine_result - exact_result)
        error_reduction = coarse_error / fine_error

        # Second-order convergence predicts a factor of four when the step
        # size is halved.  A 2% tolerance distinguishes it from first order.
        self.assertTrue(
            math.isclose(error_reduction, 4.0, rel_tol=0.02, abs_tol=0.0)
        )

    def test_reversing_bounds_changes_the_sign(self) -> None:
        forward = composite_trapezoidal(
            lambda value: value**2 + 1.0,
            lower_bound=-1.0,
            upper_bound=2.0,
            intervals=50,
        )
        reverse = composite_trapezoidal(
            lambda value: value**2 + 1.0,
            lower_bound=2.0,
            upper_bound=-1.0,
            intervals=50,
        )

        self.assertTrue(
            math.isclose(forward, -reverse, rel_tol=0.0, abs_tol=1.0e-14)
        )


if __name__ == "__main__":
    unittest.main()
