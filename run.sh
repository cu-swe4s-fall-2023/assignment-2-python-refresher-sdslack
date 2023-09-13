#!/bin/bash

set -e  # stop on error
set -u  # raise error if variable is unset
set -o pipefail  # fail if any prior step failed

if [ "$#" -ne 3 ] && [ "$#" -ne 4 ]
then
    echo "Usage: run.sh <file_name> <query_column> <query_value>"
    echo "[optional result_column]"
    echo "Script runs print_fires.py given file name, column to query"
    echo "(int), value to query, and optional result column (int)."
    exit
fi

file_name=$1
query_column=$2
query_value=$3

echo $3
echo $query_value

if [ "$#" -eq 4 ]
then
    result_column=$4
    echo "Running print_fires.py with result column $result_column"
    python3 print_fires.py "$file_name" "$query_column" "$query_value" "$result_column"
else
    echo "Running print_fires.py with default result column"
    python3 print_fires.py $file_name $query_column "$query_value"
fi
