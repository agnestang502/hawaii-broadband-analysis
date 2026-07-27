# Testing Hawaii's Hybrid Broadband Strategy
This project evaluates the robustness of Hawaii's 82/18 fiber/satellite BEAD deployment strategy, researching how sensitive the split is to changes in construction, housing density, and satellite service costs.

## Repository Structure.
```text
.
├── data/
│ ├── raw/
│ └── processed/
├── docs/
├── notebooks/
│ ├── data_processing.ipynb
│ ├── cost_model.ipynb
│ └── analysis.ipynb
├── scripts/
│ └── download_data.py
├── results/
├── requirements.txt
├── LICENSE
└── README.md
```
## Environment Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Data
This analysis requires:
- 2021 TIGER/Line Shapefiles for Hawaii
- 5-year ACS housing unit estimates (Table B25001)
- Hawaii BEAD Community Anchor Institution dataset
- USGS 3DEP elevation data

ACS housing data is included in:
`data/raw/acs_data/housing.csv`
Other raw datasets can be downloaded automatically using:
```bash
python scripts/download_data.py

## Reproducing this analysis
Run notebooks in this order:
1. `notebooks/01_data_processing.ipynb`
2. `notebooks/02_cost_model.ipynb`
3. `notebooks/03_analysis.ipynb`
   
## Methodology
The model estmates fiber deployment costs using:
-distance to broadband access proxy
-terrain difficulty
-housing density
-deployment method

Resulting costs are compared with satellite deployment costs under Monte Carlo simulation.
