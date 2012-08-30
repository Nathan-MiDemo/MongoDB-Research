import unittest
import re
import random

import names

class TestNames(unittest.TestCase):
    def test_name_generation(self):
        name = names.generate_name(30)

        self.assertGreaterEqual(len(name), 1)
        self.assertLessEqual(len(name), 30)
        self.assertIsNot(re.match("[a-zA-Z0-9]*", name), None)

    def test_bad_name_generation(self):
        with self.assertRaises(ValueError):
            name = names.generate_name(0)

        with self.assertRaises(ValueError):
            name = names.generate_name(-1)
