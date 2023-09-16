import my_utils as utils
import argparse


def get_args():
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


# TODO: should this be in a function?
# TODO: should I pass args?
def run_get_column():
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
    args = get_args()
    print(run_get_column())
