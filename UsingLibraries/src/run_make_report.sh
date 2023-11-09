#!/bin/bash

# This script is used to run make_report.py

python make_report.py \
    --ag-file-name '../../data/Agrofood_co2_emission.csv' \
    --gdp-file-name '../../data/IMF_GDP.csv' \
    --output-path '../docs' \
    --countries 'United States of America,Mexico,Canada,Guatemala,Costa Rica'