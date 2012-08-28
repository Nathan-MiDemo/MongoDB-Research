import names

def generate_bucket():
    return names.generate_name(40)

def generate_url(bucket=None):
    return ''.join(('https://s3.amazonaws.com/', generate_bucket() if bucket is None else bucket, '/'))