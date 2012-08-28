import random
import itertools
from math import floor, ceil

def random_int_bell_curve(min, max, lean=.5, clamp_min=None, clamp_max=None):
    '''
    Generate a random int on a binary distributon with p=lean. The number will
    be in the range min to max, unless clamps are given, in which case it will
    be between clamp_min and clamp_max.
    '''

    if min >= max:
        raise ValueError("Invalid min-max range for random int generation")

    if clamp_min is None:
        clamp_min = min
    if clamp_max is None:
        clamp_max = max

    if clamp_min >= clamp_max:
        raise ValueError("Invalid clamp range")

    def run_test():
        return 1 if random.random() < lean else 0

    while True:
        candidate = sum((run_test() for _ in xrange(max-min))) + min
        if candidate >= clamp_min or candidate <= clamp_max:
            return candidate

def print_histogram(items, scale):
    '''
    Takes a list of integers, and prints a histogram of that list, where each
    int is a separate bucket.
    '''
    x = sorted(random.sample(items, int(ceil(len(items) * scale))))
    bucket = x[0]

    print bucket, "\t:",
    for item in x:
        while bucket != item:
            bucket += 1
            print '\n', bucket, "\t:",
        print "*",

def test_bell_curve(samples, scale, min, max, lean, clampmin, clampmax):
    '''
    Simple demonstration function to show that random_int_bell_curve does
    generate on a bell curve
    '''
    print_histogram([random_int_bell_curve(min, max, lean, clampmin, clampmax) for _ in xrange(samples)], scale)

#Lifted directly from the itertools recipie page
def quantify(iterable, pred=bool):
    '''Count how many times the predicate is true'''
    return sum(itertools.imap(pred, iterable))