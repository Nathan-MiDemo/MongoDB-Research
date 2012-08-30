import unittest

import utility
import consistency_checks
#Sadly, only basic sanity tests are possible here
#TODO: do some statistical analysis. With 1000 values, it SHOULD be within some reasonable % of the mean
class TestBellCurve(unittest.TestCase, consistency_checks.ConsistencyChecker):
    def test_basic_range(self):
        for _ in xrange(1000):
            x = utility.random_int_bell_curve(30, 100)
            self.assertLessEqual(x, 100)
            self.assertGreaterEqual(x, 30)

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            x = utility.random_int_bell_curve(100, 30)

    def test_consistency(self):
        self.check_consistency(utility.random_int_bell_curve, 0, 100)

class TestQuantify(unittest.TestCase):
    def test_quantify(self):
        def sample_predicate(string):
            return "hello!" in string

        sample_list = ["hello world!", "hello! world!", "hello!", "goodbye", "HELLO!"]
        self.assertEqual(utility.quantify(sample_list, sample_predicate), 2)

    def test_quantify_lambda(self):
        sample_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        self.assertEqual(utility.quantify(sample_list, lambda x: x == 3), 2)