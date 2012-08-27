import random
import itertools

def random_int_bell_curve(min, max):
    '''
    Generate a random int on a bell curve from min to max
    '''
    #TODO: implement range cutting for a less distinct bell curve

    if min > max:
        raise ValueError("Invalid range for random int generation")
    return sum((random.randint(0, 1) for _ in xrange(max - min))) + min

def print_histogram(items):
    '''
    Takes a list of integers, and prints a histogram of that list, where each
    int is a separate bucket.
    '''
    x = sorted(items)
    bucket = x[0]

    print bucket, ":",
    for item in x:
        while bucket != item:
            bucket += 1
            print '\n', bucket, ":",
        print "*",

def test_bell_curve(min, max, samples):
    '''
    Simple demonstration function to show that random_int_bell_curve does
    generate on a bell curve
    '''
    print_histogram([random_int_bell_curve(min, max) for _ in xrange(samples)])

#Lifted directly from the itertools recipie page
def quantify(iterable, pred=bool):
    '''Count how many times the predicate is true'''
    return sum(itertools.imap(pred, iterable))