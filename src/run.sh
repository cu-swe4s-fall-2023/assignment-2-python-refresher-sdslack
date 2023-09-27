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
query_column_bad=-7
query_column_char="a"
query_value="United States of America"
result_column=3
result_column_bad=1000
result_column_non_int=0

# Working example with result column
echo "Running print_fires.py with result column $result_column"
python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column \
    --country "$query_value" --fires-column $result_column

# Working example with default result column
echo "Running print_fires.py with default result column"
python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column \
    --country "$query_value"

# Broken example with result column out of range
set +e  # unset exit on error
python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column \
    --country "$query_value" --fires-column $result_column_bad

# Broken example with bad file name
python3 src/print_fires.py \
    --file-name "$file_name_bad" --country-column $query_column \
    --country "$query_value"

# Broken example result column contains non-numerical characters
python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column \
    --country "$query_value" --fires-column "$result_column_non_int"

# Broken example with query column out of range (negative)
python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column_bad \
    --country "$query_value"

# Broken example with non-integer country column
python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column_char \
    --country "$query_value"