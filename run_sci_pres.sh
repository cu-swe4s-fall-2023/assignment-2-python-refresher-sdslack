#!/bin/bash

set -e  # stop on error
set -u  # raise error if variable is unset
set -o pipefail  # fail if any prior step failed

# Script runs print_fires.py given file name, column to query
# (int), value to query, optional result column (int), optional
# summary function (str), and optional file to write results
# out to (str).

# This script was used to generate the small scientific presentation
# described in the README and reproduced by the snakefile in
# workflow/snakefile.

# Set parameters
file_name="data/Agrofood_co2_emission.csv"
query_column=0  # country names
query_values=("China" "India" "United States of America" "Indonesia" "Pakistan")
result_column=29  # total emissions

# First, write out the results of total emissions query for each country
for country in "${query_values[@]}"
do
    python3 src/print_fires.py \
        --file-name "$file_name" --country-column $query_column \
        --country "$country" --fires-column $result_column \
        --write-file data/"$country"_total_emissions.txt
done

# Next, use results files to plot histograms of total emissions
for country in "${query_values[@]}"
do
    python src/plot_fires.py --file-name data/"$country"_total_emissions.txt \
        --output-path sci_pres/ --title "$country" --x-label "Total Emissions" \
        --y-label "Count"
done