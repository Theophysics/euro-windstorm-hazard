from scipy.stats import genextreme

from windstorm.gev import fit_gev, return_level


def test_return_level_recovers_known_distribution():
    true = genextreme(c=0.0, loc=30.0, scale=4.0)  # Gumbel
    sample = true.rvs(size=5000, random_state=42)
    params = fit_gev(sample)
    expected = true.ppf(1 - 1 / 50)
    assert abs(return_level(params, 50) - expected) < 1.0
