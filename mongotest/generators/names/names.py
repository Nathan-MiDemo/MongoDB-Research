import random
from ... import utility

#todo: make this better
char_set = 'abcdefghigklmnopqrstuvwkyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345679'

def generate_name(length):
    '''
    generates a random alphanumeric string with length 1 to length, along a
    bell curve
    '''
    return ''.join(random.sample(char_set, utility.random_int_bell_curve(1, length)))
    