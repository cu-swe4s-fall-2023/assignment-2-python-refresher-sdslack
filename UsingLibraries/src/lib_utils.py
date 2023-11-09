"""Functions for using libraries to make report

        * det_data - gets data from files

"""
import pandas as pd

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