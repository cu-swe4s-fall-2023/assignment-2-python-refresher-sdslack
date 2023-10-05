#!/bin/bash

set -e  # stop on error
set -u  # raise error if variable is unset
set -o pipefail  # fail if any prior step failed

# Script runs print_fires.py given file name, column to query
# (int), value to query, and optional result column (int).

# Set parameters
file_name="data/Agrofood_co2_emission.csv"
query_column=0
query_column_bad=-7
query_value="United States of America"
result_column=4
result_column_non_int=0
result_function="mean"

# Working example with result column
echo "Working example of print_fires.py with result column $result_column:"
python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column \
    --country "$query_value" --fires-column $result_column

# Broken example result column contains non-numerical characters
set +e  # unset exit on error
echo "Broken example of print_fires.py with result column $result_column_non_int that constains non-numerical characters:"
python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column \
    --country "$query_value" --fires-column "$result_column_non_int"

# Broken example with query column out of range (negative)
echo "Broken example of print_fires.py with query column $result_column out of range:"
python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column_bad \
    --country "$query_value"

# Working example that prints mean of result column
echo "Working example of print_fires.py with result function $result_function that summarizes result list:"
python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column \
    --country "$query_value" --fires-column $result_column \
    --summary_function "$result_function"