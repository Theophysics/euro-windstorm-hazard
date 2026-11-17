"""Generalised Extreme Value fits and return levels.

Note on sign convention: scipy.stats.genextreme uses a shape parameter c
that is the NEGATIVE of the xi used in most climate literature (c = -xi).
Decide which one this module exposes and say so in the docstrings.
"""

import numpy as np


def fit_gev(maxima) -> tuple[float, float, float]:
    """Fit a GEV distribution to a 1D sample of block maxima.

    Returns
    -------
    (shape, loc, scale)
    """
    raise NotImplementedError


def return_level(params: tuple[float, float, float], return_period: float) -> float:
    """Gust exceeded on average once every `return_period` winters.

    This is the quantile with non-exceedance probability 1 - 1/return_period.
    """
    raise NotImplementedError


def bootstrap_return_level(maxima, return_period: float, n_boot: int = 200,
                           seed: int | None = None) -> np.ndarray:
    """Return levels from `n_boot` resamples (with replacement) of the maxima.

    Take percentiles of the result (e.g. 5th and 95th) for a confidence interval.
    """
    raise NotImplementedError
