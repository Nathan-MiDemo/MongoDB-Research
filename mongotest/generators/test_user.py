import unittest
import random
import itertools
import os.path as path

import user
import bson
import url
from .. import consistency_checks

class TestUser(unittest.TestCase, consistency_checks.ConsistencyChecker):
    def setUp(self):
        self.maxDiff = None

    def test_user_filename(self):
        for file in itertools.islice(user.user_data_generator(100), 100):
            url_name = path.basename(file['url'])
            self.assertEqual(url_name, file['name'])

    def test_user_OID(self):
        generator1 = user.user_data_generator(100)
        id1 = next(generator1)['accountId']

        for file in itertools.islice(generator1, 10):
            self.assertEqual(id1, file['accountId'])

        generator2 = user.user_data_generator(100)
        id2 = next(generator2)['accountId']

        self.assertNotEqual(id1, id2)

        for file in itertools.islice(generator2, 10):
            self.assertEqual(id2, file['accountId'])

    def test_user_consistency(self):
        bucket = url.generate_bucket()
        self.check_consistency_iterator(user.user_data_generator, bucket=bucket, num_directories=100)

    def test_date_consistency(self):
        self.check_consistency(user.make_dates)