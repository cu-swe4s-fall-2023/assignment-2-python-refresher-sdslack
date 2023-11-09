"""Functions for using libraries to make report

        * det_data - gets data from files

"""
import pandas as pd
import matplotlib.pyplot as plt

def get_data(file_path):
    """Gets data from files
    
    Parameters
    ----------
    file_path: str
        Name of the file to read

    Returns
    -------
    df: pandas.DataFrame
        Dataframe of the file

    """
    df = pd.read_csv(file_path)
    return df

def get_country_data(df, country, country_col_name):
    """Gets data for multiple countries
    
    Parameters
    ----------
    df: pandas.DataFrame
        Dataframe of the file
    country: list
        List of countries to get data for
    country_col_name: str
        Name of the column with the country names

    Returns
    -------
    country_df: pandas.DataFrame
        Dataframe with only information from those countries

    """
    country_df = df[df[country_col_name].isin(country)]
    return country_df

def line_plot(country_df, country, country_col_name,
               x_col_name, y_col_name, output_file):
    """Makes a line plot of the data

    Parameters
    ----------
    country_df: pandas.DataFrame
        Dataframe with information from selected country/countries
    country: str, or list of str
        Name of the country/countries to plot
    country_col_name: str
        Name of the column with the country names
    x_col: str
        Name of the column with the x data
    y_col: str
        Name of the column with the y data
    output_file: str
        Name of the file to save the plot to

    """
    fig, ax = plt.subplots()
    # Add to plot for each country in list
    for name in country:
        name_df = country_df[country_df[country_col_name] == name]
        ax.plot(name_df[x_col_name],name_df[y_col_name],label=name)
        ax.set_xlabel(x_col_name)
        ax.set_ylabel(y_col_name)
        ax.set_title(y_col_name + ' versus ' + x_col_name)
        ax.legend(loc='lower right')
    plt.savefig(output_file, bbox_inches='tight')