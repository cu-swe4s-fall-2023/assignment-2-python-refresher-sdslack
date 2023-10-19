import unittest
import sys
import random
import os
sys.path.insert(0, '../../src')  # noqa
import plot_utils


class TestPlotUtils(unittest.TestCase):
    def setUp(self):
        # Single column of ints
        self.test_file = 'test_file.csv'
        f = open(self.test_file, 'w')
        f.write('14\n')
        f.write('0\n')
        f.write('14500\n')
        f.write('58\n')
        f.close()

        self.empty_test_file = 'empty_test_file.csv'
        f = open(self.empty_test_file, 'w')
        f.close()

    def tearDown(self):
        os.remove(self.test_file)
        os.remove(self.empty_test_file)

    def test_plot_hist(self):
        plot_utils.plot_hist(self.test_file, './', 'x', 'y', 'title')
        self.assertTrue(os.path.isfile('test_file_hist.png'))

    def test_plot_hist_missing_param(self):
        self.assertRaises(TypeError, plot_utils.plot_hist,
                          self.test_file, './', 'x', 'y')

    def test_plot_hist_empty_file(self):
        # Empty file should still make plot
        plot_utils.plot_hist(self.empty_test_file, './', 'x', 'y', 'title')
        self.assertTrue(os.path.isfile('empty_test_file_hist.png'))


if __name__ == '__main__':
    unittest.main()
