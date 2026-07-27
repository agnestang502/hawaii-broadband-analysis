"""
Downloads:
- Census TIGER/Line shapefiles
- ACS housing data
- Hawaii BEAD CAI data
- USGS 3DEP elevation tiles
"""
from pathlib import Path
import requests
import csv

folders = [
    "data/raw/census",
    "data/raw/acs_data",
    "data/raw/cai",
    "data/raw/elevation"
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

#2021 TIGER/Line Shapefiles for Hawaii
def download_census():
    url="https://www2.census.gov/geo/tiger/TIGER2021/BG/tl_2021_15_bg.zip"
    response = requests.get(url)
    open("data/raw/census/tl_2021_15_bg.zip","wb").write(response.content)
    print("Census data downloaded")

#5-year ACS housing unit estimates (Table B25001) for Hawaii
def download_acs():
    url = "https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b25001.dat"
    response = requests.get(url)
    open("data/raw/acs_data/housing.dat", "wb").write(response.content)
    print("Housing data downloaded")
    
#USGS 3DEP Elevation data
def download_dem():
    tiles = [
        "n20w156",
        "n22w157",
        "n22w158",
        "n22w159"
    ]

    base_url = "https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/TIFF/{tile}/USGS_13_{tile}.tif"

    for tile in tiles:
        url = base_url.format(tile=tile)

        response = requests.get(url, stream=True)

        with open(f"data/raw/elevation/USGS_13_{tile}.tif", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"{tile} downloaded")
    print("Elevation data downloaded")

#Community Anchor Institions (CAI) facility list
def download_cai():
    url = "https://www.hawaii.edu/broadband/wp-content/uploads/sites/40/2026/01/fp_cai_approved.xlsx"
    response = requests.get(url)
    open("data/raw/cai/cai_approved.xlsx","wb").write(response.content)
    print("CAI data downloaded")

def main():
    download_census()
    download_acs()
    download_cai()
    download_dem()
    print("All data downloaded")

if __name__ == "__main__":
    main()
