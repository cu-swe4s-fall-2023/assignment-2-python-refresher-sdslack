#!/bin/bash

set -e  # stop on error
set -u  # raise error if variable is unset
set -o pipefail  # fail if any prior step failed

# Script runs print_fires.py given file name, column to query
# (int), value to query, and optional result column (int).

# Set parameters
file_name="data/Agrofood_co2_emission.csv"
file_name_bad="data/Agrofoooood_co2_emission.csv"
query_column=0
query_value="United States of America"
result_column=4
result_column_bad=1000

# Working example of running print_fires.py with result column
echo "Running print_fires.py with result column $result_column"
python3 print_fires.py \
    --file-name "$file_name" --country-column $query_column \
    --country "$query_value" --fires-column $result_column

# Working example of running print_fires.py with default result column
echo "Running print_fires.py with default result column"
python3 print_fires.py \
    --file-name "$file_name" --country-column $query_column \
    --country "$query_value"

# Broken example of running print_fires.py, with result column out
# of file index
set +e  # unset exit on error
python3 print_fires.py \
    --file-name "$file_name" --country-column $query_column \
    --country "$query_value" --fires-column $result_column_bad

# Broken example of running print_fires.py, with bad file name
python3 print_fires.py \
    --file-name "$file_name_bad" --country-column $query_column \
    --country "$query_value"