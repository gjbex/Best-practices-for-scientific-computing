"""Starter tests for the numerical-integration exercise."""

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

        self.assertTrue(
            math.isclose(result, 10.0, rel_tol=0.0, abs_tol=1.0e-14)
        )

    @unittest.skip("TODO: choose a tolerance from the discretization error")
    def test_quadratic_matches_analytical_result(self) -> None:
        """Compare x² on [0, 1] with its analytical integral."""

    @unittest.skip("TODO: compare errors after halving the step size")
    def test_quadratic_converges_at_second_order(self) -> None:
        """Check that refinement reduces the error by about four."""

    @unittest.skip("TODO: formulate the relation between reversed bounds")
    def test_reversing_bounds_changes_the_sign(self) -> None:
        """Check a relation between two runs without a stored answer."""


if __name__ == "__main__":
    unittest.main()
