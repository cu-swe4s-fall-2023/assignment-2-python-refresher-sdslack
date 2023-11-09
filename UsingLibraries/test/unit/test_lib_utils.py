import unittest
import sys
import random
import os
sys.path.insert(0, '../../src')  # noqa
import lib_utils


class TestLibUtils(unittest.TestCase):

    def test_get_data(self):
        # Using small test files instead of making new to preserve
        # the formatting in target files
        agro_df = lib_utils.get_data('../data/test_Agrofood_co2_emission.csv')
        gdp_df = lib_utils.get_data('../data/test_IMF_GDP.csv')
        self.assertEqual(agro_df.shape, (26, 31))
        self.assertEqual(gdp_df.shape, (3, 40))

    def test_get_country_data_agro(self):
        agro_df = lib_utils.get_data('../data/test_Agrofood_co2_emission.csv')
        country = 'Brazil'
        country_col_name = 'Area'
        country_df = lib_utils.get_country_data(agro_df, country, country_col_name)
        self.assertEqual(country_df.shape, (7, 31))

    def test_get_country_data_gdp(self):
        gdp_df = lib_utils.get_data('../data/test_IMF_GDP.csv')
        country = 'Brazil'
        country_col_name = 'Country'
        country_df = lib_utils.get_country_data(gdp_df, country, country_col_name)
        self.assertEqual(country_df.shape, (1, 40))

    def test_line_plot(self):
        agro_df = lib_utils.get_data('../data/test_Agrofood_co2_emission.csv')
        country = 'Brazil'
        country_col_name = 'Area'
        country_df = lib_utils.get_country_data(agro_df, country, country_col_name)
        x_col_name = 'Year'
        y_col_name = 'Average Temperature °C'
        output_file = '../docs/test_line_plot.png'
        lib_utils.line_plot(country_df, country, x_col_name, y_col_name, output_file)
        self.assertTrue(os.path.isfile('../docs/test_line_plot.png'))