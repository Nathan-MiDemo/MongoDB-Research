import directories
import files
import dates
import url

import itertools
import random
from bson.json_util import ObjectID

def make_dates():
    '''
    Returns 2 date/time dicts. There is a 50% chance they will be the same;
    otherwise, the first date will always be before the second
    '''
    if random.randint(0, 1):
        date1 = dates.random_datetime()
        date2 = dates.random_datetime()

        if date1["iso"] > date2["iso"]:
            date1, date2 = date2, date1
    else:
        date1 = date2 = dates.random_datetime()

    return date1, date2

def user_data_generator(bucket, num_directories, max_depth=None, max_subdirectories=None):
    dirs = list(itertools.islice(directories.directory_generator(max_depth, max_subdirectories), num_directories))
    id = ObjectID()
    bucket_url = url.generate_url(bucket)
    for _ in xrange(num_files):
        composition = {}
        composition["accountId"] = id
        composition["path"] = random.choice(dirs)
        file_name, composition["contentType"] = files.file()
        composition["name"] = file_name
        composition["dateTimeCreated"], composition["dateTimeModified"] = make_dates()
        composition["size"] = random.randint(1000, 10000000000) #1KB to 10GB
        composition["url"] = ''.join((bucket_url, file_name))

        yield composition

