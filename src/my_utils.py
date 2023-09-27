"""Functions for querying files

    * get_column - returns the requested or default column as integers
    from the input file with the given query column and query value.

"""

import sys


def get_column(file_name, query_column, query_value, result_column=1):
    """Queries and returns the requested column or default (column 2)
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
