'''
Base class for testing data from random generators.
'''

import unittest
import random
import itertools

class RandomDataTester:
    def check_consistency(self, func, *args):
        def gen(generator):
            while(True):
                yield func(*args, generator=generator)

        self.check_consistency_iterator(gen)

    def check_consistency_iterator(self, func, *args):
        rand1 = random.Random(5678)
        rand2 = random.Random(5678)

        gen1 = func(*args, generator=rand1)
        gen2 = func(*args, generator=rand2)

        #values from the same seeds are the same
        for result1, result2 in itertools.islice(itertools.izip(gen1, gen2), 10):
            self.assertEqual(result1, result2)

        #subsequent values from the same seed are different
        self.assertNotEqual(next(gen1), next(gen1))

        #values from different seeds are different
        rand1 = random.Random(5678)
        rand2 = random.Random(1234)
        
        gen1 = func(*args, generator=rand1)
        gen2 = func(*args, generator=rand2)

        #values from different seeds are different
        for result1, result2 in itertools.islice(itertools.izip(gen1, gen2), 10):
            self.assertNotEqual(result1, result2)
