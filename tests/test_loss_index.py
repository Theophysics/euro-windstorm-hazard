import numpy as np
import pytest

from windstorm.loss_index import storm_loss_index


def test_only_cells_above_threshold_contribute():
    gust = np.array([[20.0, 33.0]])
    v98 = np.array([[22.0, 30.0]])
    population = np.array([[100.0, 1000.0]])
    # First cell is below its threshold; second gives 1000 * (33/30 - 1)**3 = 1.0
    assert storm_loss_index(gust, v98, population) == pytest.approx(1.0)
