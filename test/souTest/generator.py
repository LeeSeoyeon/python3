from random import normalvariate, random
from itertools import count

def read_fake_data(filename):
    for i in count():
        sigma = random() * 10
        yield (i, normalvariate(0, sigma))

from datetime import date
from itertools import groupby

def day_grouper(iterable):
    key = lambda timestamp, value : date.fromtimestamp(timestamp)
    return groupby(iterable, key)

import math

def check_anomaly(day, day_data):
    n, mean, M2 = 0
    max_value = None

    for timestamp, value in day_data:
        n += 1
        delta = value - mean
        mean = mean + delta/n
        M2 += delta*(value - mean)
        if max_value:
            max_value = max(max_value, value)
        else:
            max_value = value

    variance = M2/(n -1)
    standard_deviation = math.sqrt(variance)

    if max_value > mean + 3 * standard_deviation:
        return day
    return False

data = read_fake_data("data_filename")
data_day = day_grouper(data)
anomalous_dates = filter(None, map(check_anomaly, data_day))

first_anomalous_date, first_anomalous_data = anomalous_dates.next()
print("The first anomalus date is ", first_anomalous_date)