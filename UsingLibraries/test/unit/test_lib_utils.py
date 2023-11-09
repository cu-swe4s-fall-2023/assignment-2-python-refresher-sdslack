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
        agro_df, gdp_df = lib_utils.get_data('../data/test_Agrofood_co2_emission.csv',
                                             '../data/test_IMF_GDP.csv')
        self.assertEqual(agro_df.shape, (26, 31))
        self.assertEqual(gdp_df.shape, (3, 40))