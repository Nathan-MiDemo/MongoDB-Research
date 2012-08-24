import random
import names

def directory_name():
	'''
	Generates a random directory name, which is an alphanumeric string of
	length 1 to 32, selected from a bell curve
	'''
	return names.generate_name(32)

def directory_generator():
	'''
	Generator for a directory hierarchy. Each time it is iterated, it creates
	a new directory randomly in one of the previously created directories and
	returns it
	'''
	directories = []
	while True:
		if not directories:
			new_dir = '/'
		else:
			new_dir = ''.join((random.choice(directories), directory_name(), '/'))

		directories.append(new_dir)
		yield new_dir