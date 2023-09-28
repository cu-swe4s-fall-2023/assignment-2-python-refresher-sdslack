## **Overview**

This project enables querying of a file containing statistics about
fires for various countries and years. The user can query the input
file to retrieve information from the default result column for the
specified country, or the user can choose which result column they
would like to retrieve information from.

The project source code is written in Python3 but is designed to be
run using bash from the command line. An example bash script is
include in the project repository.

## **Installation**

### Dependencies

Python3 and bash are required to run the code in this project.

### Step by Step Installation Instructions

1. Clone this repository to your local machine:

```bash
git clone git@github.com:cu-swe4s-fall-2023/assignment-2-python-refresher-sdslack.git
```

2. Navigate to the directory containing the cloned repository:

```bash
cd assignment-2-python-refresher-sdslack
```

3. View the directories within the repository:
```bash
ls
```
```
README.md       run.sh      src/
```
This document is the README.md, run.sh is a bash script that runs
example (discussed in detail below), and src/ contains the source
code for this project.

4. Download the example data file 'Agrofood_co2_emission.csv' by copying
    and pasting the following link into your browser and manually pressing
    download:

https://drive.google.com/file/d/1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr/view?usp=drive_link

5. Create a data/ directory within the cloned repository, and move the
    downloaded file from your Downloads/ directory to the data/ directory:

```bash
mkdir data
mv ~/Downloads/Agrofood_co2_emission.csv data/
```

6. Finally, run the example bash script:

```bash
bash run.sh
```

## **Usage**

### Examples

The bash script run.sh includes three examples of how to use the source
code. The script can be run with the following code:

```bash
bash run.sh
```

This will run three examples:

1. A working example with a user-defined result column to query.

```bash
file_name="data/Agrofood_co2_emission.csv"
query_column=0
query_column_bad=-7
query_value="United States of America"

python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column \
    --country "$query_value" --fires-column $result_column
```

2. A broken example where the user-requested result column contains
    non-numerical characters.

```bash
file_name="data/Agrofood_co2_emission.csv"
query_column=0
query_value="United States of America"
result_column_non_int=0

python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column \
    --country "$query_value" --fires-column "$result_column_non_int"
```

3. A broken example with the default result column but where the
    user-requested query column is out of range of the input file.

```bash
file_name="data/Agrofood_co2_emission.csv"
query_column_bad=-7
query_value="United States of America"

python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column_bad \
    --country "$query_value"
```

### Script and Function Details

The example bash script runs print_fires.py. The usage of print_fires.py can be
seen by running the following code:

```python
python src/print_fires.py --help
```
```python
usage: print_fires [-h] --file-name FILE_NAME --country-column COUNTRY_COLUMN --country COUNTRY
                   [--fires-column FIRES_COLUMN]

Print results queired from the input file for the given country. Default prints fires column.

options:
  -h, --help            show this help message and exit
  --file-name FILE_NAME
                        Name of the file to read
  --country-column COUNTRY_COLUMN
                        Column number of the country
  --country COUNTRY     Country to search
  --fires-column FIRES_COLUMN
                        Column number to query from the file
```

In more detail, the inputs to print_fires.py are as follows:

+ file-name (required) - the name of the file to read given as a string. This
    file should be comma-delimited with a .csv extension. The file should contain
    a column that contains different country names, and at least one colum with
    different data for each country.
+ country-column (required) - the integer column number that contains different
    country names in the input file. To note: the first column is column 0.
+ country (required) - the string name of the country to query results for from
    the input file. The string name should match a value present in the country
    names column.
+ fires-column (optional) - the integer column number to query results from in
    the input file. The default value is 1. To note: the first column is column 0.

The script print_fires.py runs the following functions:

+ get_args - gets command line arguments.
+ run_get_column - runs get_column from my_utils.
+ main - runs run_get_column and prints results.

The run_get_column function in print_fires.py uses the get_column function from
my_utils.py.

The docustring for the get_column function can be access by running the following:

```python
python src/my_utils.py --help
```

```python
import my_utils
my_utils.get_column.__doc__
```
```python
    Queries and returns the requested column or default (column 1)
    as integers from input file with the given query column and query value.

    Parameters
    ----------
    file_name : str
        Name of the file to read
    query_column : int
        Column number of the query
    query_value : str
        Value to query in query column
    result_column : int (optional, default=1)
        Column number of result to query

    Returns
    -------
    result_int : list of int
        List of integer values from the result column
```

In more detail, the get_column function takes in the file name to
query, the column number to query (the column containing country names)
for the query value (the country name to query), and optionally the
column number with the results to return. If the result column is not
specificed, the default column (column 1) is returned. Because
get_column converts the data to be returned to integers, it is not
possible to select a result column that is non-numeric.