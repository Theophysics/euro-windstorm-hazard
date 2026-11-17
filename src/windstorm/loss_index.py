"""Storm loss index after Klawa & Ulbrich (2003)."""

import numpy as np


def storm_loss_index(gust, v98, population) -> float:
    """Population-weighted loss index for one storm footprint.

    LI = sum over cells of population * (gust / v98 - 1)**3,
    counting only cells where gust > v98.

    Parameters
    ----------
    gust : array, maximum gust per cell during the storm (m/s)
    v98 : array, local 98th percentile of daily maximum gust (m/s)
    population : array, population per cell

    All three arrays share the same shape.
    """
    raise NotImplementedError
