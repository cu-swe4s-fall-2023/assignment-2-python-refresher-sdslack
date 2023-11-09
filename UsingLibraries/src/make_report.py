"""Makes report on AG and GDP data

        * TBD

"""

import lib_utils as lib_utils
import argparse


def get_args():
    """Get command line arguments.

    Returns
    -------
    args : argparse.Namespace
        Arguments from command line

    """
    parser = argparse.ArgumentParser(
        description=('Makes report on AG and GDP data, specifically '
                     'plotting average temp, year versus emissions, '
                     'GDP versus emissions, and population over time.'),
        prog='make_report'
    )
    parser.add_argument('--ag-file-name',
                        type=str,
                        required=True,
                        help='Name of file with AG data')
    parser.add_argument('--gdp-file-name',
                        type=str,
                        required=True,
                        help='Name of file with GDP data')
    parser.add_argument('--output-path',
                        type=str,
                        required=True,
                        help='Path to write output files to')
    parser.add_argument('--countries',
                        type=str,
                        required=True,
                        help='List of countries to plot (comma sep)')
    args = parser.parse_args()
    args.countries = args.countries.split(',')
    return args

def plot_avg_temp(args):
    """
    Plots average temperature over time for selected countries.
    
    Parameters
    ----------
    args : argparse.Namespace
        Arguments from command line

    """
    agro_df = lib_utils.get_data(args.ag_file_name)
    country_col_name = 'Area'
    country_df = lib_utils.get_country_data(agro_df, args.countries, country_col_name)
    x_col_name = 'Year'
    y_col_name = 'Average Temperature °C'
    output_file = args.output_path + '/avg_temp.png'
    lib_utils.line_plot(country_df, args.countries, country_col_name,
                        x_col_name, y_col_name, output_file)
    
def plot_year_vs_emissions(args):
    """
    Plots year versus emissions for selected countries.
    
    Parameters
    ----------
    args : argparse.Namespace
        Arguments from command line

    """
    agro_df = lib_utils.get_data(args.ag_file_name)
    country_col_name = 'Area'
    country_df = lib_utils.get_country_data(agro_df, args.countries, country_col_name)
    x_col_name = 'Year'
    y_col_name = 'total_emission'
    output_file = args.output_path + '/year_vs_emissions.png'
    lib_utils.scatter_plot(country_df, args.countries, country_col_name,
                           x_col_name, y_col_name, output_file)
    
def plot_gdp_vs_emissions(args):
    """
    Plots GDP versus emissions for selected countries.
    
    Parameters
    ----------
    args : argparse.Namespace
        Arguments from command line

    """
    agro_df = lib_utils.get_data(args.ag_file_name)
    gdp_df = lib_utils.get_data(args.gdp_file_name)
    # GDP data has United States instead of United States of America
    gdp_df['Country'] = gdp_df['Country'].replace('United States', 'United States of America')
    agro_gdp_df = lib_utils.merge_data(agro_df, gdp_df)

    country_col_name = 'Area'
    country_df = lib_utils.get_country_data(agro_gdp_df, args.countries, country_col_name)
    x_col_name = 'GDP'
    y_col_name = 'total_emission'
    output_file = args.output_path + '/gdp_vs_emissions.png'
    lib_utils.scatter_plot(country_df, args.countries, country_col_name,
                           x_col_name, y_col_name, output_file)
    
def plot_pop(args):
    """
    Plots population over time for selected countries.
    
    Parameters
    ----------
    args : argparse.Namespace
        Arguments from command line

    """
    agro_df = lib_utils.get_data(args.ag_file_name)
    country_col_name = 'Area'
    country_df = lib_utils.get_country_data(agro_df, args.countries, country_col_name)
    x_col_name = 'Year'
    y_col_name = 'Total Population - Female'
    output_file = args.output_path + '/pop.png'
    lib_utils.line_plot(country_df, args.countries, country_col_name,
                        x_col_name, y_col_name, output_file)
    

if __name__ == '__main__':
    """Makes report on AG and GDP data.

    """
    args = get_args()
    plot_avg_temp(args)
    plot_year_vs_emissions(args)
    plot_gdp_vs_emissions(args)
    plot_pop(args)