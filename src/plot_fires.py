"""Plots for values from file from fires query

        * get_args - gets command line arguments.
        * run_plot_hist - runs plot_hist from plot_utils.

"""

import plot_utils as plot_utils
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
        description=('Makes plot of values from file from query.'),
        prog='plot_fires'
    )
    parser.add_argument('--file-name',
                        type=str,
                        required=True,
                        help='Name of file with query results')
    parser.add_argument('--title',
                        type=str,
                        required=True,
                        help='Title to use for plot')
    parser.add_argument('--x-label',
                        type=str,
                        required=True,
                        help='Label for x-axis')
    parser.add_argument('--y-label',
                        type=str,
                        required=True,
                        help='Label for y-axis')
    args = parser.parse_args()
    return args

def run_plot_hist(args):
    """Runs plot_hist from plot_utils.

    Parameters
    ----------
    args : argparse.Namespace
        Arguments from command line

    """
    try:
        f = open(args.file_name, 'r')
    except FileNotFoundError:
        print("File not found: " + args.file_name)
        sys.exit(1)
    except PermissionError:
        print("Could not open: " + args.file_name)
        sys.exit(1)
    plot_utils.plot_hist(args.file_name, args.x_label, args.y_label, args.title)


if __name__ == '__main__':
    """Runs run_plot_hist and writes out plot.

    """
    args = get_args()
    run_plot_hist(args)