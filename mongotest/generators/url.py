import names

def generate_bucket():
    return names.generate_name(40)

def generate_url():
    return ''.join(('https://s3.amazonaws.com/', generate_bucket(), '/'))