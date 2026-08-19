"""A minimal composite trapezoidal-rule implementation."""

from __future__ import annotations

from collections.abc import Callable


def composite_trapezoidal(
    function: Callable[[float], float],
    lower_bound: float,
    upper_bound: float,
    intervals: int,
) -> float:
    """Approximate an integral using equally sized subintervals."""

    if isinstance(intervals, bool) or not isinstance(intervals, int):
        raise TypeError("intervals must be an integer")
    if intervals <= 0:
        raise ValueError("intervals must be positive")

    step = (upper_bound - lower_bound) / intervals
    weighted_sum = 0.5 * (
        function(lower_bound) + function(upper_bound)
    )
    weighted_sum += sum(
        function(lower_bound + index * step)
        for index in range(1, intervals)
    )
    return step * weighted_sum
