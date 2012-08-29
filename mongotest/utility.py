import random
import itertools
from math import floor, ceil

def random_int_bell_curve(min, max, lean=.5, narrow=10, generator=random):
    '''
    Generate a random int on a beta distribution, with a mean of lean, scaled
    to min and max. The parameters are tuned such that alpha=lean*narrow,
    beta=(1-lean)*narrow. Therefore, the larger narrow is, the narrower the
    graph will be.
    '''

    if min >= max:
        raise ValueError("Invalid min-max range for random int generation")

    if not 0 <= lean <= 1:
        raise ValueError("lean must be between 0 and 1")

    alpha = lean * narrow
    beta = (1 - lean) * narrow

    return int(generator.betavariate(alpha, beta) * (max - min)) + min



def print_histogram(items, scale, clamp_left=None, clamp_right=None):
    '''
    Takes a list of integers, and prints a histogram of that list, where each
    int is a separate bucket.
    '''
    counts = {}
    def count(x):
        if x in counts:
            counts[x] += scale
        else:
            counts[x] = scale

    map(count, items)

    if clamp_left is None:
        clamp_left = min(counts.iterkeys())

    if clamp_right is None:
        clamp_right = max(counts.iterkeys())

    for bucket in xrange(clamp_left, clamp_right + 1):
        print bucket, '\t:',
        if bucket in counts:
            for _ in xrange(int(floor(counts[bucket]))):
                print '*',
        print '\n',


def test_bell_curve(samples, scale, min, max, lean):
    '''
    Simple demonstration function to show that random_int_bell_curve does
    generate on a bell curve
    '''
    print_histogram((random_int_bell_curve(min, max, lean) for _ in xrange(samples)), scale, min, max)

#Lifted directly from the itertools recipie page
def quantify(iterable, pred=bool):
    '''Count how many times the predicate is true'''
    return sum(itertools.imap(pred, iterable))