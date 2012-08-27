import datetime

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def random_datetime():
    date = datetime.datetime.now()
    date_dict = {}

    date_dict['year'] = date.year = random.randint(2000, 2010)
    date_dict['month'] = date.month = random.randint(1, 12)
    date_dict['day'] = date.day = random.randint(1, days_per_month[date.month - 1])
    date_dict['hour'] = date.hour = random.randint(0, 23)
    date_dict['minute'] = date.minute = random.randint(0, 59)
    date_dict['second'] = date.second = random.randint(0, 59)

    return {'iso': date.isoformat(), 'date': date_dict}

