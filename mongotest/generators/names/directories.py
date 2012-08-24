import random
from . import generate_name

def directory_name():
	'''
	Generates a random directory name, which is an alphanumeric string of
	length 1 to 32, selected from a bell curve
	'''
	return generate_name(32)

def directory_generator():
	'''
	Generator for a directory hierarchy. Each time it is iterated, it creates
	a new directory randomly in one of the previously created directories and
	returns i
	'''
	directories = []

	if not directories:
		x = '/'
	else:
		x = ''.join((random.choice(directories), directory_name(), '/'))

	directories.append(x)
	yield x