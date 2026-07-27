# Testing Hawaii's Hybrid Broadband Strategy
This project uses geospatial data analytics and Monte Carlo simulation to test the robustness of Hawaii's 82/18 fiber/satellite BEAD deployment strategy, researching how sensitive the split is to changes in construction and satellite service costs.

## Data 
This analysis requires:
1. 2021 TIGER/Line Shapefiles for Hawaii 
2. 5-year ACS housing unit estimates (Table B25001) 
3. Hawaii BEAD Community Anchor Instituion dataset
4. USGS 3DEP elevation data
   
## Environment Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Reproducing this analysis
Run notebooks in this order:
1. 01_notebooks/data_processing.ipynb
2. 02_notebooks/cost_model.ipynb
3. 03_notebooks/analysis.ipynb
   
## Methodology
The model estmates fiber deployment costs using:
-distance to broadband access proxy
-terrain difficulty
-housing density
-deployment method

Resulting costs are compared with satellite deployment costs under Monte Carlo simulation.
