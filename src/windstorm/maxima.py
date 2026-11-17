"""Winter (October-March) block maxima of daily gust fields."""

import numpy as np
import xarray as xr


def winter_year(time) -> np.ndarray:
    """Label each date with its winter season.

    A winter is named after the year of its January: October 1999 to
    March 2000 is winter 2000. Only meaningful for October-March dates.

    Parameters
    ----------
    time : array-like of datetime64

    Returns
    -------
    numpy.ndarray of int
    """
    raise NotImplementedError


def winter_maxima(gust: xr.DataArray) -> xr.DataArray:
    """Maximum gust per grid cell for each winter.

    Parameters
    ----------
    gust : DataArray with dims (time, latitude, longitude), daily maximum gust in m/s.
        Dates outside October-March are ignored.

    Returns
    -------
    DataArray with dims (winter, latitude, longitude).
    """
    raise NotImplementedError
