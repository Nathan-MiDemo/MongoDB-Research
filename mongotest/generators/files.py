import random
import names

mime_types = {
		"image":
		{
			"gif": "gif",
			"jpeg": "jpg",
			"png": "png",
			"tiff": "tiff"
		},
		"audio":
		{
			"mp4": "mp4",
			"mpeg": "mp3",
			"ogg": "ogg",
			"vnd.wave": "wav"
		},
		"video":
		{
			"mpeg": "mpg",
			"mp4": "mp4",
			"quicktime": "mov",
			"x-ms-wmv": "wmv"
		},
		"application":
		{
			"json": "json",
			"pdf": "pdf",
			"javascript": "js",
			"postcript": "ps",
			"zip": "zip",
			"x-gzip": "gz"
		},
		"text":
		{
			"css": "css",
			"csv": "csv",
			"html": "html",
			"plain": "txt",
			"xml": "xml"
		}
	}

def random_mime_type(type=None, subtype=None, generator=random):
	'''
	Returns a tuple of (mime_type, extension). Mime_type is a tuple containing
	(supertype, subtype). If the type parameter is not None, the supertype will
	be type.
	'''

	if type is None:
		type = generator.choice(mime_types.keys())

	if subtype is None:
		subtype = generator.choice(mime_types[type].keys())

	return (type, subtype), mime_types[type][subtype]

def file_name(generator=random):
	'''
	Creates a random file name, which is a random alphanumeric string with a
	random number of characters, between 1 and 64, selected on a bell curve.
	'''
	return names.generate_name(64, generator)

def file(type = None, generator=random):
	'''
	Creates a file object, which is a file name plus extension, and a mime type,
	in a tuple. Both objects are strings.
	'''

	mime_type, extension = random_mime_type(type, generator)

	return '.'.join((file_name(generator), extension)), '/'.join(mime_type)
