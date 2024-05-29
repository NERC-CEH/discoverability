# EIDC Data Scraping
This folder contains scripts for gathering data from the EIDC data catalogue.

## get_catalogue_metadata.py
This script retrieves the top level metadata for the catalogue. To run:
```shell
./get_catalogue_metadata.py
```
this will download and save the catalogue metadata to `catalogue_metadata.json` The url and output file are defined in `config.yml`. 