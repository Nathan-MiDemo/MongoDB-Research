import random
import os.path as path

import names
from ... import utility

def directory_name():
	'''
	Generates a random directory name, which is an alphanumeric string of
	length 1 to 32, selected from a bell curve
	'''
	return names.generate_name(32)

def directory_generator(max_depth=None, max_subdirectories_per_directory=None):
	'''
	Generator for a directory hierarchy. Each time it is iterated, it creates
	a new directory randomly in one of the previously created directories and
	returns it. max_depth is how deep the directories will go- if 0, only the
	root will exist; if 1; 1 level of subdirectory in root; etc
	'''

	if max_depth is not None and max_depth < 0:
		raise ValueError('max_depth must be >= 0 or None')

	if max_subdirectories_per_directory is not None and max_subdirectories_per_directory <= 0:
		raise ValueError('max_subdirectories_per_directory must be > 0 or None')

	yield '/'

	if max_depth is not None and max_depth == 0:
		return #this stops iteration

	directories = set('/')
	if max_subdirectories_per_directory is not None:
		num_subdirectories_table = {'/': 0}
	
	while directories:
		#sadly, random.choice doesn't work on sets.
		containing_dir = random.sample(directories, 1)[0]
		new_dir = path.join(containing_directory, directory_name())

		if max_subdirectories_per_directory is not None:
			num_subdirectories_table[new_dir] = 0
			num_subdirectories_table[containing_dir] += 1
			if num_subdirectories_table[containing_dir] >= max_subdirectories_per_directory:
				directories.remove(containing_dir)

		#Directories is a list of all directories that can have
		#subdirectories. Therefore, only add new directories to it that are
		#below the depth limit
		if max_depth is None or new_dir.count('/') < max_depth:
			directories.add(new_dir)

		yield new_dir