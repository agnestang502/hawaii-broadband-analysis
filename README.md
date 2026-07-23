# Testing Hawaii's Hybrid Broadband Strategy

This project uses geospatial data analytics and Monte Carlo simulation to test the cost-efficiency and robustness of Hawaii's 82/18 fiber/satellite BEAD deployment strategy, researching how sensitive the split is to changes in construction and satellite service costs.

## Data Setup

Download the following source files before running `notebooks/data_processing.ipynb`:

1. **Census Block Group Shapefiles**: 2021 TIGER/Line Shapefiles for Hawaii (`tl_2021_15_bg.zip`) 
   from the [US Census Bureau](https://catalog.data.gov/dataset/tiger-line-shapefile-2021-state-hawaii-block-groups). 
   Extract into `data/raw/census data/`.

2. **ACS Housing Data**: 5-year ACS housing unit estimates (Table B25001) for Hawaii from 
   [data.census.gov](https://data.census.gov/table/ACSDT5Y2024.B25001?q=B25001:+Housing+Units). 
   Save as `data/raw/acs_data/housing.csv`.

3. **Community Anchor Institions (CAI)**: Approved CAI facility list from the 
   [Hawaii BEAD Final Proposal](https://www.hawaii.edu/broadband/final-proposal/). 
   Save as `data/raw/cai_approved.xlsx`.

4. **Elevation Data (USGS 3DEP, 1/3 arc-second)**: Download the following DEM tiles from 
   [The National Map downloader](https://apps.nationalmap.gov/downloader/#/):
   - n20w1562023
   - n22w157
   - n22w158
   - n22w159
   
   Place all `.tif` files directly into `data/raw/`.
   
   **Note:** these files are large (~300MB each). Browser downloads can silently truncate; 
   using `wget -c <url>` (resume-capable) is recommended over a browser tab.

## Environment Setup

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
