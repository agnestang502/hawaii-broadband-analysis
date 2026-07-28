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
    
#USGS 3DEP Elevation data
def download_dem():
    dem_urls = {
    "n20w156": "https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/TIFF/historical/n20w156/USGS_13_n20w156_20250611.tif",
    "n22w157": "https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/TIFF/historical/n22w157/USGS_13_n22w157_20250611.tif",
    "n22w158": "https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/TIFF/historical/n22w158/USGS_13_n22w158_20250611.tif",
    "n22w159": "https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/TIFF/historical/n22w159/USGS_13_n22w159_20250611.tif",
}
    for tile, url in dem_urls.items():
        print(f"downloading {tile}...")
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
    download_cai()
    download_dem()
    print("All data downloaded")

if __name__ == "__main__":
    main()