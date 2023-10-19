## **Overview**

This project enables querying of a file containing statistics about
fires for various countries and years. The user can query the input
file to retrieve information from the default result column for a
chosen country, or the user can choose which result column they
would like to retrieve information from.

The project source code is written in Python3 but is designed to be
run using bash from the command line. An example bash script is
included in the project repository.

## **Installation**

### Dependencies

Python3 and bash are required to run the code in this project.

The example bash script run.sh should be executed from the top level of
the repository.

Unit tests (located at test/unit), functional tests (test/func), and style
tests for python (PEP8, tested using pycodestyle), are executed when
any branch is pushed to the GitHub-hosted repository as well as when a pull
request is made on the main branch on GitHub. 

The style tests set up mamba environment "csci6118" using its environment
file at test/etc/csci6118_env.yml in order to use the pycodestyle program.
The functional tests use the Stupid Simple Bash Testing Framework, which
is automatically downloaded when the tests are executed on GitHub.

### Step by Step Installation Instructions

1. Clone this repository to your local machine:

```bash
git clone git@github.com:cu-swe4s-fall-2023/assignment-2-python-refresher-sdslack.git
```

2. Navigate to the directory containing the cloned repository:

```bash
cd assignment-2-python-refresher-sdslack
```

3. View the contents of the repository:
```bash
ls
```
```
README.md       run.sh      src/
```
This document is the README.md, run.sh is a bash script that runs
examples (discussed in detail below), and src/ contains the source
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

The bash script run.sh includes four examples of how to use the source
code. The script can be run with the following code:

```bash
bash run.sh
```

This will run four examples:

1. A working example with a user-defined result column to query.

```bash
file_name="data/Agrofood_co2_emission.csv"
query_column=0
query_value="United States of America"
result_column=4

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

3. A broken example returning the default result column but where the
    user-requested query column is out of range of the input file.

```bash
file_name="data/Agrofood_co2_emission.csv"
query_column_bad=-7
query_value="United States of America"

python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column_bad \
    --country "$query_value"
```

4. A working example that prints mean of the user-defined result column
to query.

```bash
file_name="data/Agrofood_co2_emission.csv"
query_column=0
query_value="United States of America"
result_column=4
result_function="mean"

python3 src/print_fires.py \
    --file-name "$file_name" --country-column $query_column \
    --country "$query_value" --fires-column $result_column \
    --summary_function "$result_function"

```

### Script and Function Details

The example bash script runs print_fires.py. The usage of print_fires.py can be
seen by running the following code:

```python
python src/print_fires.py --help
```
```python
usage: print_fires [-h] --file-name FILE_NAME --country-column COUNTRY_COLUMN
                    --country COUNTRY [--fires-column FIRES_COLUMN]
                   [--summary_function SUMMARY_FUNCTION]

Print results queired from the input file for the given country. Default prints fires column
and does not summarize the results (prints integer list of all results).

options:
  -h, --help            show this help message and exit
  --file-name FILE_NAME
                        Name of the file to read
  --country-column COUNTRY_COLUMN
                        Column number of the country
  --country COUNTRY     Country to search
  --fires-column FIRES_COLUMN
                        Column number to query from the file
  --summary_function SUMMARY_FUNCTION
                        Function to summarize results, use "mean", "median", or "std_dev"
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
+ summary_function (optional) - the string name of the function to summarize the
    results from the input file. The default is to not summarize and to return
    a list of integers. The options are "mean", "median", and "std_dev".

The script print_fires.py runs the following functions:

+ get_args - gets command line arguments.
+ run_get_column - runs get_column from my_utils, optionally also running summary
    functions from my_utils.
+ main - runs run_get_column and prints results.

The run_get_column function in print_fires.py uses the get_column function from
and summary functions get_mean, get_median, and get_std_dev from my_utils.py.

The docustring for the get_column function can be accessed by running the following
in the Python interpreter:

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
column number with results to return. If the result column is not
specified, the default column (column 1) is returned. Because
get_column converts the data to be returned to integers, it is not
possible to select a result column that is non-numeric.

The docustring for the summary functions can be accessed by running the following
in the Python interpreter, once inside the src/ directory:

```python
import my_utils
my_utils.get_mean.__doc__
```
```python
    Returns the mean of a list of integers.

    Parameters
    ----------
    int_list : list of int
        List of integers

    Returns
    -------
    mean : float
        Mean of the list of integers
```

```python
import my_utils
my_utils.get_median.__doc__
```
```python
    Returns the median of a list of integers.

    Parameters
    ----------
    int_list : list of int
        List of integers

    Returns
    -------
    median : float
        Median of the list of integers
```

```python
import my_utils
my_utils.get_std_dev.__doc__
```
```python
    Returns the standard deviation of a list of integers.

    Parameters
    ----------
    int_list : list of int
        List of integers

    Returns
    -------
    std_dev : float
        Standard deviation of the list of integers
```

## **Small Scientific Presentation**

### Introduction

Using the CO2 emission data in the Agrofood_co2_emission.csv (see above
for download instructions), I compared the distribution of total emissions for
all years included in the data from the top five largest countries by population
as of July 2023 according to the United States Census Bureau:

    1. China
    2. India
    3. United States of America
    4. Indonesia
    5. Pakistan

Reference: https://www.census.gov/popclock/world

### Results

The following figures show the distribution of total emissions for each of
the five countries for all years included in the data file.

China:
![China](sci_pres/China.png)

India:
![India](sci_pres/India.png)

United States of America:
![United States of America](sci_pres/United_States_of_America.png)

Indonesia:
![Indonesia](sci_pres/Indonesia.png)

Pakistan:
![Pakistan](sci_pres/Pakistan.png)

**Conclusions:** China had the highest distribution of yearly-reported total
emissions, although India, Indonesia, and the United States were all on the
same scale of magnitude. Pakistan had a much lower distribution of yearly-reported
total emissions.

**Limitations:** The current work did not include any statistical analysis of the
difference between Pakistan and the other four countries. Additionally, the years
included in the plots were not standardized across all countries and therefore may
have some variation.

### Methods

The results were generated two different ways:

1. Using the bash script run_sci_pres.sh

+ Bash scripting was used to loop over the five countries for each step of analysis
+ The first step of analysis used print_fires.py to query the total emissions for
    each country for each year included in the data file. The results were written
    to a file for each country.
+ The second step of analysis used plot_fires.py to plot the distribution of total
    emissions for each country for all years included in the data file. The plots
    were written to the sci_pres/ directory.

2. Using the snakefile under workflow/snakefile

+ The snakefile was used to run the same analysis for all countries by expanding
  the rule all to include the final PNG file output name for all countries.
+ The first rule make_data_file only ran if the raw CSV data is present. It used
    print_fires.py to query the total emissions for each country for each year
    included in the data file. The results were written to a file for each country.
+ The second rule plot_data_hist only ran if the query files for each country were
    found. It used plot_fires.py to plot the distribution of total emissions for
    each country for all years included in the data file. The plots were written
    to the sci_pres_snake/ directory.
