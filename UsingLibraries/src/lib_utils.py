"""Functions for using libraries to make report

        * det_data - gets data from files

"""
import pandas as pd

def get_data(agro_file, gdp_file):
    """Gets data from files
    
    Parameters
    ----------
    agro_file: str
        Name of the agriculture file to read
    gdp_file: str
        Name of the GDP file to read

    Returns
    -------
    
    """
    agro_df = pd.read_csv(agro_file)
    gdp_df = pd.read_csv(gdp_file)
    return agro_df, gdp_df