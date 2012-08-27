import datetime
import random

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def random_datetime():
    date_dict = {}

    year = date_dict['year'] = random.randint(2000, 2010)
    month = date_dict['month'] = random.randint(1, 12)
    day = date_dict['day'] = random.randint(1, days_per_month[date_dict['month'] - 1])
    hour = date_dict['hour'] = random.randint(0, 23)
    minute = date_dict['minute'] = random.randint(0, 59)
    second = date_dict['second'] = random.randint(0, 59)

    date = datetime.datetime(year, month, day, hour, minute, second)

    return {'iso': date.isoformat(), 'date': date_dict}

