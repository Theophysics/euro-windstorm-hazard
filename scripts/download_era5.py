"""Download ERA5 daily-maximum 10 m wind gust for European extended winters.

One NetCDF file per calendar year is written to data/raw/. Years already
downloaded are skipped, so the script can be stopped and restarted.

Before the first run:
  1. Create a Copernicus CDS account and accept the ERA5 licence on the
     dataset page.
  2. Put your API key in ~/.cdsapirc.
  3. Build the same request in the dataset's web form and compare its
     "Show API request" snippet with REQUEST below. The CDS catalogue is
     occasionally reorganised, so check the keys and values still match.

Usage:
    python scripts/download_era5.py --years 1999      # one year, as a test
    python scripts/download_era5.py                   # everything
"""

import argparse
from pathlib import Path

import cdsapi

DATASET = "derived-era5-single-levels-daily-statistics"
VARIABLE = "10m_wind_gust_since_previous_post_processing"
AREA = [72, -15, 35, 30]  # north, west, south, east
FIRST_YEAR, LAST_YEAR = 1979, 2025  # Oct 1979 - Mar 2025 = winters 1980-2025
OUT_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"


def months_for(year: int) -> list[str]:
    """Extended-winter months needed from this calendar year."""
    months = [1, 2, 3, 10, 11, 12]
    if year == FIRST_YEAR:
        months = [10, 11, 12]
    if year == LAST_YEAR:
        months = [1, 2, 3]
    return [f"{m:02d}" for m in months]


def download_year(client: cdsapi.Client, year: int) -> None:
    target = OUT_DIR / f"era5_fg10_dailymax_{year}.nc"
    if target.exists():
        print(f"{year}: already downloaded, skipping")
        return
    request = {
        "product_type": "reanalysis",
        "variable": [VARIABLE],
        "year": str(year),
        "month": months_for(year),
        "day": [f"{d:02d}" for d in range(1, 32)],
        "daily_statistic": "daily_maximum",
        "time_zone": "utc+00:00",
        "frequency": "1_hourly",
        "area": AREA,
    }
    print(f"{year}: requesting")
    client.retrieve(DATASET, request, str(target))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--years", type=int, nargs="+",
                        help="calendar years to download (default: all)")
    args = parser.parse_args()
    years = args.years or range(FIRST_YEAR, LAST_YEAR + 1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    client = cdsapi.Client()
    for year in years:
        download_year(client, year)


if __name__ == "__main__":
    main()
