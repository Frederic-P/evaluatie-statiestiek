# Project: evalutation statistics (cars dataset and production forecasts)

Downloadable from: [GitHub](https://github.com/Frederic-P/evaluatie-statiestiek)

## Overview of key files/folders:
There's a sample dataset included in root/data/raw_data/sample, which can be used to better understand the required data structure. The sample size is too small to use, add the full data as described in the data-section.
```
root
|___data
|   |___raw_data
|       |__full
|           |__data_productie
|           |__daily_production
|           |   |__BRU
            |       - *all your json files for BRU production*
|           |   |__STO
            |       - *all your json files for STO production*
|           |   -master_data.json
|           -cars.csv
|___documentation
|       -assignment.pdf
|___notebooks
|       -autoproductie.ipynb
|       -production_forecast.ipynb
|__config
|       -config_cars.json
|       -config_production.json
|__utils
|       -cars.py
|       -config.py
|       -plotstyle.py
|       -preflight.py
|       -production.py
|       -stats.py
-.gitignore
-.environment.yaml
-.readme.md
```

- Asignment solutions can be found as notebooks in the notebooks folder. The names represent the section of the asginment that's handled in there. 
- There is one configuration file per notebook available. The name of the config.json file represents which sectin of the asignment it is relevant for. The configuration files can be found in the config dir. 
- utils: The utils folder contains all the helper functions we use, organized per theme. 
    - cars = functions I don't envision to use in other projects and are specific for targetting questions in the cars-related section of the asignment.
    - config = functions to read the configuration files into the notebook; can be reused in other projects later on.
    - plotstyle = function that loads a custom style for matplotlib; can be reused in other projects later on.
    - preflight = perform some preflight checks on a pandas dataframe; can be reused in other projects later on.
    - production.py functions I don't envision to use in other projects and are specific for targetting question sin de production-related section of the asignment.
    - stats.py functions to perform basic statistical operations; can be reused in other projects later on.

- documentation holds the asignment task
- data folder is where you load your data as described in the next section.

## Data: 
The GitHub Repo does not contain data. The full dataset should be loaded into the correct folders before running the notebooks. 

### Cars dataset: 
Data on the used cars should be loaded in ROOT/data/raw_data/full and should be stored as cars.csv. It should match the structure which is provided as a sample in ROOT/data/raw_data/sample/cars.csv

### Production dataset= 
Production related data should be deployed in data/rawdata/full/data_productie.
- The JSON data for the MSR should be stored there as master_data.json
- The individual JSON files representing production per day, per factory should be loaded in a subfolder /daily_production/*factorycode*. E.G. the data for the BRU facility should be stored in: /data/rawdata/full/data_productie/daily_production/BRU
    - every new facility has its own subfolder in daily_production.
- A sample is provided in /data/rawdata/sample/data_productie with the full msr-file and 5 sample files per facility. 


## Installation: 
1) Download the GitHub repository, or clone it as you would with every other GitHub project.
2) Install and activate the virtual environment (environment.yaml). For this you'll need to have [Anaconda](https://docs.anaconda.com/free/navigator/index.html) installed.
- Open an Anaconda PowerShell prompt and use `cd` to navigate to the directory where you cloned this repository to. The commands below assume you are in the root-directory of the codebase. To install the environment use: `conda env create -f environment.yaml` Wait for the installation process to complete. You'll know if the process is complete when the Anaconda PowerShell shows you the commands to activate and deactivate the newly installed environemnt.
3) Deploy the data files you have in the folders as described in the **Data** section.
- once installed type: `conda activate env_evalutatie_statistiek` to activate this environment; you need to use this Kernel for all modules to work. 
- once activated open the notebook using the `jupyter notebook` command and open the notebooks you are interested in in the browserwindow that pops up. 
4) Run the notebook
5) Play with all the cells