import random
import names
from ... import utility

def directory_name():
	'''
	Generates a random directory name, which is an alphanumeric string of
	length 1 to 32, selected from a bell curve
	'''
	return names.generate_name(32)

def directory_generator(max_depth=None, max_subdirectories_per_directory=None, max_total_directories=None):
	'''
	Generator for a directory hierarchy. Each time it is iterated, it creates
	a new directory randomly in one of the previously created directories and
	returns it. max_depth is how deep the directories will go- if 0, they will
	only go in root; if 1, they will only go in root or roots direct
	subdirectories; etc.
	'''

	if max_total_directories is not None:
		if max_total_directories < 0:
			raise ValueError('max_total_directories must be >= 0 or None')
		elif max_total_directories == 0:
			raise StopIteration()

	if max_depth is not None and max_depth < 0:
		raise ValueError('max_depth must be >= 0 or None')

	if max_subdirectories_per_directory is not None and max_subdirectories_per_directory <= 0:
		raise ValueError('max_subdirectories_per_directory must be > 0 or None')

	directories = set('/')
	total_directories = 1

	yield '/'
	
	while True:
		#sadly, random.choice doesn't work on sets.
		containing_directory = random.sample(directories, 1)[0]
		new_dir = join((containing_directory, directory_name(), '/'))

		#2 Notes here. First on the math- the new directory hasn't been
		#added yet, but quantify will count the directory itself as a
		#subdirectory, so it works out. Second is that the >= is only for
		#clarity, and it should only ever trigger on ==.
		if max_subdirectories_per_directory is not None and utility.quantify(directories, lambda string: containing_directory in string) >= max_subdirectories_per_directory:
			directories.remove(containing_directory)

		#Directories is a list of all directories that can have
		#subdirectories. Therefore, only add new directories to it that are
		#below the depth limit
		if max_depth is None or new_dir.count('/') <= max_depth + 1:
			directories.add(new_dir)

		total_directories += 1
		yield new_dir

		if not directories or total_directories == max_total_directories:
			raise StopIteration