"""Queries and prints column specificed by user input

        * get_args - gets command line arguments.
        * run_get_column - runs get_column from my_utils.
        * main - runs run_get_column and prints results.

"""

import my_utils as utils
import argparse
import sys


def get_args():
    """Get command line arguments.

    Returns
    -------
    args : argparse.Namespace
        Arguments from command line

    """
    parser = argparse.ArgumentParser(
        description=('Print results queired from the input file for the '
                     'given country. Default prints fires column.'),
        prog='print_fires'
    )
    parser.add_argument('--file-name',
                        type=str,
                        required=True,
                        help='Name of the file to read')
    parser.add_argument('--country-column',
                        type=int,
                        required=True,
                        help='Column number of the country')
    parser.add_argument('--country',
                        type=str,
                        required=True,
                        help='Country to search')
    parser.add_argument('--fires-column',
                        type=int,
                        required=False,
                        help='Column number to query from the file')
    args = parser.parse_args()
    return args


def run_get_column(args):
    """Runs get_column from my_utils.

    Parameters
    ----------
    args : argparse.Namespace
        Arguments from command line

    Returns
    -------
    fires : list of int
        List of integers from the fires column

    """
    try:
        f = open(args.file_name, 'r')
    except FileNotFoundError:
        print("File not found: " + args.file_name)
        sys.exit(1)
    except PermissionError:
        print("Could not open: " + args.file_name)
        sys.exit(1)
    if args.fires_column is not None:
        fires = utils.get_column(args.file_name,
                                 args.country_column,
                                 args.country,
                                 result_column=args.fires_column)
    else:
        fires = utils.get_column(args.file_name,
                                 args.country_column,
                                 args.country)
    return fires


if __name__ == '__main__':
    """
    Runs run_get_column and prints results.
    
    """
    args = get_args()
    print(run_get_column(args))
