#This module contains all functions for generating strings and names

import random
import utility

#todo: make this better
char_set = 'abcdefghigklmnopqrstuvwkyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345679'

def generate_name(length):
	return ''.join(random.sample(char_set, utility.random_int_bell_curve(1, length)))
	