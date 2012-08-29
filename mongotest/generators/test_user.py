import unittest
import random
import itertools
import os.path as path

import user
import bson

class TestUser(unittest.TestCase):
    def test_user_random_consistency(self):
        id = bson.ObjectId()

        random.seed(2345)
        list1 = list(itertools.islice(user.user_data_generator(100, id=id), 10))

        random.seed(2345)
        list2 = list(itertools.islice(user.user_data_generator(100, id=id), 10))

        for item1, item2 in itertools.izip(list1, list2):
            self.assertEqual(item1, item2)

    def test_user_filename_consistency(self):
        for file in itertools.islice(user.user_data_generator(100), 100):
            url_name = path.basename(file['url'])
            self.assertEqual(url_name, file['name'])

    def test_user_OID_consistency(self):
        generator1 = user.user_data_generator(100)
        id1 = next(generator1)['accountId']

        for file in itertools.islice(generator1, 10):
            self.assertEqual(id1, file['accountId'])

        generator2 = user.user_data_generator(100)
        id2 = next(generator2)['accountId']

        self.assertNotEqual(id1, id2)

        for file in itertools.islice(generator2, 10):
            self.assertEqual(id2, file['accountId'])