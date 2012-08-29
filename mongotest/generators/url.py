import names
import random

def generate_bucket(generator=random):
    return names.generate_name(40, generator=generator)

def generate_url(bucket=None, generator=random):
    return ''.join(('https://s3.amazonaws.com/', generate_bucket(generator=generator) if bucket is None else bucket, '/'))