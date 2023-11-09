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
    """Gets data for a specific country
    
    Parameters
    ----------
    df: pandas.DataFrame
        Dataframe of the file
    country: str
        Name of the country to get data for

    Returns
    -------
    country_df: pandas.DataFrame
        Dataframe with only information from that country

    """
    country_df = df[df[country_col_name] == country]
    return country_df

def line_plot(country_df, country,
              x_col_name, y_col_name, output_file):
    """Makes a line plot of the data

    Parameters
    ----------
    country_df: pandas.DataFrame
        Dataframe with only information from that country
    x_col: str
        Name of the column with the x data
    y_col: str
        Name of the column with the y data
    output_file: str
        Name of the file to save the plot to
    
    Returns
    -------
    None

    """
    fig, ax = plt.subplots()
    ax.plot(country_df[x_col_name],country_df[y_col_name],label=country,color='#f80000')
    # ax.plot(can_df['Year'],can_df['Total Population - Male'],label='Male',color='green')
    ax.set_xlabel(x_col_name)
    ax.set_ylabel(y_col_name)
    ax.set_title(y_col_name + ' versus ' + x_col_name)
    ax.legend(loc='lower right')
    plt.savefig(output_file, bbox_inches='tight')