import unittest
import sys
import random
import os
sys.path.insert(0, '../../src')
import my_utils


class TestMyUtils(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_file.csv'
        f = open(self.test_file, 'w')
        f.write('Andorra,1990,14.5,0.05,205\n')
        f.write('Brazil,2001,0.0,0.0,926.3\n')
        f.write('Brazil,2006,14500,115.2,20006.2\n')
        f.write('Brazil,2012,1333,58.3,1.6\n')
        f.close()

    def tearDown(self):
        os.remove(self.test_file)

    def test_get_column_default_res(self):
        r = my_utils.get_column(self.test_file, 0, 'Andorra')
        self.assertEqual(r, [1990])

    def test_get_column_choose_res(self):
        r = my_utils.get_column(self.test_file, 0, 'Brazil', 4)
        self.assertEqual(r, [926, 20006, 2])

    def test_get_column_query_out_of_range(self):
        self.assertRaises(SystemExit, my_utils.get_column,
                          self.test_file, -7, 'Andorra')

    def test_get_column_result_non_int(self):
        self.assertRaises(SystemExit, my_utils.get_column,
                          self.test_file, 0, 'Andorra', 0)

    def test_get_mean(self):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        r = my_utils.get_mean([a, b])
        self.assertEqual(r, (a + b) / 2)

    def test_get_mean_empty(self):
        self.assertRaises(ZeroDivisionError, my_utils.get_mean, [])

    def test_get_mean_equal(self):
        random.seed(1)
        a = random.randint(0, 100)
        random.seed(1)
        b = random.randint(0, 100)
        r = my_utils.get_mean([a, b])
        self.assertEqual(r, a)

    def test_get_median_odd(self):
        a = random.randint(0, 20)
        b = random.randint(30, 50)
        c = random.randint(70, 90)
        r = my_utils.get_median([a, b, c])
        self.assertEqual(r, b)

    def test_get_median_even(self):
        a = random.randint(0, 20)
        b = random.randint(30, 50)
        c = random.randint(70, 90)
        d = random.randint(100, 120)
        r = my_utils.get_median([d, a, b, c])
        self.assertEqual(r, (b + c) / 2)

    def test_get_median_empty(self):
        self.assertRaises(IndexError, my_utils.get_median, [])

    def test_get_median_chr(self):
        self.assertRaises(TypeError, my_utils.get_median, [1, 2, 'a'])

    def test_get_median_dbl(self):
        a = random.uniform(0, 20)
        b = random.uniform(30, 50)
        c = random.uniform(70, 90)
        r = my_utils.get_median([b, c, a])
        self.assertEqual(r, b)

    def test_get_std_dev_equal(self):
        random.seed(1)
        a = random.randint(0, 100)
        random.seed(1)
        b = random.randint(0, 100)
        random.seed(1)
        c = random.randint(0, 100)
        r = my_utils.get_std_dev([a, b, c])
        self.assertEqual(r, 0)

    def test_get_std_dev_rand(self):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        c = random.randint(0, 100)
        r = my_utils.get_std_dev([a, b, c])
        self.assertNotEqual(r, 0)

    def test_get_std_dev_neg(self):
        a = -random.randint(0, 100)
        b = -random.randint(0, 100)
        c = -random.randint(0, 100)
        r = my_utils.get_std_dev([a, b, c])
        self.assertNotEqual(r, 0)

    def test_get_std_dev_empty(self):
        self.assertRaises(ZeroDivisionError, my_utils.get_std_dev, [])


if __name__ == '__main__':
    unittest.main()
