import random

class IndexGenerator:
	mime_types = {
		"image":
		{
			"gif": ".gif",
			"jpeg": ".jpg",
			"png": ".ping",
			"tiff": ".tiff"
		},
		"audio":
		{
			"mp4": ".mp4",
			"mpeg": ".mp3",
			"ogg": ".ogg",
			"vnd.wave": ".wav"
		},
		"video":
		{
			"mpeg": ".mpg",
			"mp4": ".mp4",
			"quicktime": ".mov",
			"x-ms-wmv": ".wmv"
		},
		"application":
		{
			"json": ".json",
			"pdf": ".pdf",
			"javascript": ".js",
			"postcript": ".ps",
			"zip": ".zip",
			"x-gzip": ".gz"
		},
		"text":
		{
			"css": ".css",
			"csv": ".csv",
			"html": ".html",
			"plain": ".txt",
			"xml": ".xml"
		}
	}

	def __init__(self):
		pass


	def random_mime_type(self, type=''):
		if type is '':
			type = random.choice(self.mime_types.keys())

		subtype = random.choice(self.mime_types[type].keys())

		#returns (complete-mime-type, extension)
		return (type, subtype), self.mime_types[type][subtype]