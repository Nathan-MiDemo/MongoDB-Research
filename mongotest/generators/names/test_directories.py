import unittest
import re
import itertools

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
        #sanity checks 100 times, giving a 1% chance of a false positive
        for name in (directories.directory_name() for _ in xrange(100)):
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

        #get 30 sample directories
        sample_directories = [dir for dir, _ in zip(directories.directory_generator(), xrange(30))]

        self.assertIs(sample_directories[0], '/')

        for dir in sample_directories[1:]:
            separator = dir.rfind('/', 0, -1)
            containing_dir = dir[:separator + 1]
            self.assertIn(containing_dir, sample_directories)


    #Like with some of the others, there's no way to assure that this test gives a false positive
    def test_max_depth(self):
        generator = directories.directory_generator(max_depth=2)

        for dir in itertools.islice(generator, 100):
            self.assertLessEqual(dir.count('/'), 3)

        generator = directories.directory_generator(max_depth=0)

        #this should only iterate once
        for i, dir in enumerate(itertools.islice(generator, 3):
            self.assertEqual(dir, '/')
            self.assertEqual(i, 0)