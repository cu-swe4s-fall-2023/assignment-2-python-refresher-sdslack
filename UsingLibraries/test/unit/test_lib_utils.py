import unittest
import sys
import random
import os
sys.path.insert(0, '../../src')  # noqa
import lib_utils


class TestLibUtils(unittest.TestCase):
    def setUp(self):
        # Set up test agro file
        self.test_agro_file = 'test_agro_file.csv'
        f = open(self.test_agro_file, 'w')
        f.write('Angola,1990,14.5,0.05,205\n')
        f.write('Brazil,2001,0.0,0.0,926.3\n')
        f.write('Brazil,2006,14500,115.2,20006.2\n')
        f.write('Brazil,2012,1333,58.3,1.6\n')
        f.close()
        # Set up test GDP file
        self.test_gdp_file = 'test_gdp_file.csv'
        f = open(self.test_gdp_file, 'w')
        f.write('Country,1950,1990,2001,2012\n')
        f.write('Angola,...,...,...,...\n')
        f.write('Brazil,...,17,000.35,180,760.00,900,000.99\n')
        f.close()

    def tearDown(self):
        os.remove(self.test_agro_file)
        os.remove(self.test_gdp_file)

    def test_get_data(self):
        agro_df, gdp_df = lib_utils.get_data(test_agro_file.csv, test_gdp_file.csv)
        self.assertEqual(agro_df.shape, (4, 5))
        self.assertEqual(gdp_df.shape, (4, 5))