import unittest
import random

import random_checks

class TestRandomChecks(unittest.TestCase):
    def setUp(self):
        class SampleTester(unittest.TestCase, random_checks.RandomDataTester):
            def runTest(self):
                pass

        self.tester = SampleTester()

    def test_check_consistency(self):
        def basic_rand(generator):
            return generator.random()

        self.tester.check_consistency(basic_rand)

    def test_check_consistency_iterator(self):
        def basic_rand_iter(generator):
            while True:
                yield generator.random()

        self.tester.check_consistency_iterator(basic_rand_iter)

    def test_check_consistency_arguments(self):
        def basic_rand_args(min, max, generator):
            return generator.randint(min, max)

        self.tester.check_consistency(basic_rand_args, 2, 12)

    def test_check_consistency_iterator_arguments(self):
        def basic_rand_iterator_args(min, max, generator):
            while True:
                yield generator.randint(min, max)

        self.tester.check_consistency_iterator(basic_rand_iterator_args, 8, 14)

    def test_bad_iterator_allsame(self):
        def basic_bad_iterator(generator):
            while True:
                yield 5

        with self.assertRaises(AssertionError):
            self.tester.check_consistency_iterator(basic_bad_iterator)

    def test_bad_iterator_seed_failure(self):
        def basic_bad_iterator(generator):
            while True:
                yield random.random()

        with self.assertRaises(AssertionError):
            self.tester.check_consistency_iterator(basic_bad_iterator)

    def test_bad_iterator_same_sequence(self):
        def basic_bad_iterator(generator):
            i = 0
            while True:
                i += 1
                yield i

        with self.assertRaises(AssertionError):
            self.tester.check_consistency_iterator(basic_bad_iterator)