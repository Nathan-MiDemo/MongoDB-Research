import unittest
import re
import itertools
import os.path as path

import directories

class TestDirectories(unittest.TestCase):
    def setUp(self):
        pass

    def test_random_names(self):
        '''
        Test the directories.generate_name function. Checks that the length is
        correct, and that all the characters come from the alphanumeric characters
        set.
        '''

        #Note that it is IMPOSSIBLE to determine with certainty that the
        #generate_name function is perfoming perfectly. Instead, we repeat the
        #sanity checks 1000 times, giving a .1% chance of a false positive
        for _ in xrange(1000):
            name = directories.directory_name()
            #length is beteen 1 and 32
            self.assertLessEqual(len(name), 32)
            self.assertGreaterEqual(len(name), 1)
            self.assertIsNot(re.match('[a-zA-Z0-9]+', name), None)

    def test_random_heirarchies_basic(self):
        '''
        Test the directories.directory_generator generator. Checks that the
        heirarchy makes sense- that is, every directory has an enclosing
        directory as well.
        '''
        #create directories. For each one, confirm that the parent directory exists
        dir_generator = directories.directory_generator()

        #get 1000 sample directories
        sample_directories = [dir for dir in itertools.islice(directories.directory_generator(), 1000)]

        self.assertIs(sample_directories[0], '/')

        for dir in sample_directories[1:]:
            containing_dir, _ = path.split(dir)
            self.assertIn(containing_dir, sample_directories)

    #Like with some of the others, there's no way to assure that this test gives a false positive
    def test_max_depth(self):
        generator = directories.directory_generator(max_depth=3)

        for dir in itertools.islice(generator, 1000):
            self.assertLessEqual(dir.count('/'), 3)

        generator = directories.directory_generator(max_depth=0)

        #this should only iterate once
        for i, dir in enumerate(itertools.islice(generator, 3)):
            self.assertEqual(dir, '/')
            self.assertEqual(i, 0)

    def test_max_subdirectories(self):
        generator = directories.directory_generator(max_subdirectories_per_directory=5)
        num_subdirectories = {'/': 0}

        for dir in itertools.islice(generator, 1, 1000):
            containing_dir, _ = path.split(dir)
            num_subdirectories[dir] = 0
            num_subdirectories[containing_dir] += 1

        for num in num_subdirectories.itervalues():
            self.assertLessEqual(num, 5)

    def test_depth_and_subdirectories(self):
        generator = directories.directory_generator(max_subdirectories_per_directory=3, max_depth=3)

        #assumes that the individual max tests work. Having both maxes should
        #cap the number of subdirectories

        all_dirs = list(itertools.islice(generator, 50))

        self.assertEqual(len(all_dirs), 40)

    def test_invalid_max_depth(self):
        with self.assertRaises(ValueError):
            generator = directories.directory_generator(max_depth=-5)
            next(generator)

    def test_invalid_max_subdirectories(self):
        with self.assertRaises(ValueError):
            generator = directories.directory_generator(max_subdirectories_per_directory=-5)
            next(generator)