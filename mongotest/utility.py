import random

def random_int_bell_curve(min, max):
	return sum((random.randint(0, 1) for _ in xrange(max - min))) + min

def print_histogram(items):
    x = sorted(items)
    bucket = x[0]

    print bucket, ":",
    for item in x:
        while bucket != item:
            bucket += 1
            print '\n', bucket, ":",
        print "*",

#utility function to show that random_int_bell_curve does generate on a bell curve
def test_bell_curve(max, samples):
	print_histogram([random_int_bell_curve(max) for _ in xrange(samples)])