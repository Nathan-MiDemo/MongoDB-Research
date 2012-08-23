import unittest
import index_generator

class TestIndexGenerator(unittest.TestCase):
	def setUp(self):
		self.test_object = index_generator.IndexGenerator()

	def test_random_mime_generation(self):
		full_type, extension = self.test_object.random_mime_type()
		type, subtype = full_type

		print "Got full type: ", full_type
		print "Got extension: ", extension

		self.assertIn(type, self.test_object.mime_types.keys())
		self.assertIn(subtype, self.test_object.mime_types[type].keys())
		self.assertIs(extension, self.test_object.mime_types[type][subtype])

	def test_random_mime_generation_with_supertype(self):
		test_type = 'audio'
		full_type, extension = self.test_object.random_mime_type(test_type)
		type, subtype = full_type

		print "Got full type: ", full_type
		print "Got extension: ", extension

		self.assertIs(test_type, type)
		self.assertIn(subtype, self.test_object.mime_types[test_type].keys())
		self.assertIs(extension, self.test_object.mime_types[test_type][subtype])

if __name__ == '__main__':
	unittest.main()