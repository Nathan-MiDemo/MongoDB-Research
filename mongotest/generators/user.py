import itertools
import random
import bson

import directories
import files
import dates
import url

def make_dates(generator=random):
    '''
    Returns 2 date/time dicts. There is a 50% chance they will be the same;
    otherwise, the first date will always be before the second
    '''
    if generator.randint(0, 1):
        date1 = dates.random_datetime()
        date2 = dates.random_datetime()

        if date1["iso"] > date2["iso"]:
            date1, date2 = date2, date1
    else:
        date1 = date2 = dates.random_datetime()

    return date1, date2

def user_data_generator(num_directories, bucket=None, max_depth=None, max_subdirectories=None, id=None, generator=random):
    '''
    Generator for MongoDB data. Generates dicts ready to be inserted into
    MongoDB for a single user. Iterates infinitly.
    '''
    dirs = list(itertools.islice(directories.directory_generator(max_depth, max_subdirectories), num_directories))
    id = bson.ObjectId() if id is None else id
    bucket_url = url.generate_url(bucket)

    while True:
        composition = {}
        composition["accountId"] = id
        composition["path"] = generator.choice(dirs)
        file_name, composition["contentType"] = files.file()
        composition["name"] = file_name
        composition["dateTimeCreated"], composition["dateTimeModified"] = make_dates()
        composition["size"] = generator.randint(1000, 10000000000) #1KB to 10GB
        composition["url"] = ''.join((bucket_url, file_name))

        yield composition
