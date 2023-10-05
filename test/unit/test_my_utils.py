import unittest
import sys
sys.path.insert(0, 'src')
import my_utils
import random

class TestMyUtils(unittest.TestCase):
    # def test_get_column(self):

    def test_get_mean(self):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        r = my_utils.get_mean([a, b])
        self.assertEqual(r, (a + b) / 2)
    
    def test_get_mean_empty(self):
        self.assertRaises(SystemExit, my_utils.get_mean, [])
    
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

    # def test_get_std_dev(self):



if __name__ == '__main__':
    unittest.main()