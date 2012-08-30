import random
import string
from .. import utility

#todo: make this better
#char_set = 'abcdefghigklmnopqrstuvwkyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345679'

#fixed: better! MUCH better
char_set = string.letters + string.digits

def generate_name(length, generator=random):
    '''
    generates a random alphanumeric string with length 1 to length, along a
    bell curve
    '''
    length = utility.random_int_bell_curve(1, length, generator=generator)
    return ''.join(utility.sample_wr(char_set, length, generator=generator))
    