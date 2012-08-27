import re
import unittest
import files

class TestMimeGeneration(unittest.TestCase):
    def check_valid_mime_type(self, mime_type, extension):
        type, subtype = mime_type

        self.assertIn(type, files.mime_types)
        self.assertIn(subtype, files.mime_types[type])
        self.assertEqual(extension, files.mime_types[type][subtype])

    def test_mime_types(self):
        mime_type, extension = files.random_mime_type()

        self.check_valid_mime_type(mime_type, extension)

    def test_mime_type_fixed_type(self):
        mime_type, extension = files.random_mime_type("audio")
        type, _ = mime_type
        
        self.assertEqual(type, "audio")
        self.check_valid_mime_type(mime_type, extension)

    def test_mime_type_fixed_subtype(self):
        mime_type, extension = files.random_mime_type("audio", "mpeg")
        type, subtype = mime_type

        self.assertEqual(type, "audio")
        self.assertEqual(subtype, "mpeg")
        self.assertEqual(extension, "mp3")
        self.check_valid_mime_type(mime_type, extension)

    def test_mime_type_mismatch(self):
        with self.assertRaises(KeyError):
            mime_type, extension = files.random_mime_type("audio", "jpeg")

    def test_mime_type_nonexistent(self):
        with self.assertRaises(KeyError):
            mime_type, extension = files.random_mime_type("foo")


class TestFiles(unittest.TestCase):
    def test_file_name(self):
        for _ in xrange(1000):
            name = files.file_name()

            self.assertLessEqual(len(name), 64)
            self.assertGreaterEqual(len(name), 1)
            self.assertIsInstance(re.match("[a-zA-Z0-9]*", name), re.MatchObject)

    def test_full_file(self):
        file, mime_type = files.file()
        file_type = file[file.rfind('.') + 1:]
        type, subtype = mime_type.split('/')

        self.assertEqual(file_type, files.mime_types[type][subtype])