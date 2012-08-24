import unittest
import directories
from names import char_set

class TestDirectories(unittest.TestCase):
    def test_random_names(self):
        for _ in xrange(20):
            name = directories.generate_name()
            self.assertLessEqual(len(name), 32)
            self.assertGreaterEqueal(len(name), 1)
            for char in name:
                self.assertIn(char, char_set)

    def test_random_heirarchies(self):
        #create directories. For each one, confirm that the parent directory exists
        dir_generator = directories.directory_generator()

        #get 30 sample directories
        sample_directories = [dir for dir, _ in directories.directory_generator, xrange(30)]

        self.assertIs(sample_directories[0], '/')

        for dir in sample_directories[1:]:
            separator = dir.rfind(/, 0, -1)
            containing_dir = dir[:separator]
            self.assertIn(containing_dir, sample_directories)