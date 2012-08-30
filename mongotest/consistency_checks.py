'''
Base class for testing data from random generators.
'''

import unittest
import random
import itertools
import copy

class ConsistencyChecker:
    def check_consistency(self, func, *args, **kwargs):
        def gen(generator):
            copied_kwargs = copy.copy(kwargs)
            copied_kwargs['generator'] = generator
            while(True):
                yield func(*args, **copied_kwargs)

        self.check_consistency_iterator(gen)

    def check_consistency_iterator(self, func, *args, **kwargs):
        rand1 = random.Random(5678)
        rand2 = random.Random(5678)

        kwargs['generator'] = rand1
        gen1 = func(*args, **kwargs)

        kwargs['generator'] = rand2
        gen2 = func(*args, **kwargs)

        #values from the same seeds are the same
        for result1, result2 in itertools.islice(itertools.izip(gen1, gen2), 10):
            self.assertEqual(result1, result2)

        #subsequent values from the same seed are different
        self.assertNotEqual(next(gen1), next(gen1))

        #values from different seeds are different
        rand1 = random.Random(5678)
        rand2 = random.Random(1234)
        
        kwargs['generator'] = rand1
        gen1 = func(*args, **kwargs)

        kwargs['generator'] = rand2
        gen2 = func(*args, **kwargs)

        #values from different seeds are different. Assert that at least half are different
        num_same = 0
        for result1, result2 in itertools.islice(itertools.izip(gen1, gen2), 10):
            try:
                self.assertNotEqual(result1, result2)
            except AssertionError:
                num_same += 1
                if num_same > 5:
                    raise

            
