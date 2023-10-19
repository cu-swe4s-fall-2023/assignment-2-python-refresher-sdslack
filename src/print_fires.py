"""Queries and prints column specificed by user input

        * get_args - gets command line arguments.
        * run_get_column - runs get_column from my_utils, optionally
        also running summary functions from my_utils.
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
        description=('Default prints fires column and does not summarize'
                     'the results (prints integer list of all results).'),
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
    parser.add_argument('--summary_function',
                        type=str,
                        required=False,
                        help='Function to summarize results, '
                             'use "mean", "median", or "std_dev"')
    parser.add_argument('--write-file',
                        type=str,
                        required=False,
                        help='Option to write results to file')
    args = parser.parse_args()
    return args


def run_get_column(args):
    """Runs get_column from my_utils, optionally also running summary
    functions from my_utils.

    Parameters
    ----------
    args : argparse.Namespace
        Arguments from command line

    Returns
    -------
    fires : list of int
        List of integers from the fires column

    fires_sum : float
        Summarized results from fires column

    """
    try:
        f = open(args.file_name, 'r')
    except FileNotFoundError:
        print("File not found: " + args.file_name)
        sys.exit(1)
    except PermissionError:
        print("Could not open: " + args.file_name)
        sys.exit(1)
    try:
        if args.country_column < 0:
            raise ValueError
    except ValueError:
        print('Country column must be positive.')
        sys.exit(1)
    if args.fires_column is not None:
        try:
            if args.fires_column < 0:
                raise ValueError
        except ValueError:
            print('Fires column must be positive.')
            sys.exit(1)
        fires = utils.get_column(args.file_name,
                                 args.country_column,
                                 args.country,
                                 result_column=args.fires_column)
    else:
        fires = utils.get_column(args.file_name,
                                 args.country_column,
                                 args.country)
    if args.summary_function is None:
        if args.write_file is not None:
            try:
                utils.write_file(fires, args.write_file)
            except PermissionError:
                print("Could not write out file")
                sys.exit(1)
            return fires
        else:
            return fires
    else:
        try:
            if args.summary_function not in ['mean', 'median', 'std_dev']:
                raise ValueError
        except ValueError:
            print('Summary function must be "mean", "median", or "std_dev".')
            sys.exit(1)
        try:
            fires[0]
        except IndexError:
            print("Result list is empty.")
            sys.exit(1)
        if args.summary_function == 'mean':
            fire_sum = utils.get_mean(fires)
        elif args.summary_function == 'median':
            fire_sum = utils.get_median(fires)
        elif args.summary_function == 'std_dev':
            fire_sum = utils.get_std_dev(fires)
        if args.write_file is not None:
            try:
                utils.write_file(fire_sum, args.write_file)
            except PermissionError:
                print("Could not write out file")
                sys.exit(1)
            return fire_sum
        else:
            return fire_sum


if __name__ == '__main__':
    """Runs run_get_column and prints results.

    """
    args = get_args()
    print(run_get_column(args))
