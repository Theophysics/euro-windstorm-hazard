"""
Plot storm footprints (max gust per grid cell) for four named European windstorms.
"""

from pathlib import Path

import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

REPO = Path(__file__).resolve().parents[1]
CITIES = {                  # name: (lat, lon)
    "London":  (51.5, -0.1),
    "Paris":   (48.9, 2.35),
    "Hamburg": (53.55, 10.0),
    "Zurich":  (47.4, 8.5),
}
GUST_VMIN, GUST_VMAX = 0, 45
OUT_DIR = REPO / "figures"
CENTRE_LAT = 50

STORMS = {# name: (first day, last day), UTC dates, both included
    "Lothar":  ("1999-12-26", "1999-12-26"),
    "Kyrill":  ("2007-01-18", "2007-01-19"),
    "Xynthia": ("2010-02-27", "2010-02-28"),
    "Eunice":  ("2022-02-18", "2022-02-18"),
}

def plot_storm_footprint(ds, name, start, end, out): # plot the storm footprints
    
    ds = ds.drop_vars("number")
    window = ds.fg10.sel(valid_time=slice(start, end))
    footprint = window.max("valid_time") 
    fig, ax = plt.subplots(figsize=(7.5, 6), dpi=150)
    footprint.plot(
        ax=ax,
        cmap="magma_r",                  # colour map
        vmin=GUST_VMIN, vmax=GUST_VMAX,  # fixed colour range in m/s
        cbar_kwargs={"label": "Daily max 10 m gust (m/s)"},
    )
    if start == end:
        ax.set_title(f"ERA5 max gust for storm {name}, {start}")
    else:
        ax.set_title(f"ERA5 max gust for storm {name}, {start} to {end}")
    ax.set_aspect(1 / np.cos(np.deg2rad(CENTRE_LAT)))

    #Add details:
    label_cities(ax, footprint, CITIES)

    plt.savefig(out, dpi=150)
    plt.close()

def label_cities(ax, field, cities):
    for name, (lat, lon) in cities.items():
        city = field.sel(latitude=lat, longitude=lon, method="nearest")
        value = float(city)
        ax.plot(lon, lat, "o", mfc="none", mec="cyan")    # hollow circle at (lon, lat)
        ax.annotate(f"{name} {value:.1f} m/s",
                xy=(lon, lat),
                xytext=(6, 6), textcoords="offset points",     
                color="cyan",
                arrowprops={"arrowstyle": "-", "color": "cyan"}, # line joining them
                path_effects=[pe.withStroke(linewidth=2, foreground="black")]
        )


def main() -> None:
    for name, (start, end) in STORMS.items():
        year = start.split("-")[0]
        year_end = end.split("-")[0]
        if year != year_end:
            years = [year, year_end]
        else:
            years = [year]
        out = OUT_DIR / f"{name}_fg10_{start}.png"

        OUT_DIR.mkdir(parents=True, exist_ok=True)
        data_files = [REPO / "data" / "raw" / f"era5_fg10_dailymax_{year}.nc" for year in years]
        if not all(f.exists() for f in data_files):
            print(f"{name}: data for {years} not downloaded yet, skipping")
            continue
        ds = xr.open_mfdataset(data_files)
    
        plot_storm_footprint(ds, name, start, end, out)


if __name__ == "__main__":
    main()
