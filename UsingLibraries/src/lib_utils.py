"""Functions for using libraries to make report

        * det_data - gets data from a file
        * get_country_data - gets data for one or more countries
        * line_plot - makes a line plot of the data
        * scatter_plot - makes a scatter plot of the data
        * merge_data - merges two dataframes
        * destroy_commas - removes commas from a string

"""
import pandas as pd
import matplotlib.pyplot as plt


def get_data(file_path):
    """Gets data from given file

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
              x_col_name, y_col_name, output_file, ax=None):
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

    Returns
    -------
    ax: matplotlib.axes._subplots.AxesSubplot
        Axes of the plot

    """
    ax = ax or plt.gca()
    # Add to plot for each country in list
    for name in country:
        name_df = country_df[country_df[country_col_name] == name]
        ax.plot(name_df[x_col_name], name_df[y_col_name], label=name)
        ax.set_xlabel(x_col_name)
        ax.set_ylabel(y_col_name)
        ax.set_title(y_col_name + ' versus ' + x_col_name)
        ax.legend(loc='lower right')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)


def scatter_plot(country_df, country, country_col_name,
                 x_col_name, y_col_name, output_file, ax=None):
    """Makes a scatter plot of the data

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
    ax = ax or plt.gca()
    # Add to plot for each country in list
    for name in country:
        name_df = country_df[country_df[country_col_name] == name]
        ax.scatter(name_df[x_col_name], name_df[y_col_name], label=name)
        ax.set_xlabel(x_col_name)
        ax.set_ylabel(y_col_name)
        ax.set_title(y_col_name + ' versus ' + x_col_name)
        ax.legend(loc='lower right')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)


def merge_data(agro_df, gdp_df):
    """Merges dataframes, specifically GDP into AG data

    Parameters
    ----------
    agro_df: pandas.DataFrame
        Dataframe with AG data

    gdp_df: pandas.DataFrame
        Dataframe with GDP data

    Returns
    -------
    agro_gdp_df: pandas.DataFrame
        Dataframe with AG data and GDP data
    """
    # Melt GDP data so can merge
    gdp_df_melt = pd.melt(gdp_df, id_vars=['Country'],
                          var_name='Year', value_name='GDP')

    # Update types after melt, replace ... & - values, remove commas
    gdp_df_melt = gdp_df_melt.replace('...', None)
    gdp_df_melt = gdp_df_melt.replace('-', None)
    gdp_df_melt['Year'] = gdp_df_melt['Year'].astype('int64')
    gdp_df_melt['Country'] = gdp_df_melt['Country'].astype('str')
    for col in gdp_df_melt.columns:
        if col == 'GDP':
            gdp_df_melt[col] = gdp_df_melt[col].apply(destroy_commas)
    gdp_df_melt['GDP'] = gdp_df_melt['GDP'].astype('float64')

    # Merge into agro data
    agro_gdp_df = pd.merge(agro_df, gdp_df_melt, how='inner',
                           left_on=['Year', 'Area'],
                           right_on=['Year', 'Country'])
    return agro_gdp_df


def destroy_commas(x):
    """Replces commas with nothing

    Parameters
    ----------
    x: str
        String to remove commas from

    Returns
    -------
    float
        String with commas removed
    """
    if x is None:
        return None
    return float(x.replace(',', ''))
