import numpy as np

from windstorm.maxima import winter_year


def test_winter_is_named_after_its_january():
    dates = np.array(["1999-10-01", "1999-12-26", "2000-03-31", "2000-10-01"],
                     dtype="datetime64[D]")
    assert list(winter_year(dates)) == [2000, 2000, 2000, 2001]
