"""Functions for querying files

    * get_column - returns the requested or default column as integers
    from the input file with the given query column and query value.
    * get_mean - returns the mean of a list of integers.
    * get_median - returns the median of a list of integers.
    * get_std_dev - returns the standard deviation of a list of integers.

"""

import sys
import math


def get_column(file_name, query_column, query_value, result_column=1):
    """Queries and returns the requested column or default (column 1)
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

    """

    result = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.rstrip().split(',')
            try:
                line[query_column]
            except IndexError:
                print("Query column out of range.")
                sys.exit(1)
            try:
                line[result_column]
            except IndexError:
                print("Result column out of range.")
                sys.exit(1)
            if line[query_column] == query_value:
                result.append(line[result_column])
    try:
        result = [float(val) for val in result]
    except ValueError:
        print("Could not convert result to float, so can't convert to int.")
        sys.exit(1)
    result_int = [int(round(float(val))) for val in result]
    return result_int

def get_mean(int_list):
    """Returns the mean of a list of integers.

    Parameters
    ----------
    int_list : list of int
        List of integers

    Returns
    -------
    mean : float
        Mean of the list of integers

    """
    mean = sum(int_list) / len(int_list)
    return mean

def get_median(int_list):
    """Returns the median of a list of integers.

    Parameters
    ----------
    int_list : list of int
        List of integers

    Returns
    -------
    median : float
        Median of the list of integers

    """
    int_list.sort()
    if len(int_list) % 2 == 0:
        median = (int_list[len(int_list) // 2] +
                  int_list[len(int_list) // 2 - 1]) / 2
    else:
        median = int_list[len(int_list) // 2]
    return median

def get_std_dev(int_list):
    """Returns the standard deviation of a list of integers.

    Parameters
    ----------
    int_list : list of int
        List of integers

    Returns
    -------
    std_dev : float
        Standard deviation of the list of integers

    """
    mean = get_mean(int_list)
    devs_sq = [(val - mean) ** 2 for val in int_list]
    devs_sq_mean = get_mean(devs_sq)
    std_dev = math.sqrt(devs_sq_mean)
    return std_dev