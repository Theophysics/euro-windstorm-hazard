# European windstorm hazard from ERA5

A miniature windstorm hazard model for Europe: return-period gust maps and a
population-weighted storm loss index, built from ERA5 reanalysis
(extended winters, October to March, 1980 to 2025).

> Work in progress. Sections marked TODO are filled in as the analysis is done.

## Summary

**Status (Nov 2026): in progress.** Done: ERA5 download pipeline, storm footprint maps. Data request from CDS very slow but in progress around 10 hours per year.
Next: winter maxima, GEV return-period maps, storm loss index, as the 1980–2025 ERA5 record downloads.

[Storm Lothar footprint, 26 Dec 1999](figures/Lothar_fg10_1999-12-26.png)

## Data

- ERA5 daily maximum 10 m wind gust, 0.25 degree grid, 35-72N, 15W-30E
  (Copernicus Climate Data Store).
- TODO: population grid used for the loss index.

## Method

1. Storm footprints: maximum gust per grid cell over each named storm.
2. Winter maxima: maximum gust per cell for each October-March season.
3. GEV fit per cell; return levels for 10, 50 and 200 years.
4. Bootstrap uncertainty on the 200-year gust.
5. Storm loss index after Klawa & Ulbrich (2003).

## Results

TODO: four figures from `figures/`, one sentence each.

## Limitations

TODO (ERA5 gust bias, short record for a 200-year estimate, ...).

## How to reproduce

```bash
conda env create -f environment.yml
conda activate windstorm
python scripts/download_era5.py --years 1999     # test with one year first
python scripts/download_era5.py                  # full download
pytest
```

Downloading needs a free Copernicus CDS account with the API key in `~/.cdsapirc`.

## Reference

Klawa, M. and Ulbrich, U. (2003). A model for the estimation of storm losses and
the identification of severe winter storms in Germany. *Nat. Hazards Earth Syst.
Sci.*, 3, 725-732.
