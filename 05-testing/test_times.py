import datetime
from times import time_range, overlap_time

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = overlap_time(large, short)

    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_class_time():
    obs1 = time_range("2019-10-31 10:00:00", "2019-10-31 13:00:00")
    obs2 = time_range("2019-10-31 10:05:00", "2019-10-31 12:55:00", 3, 600)
    result = overlap_time(obs1, obs2)

    assert result == obs2

def test_multiple_time():
    obs1 = time_range("2019-10-31 00:00:00", "2019-10-31 23:50:00", 24, 10 * 60)
    obs2 = time_range("2019-10-31 00:30:00", "2019-10-31 23:55:00", 24, 35 * 60)

    result = overlap_time(obs1, obs2)

    for tr1, tr2 in result:
        tr1_s = datetime.datetime.strptime(tr1, "%Y-%m-%d %H:%M:%S")
        tr2_s = datetime.datetime.strptime(tr2, "%Y-%m-%d %H:%M:%S")
        interval_length = (tr2_s - tr1_s).total_seconds()
        # print(interval_length)
        assert interval_length == 20 * 60


# Testing Ideas
# -------------
# Intervals
# - One inside other
# - Left overlap
# - Right overlap
# - Touching
# - No overlap
# 
# You could capture all cases that ensure overlap by checking that at least one of the limits of one of
# the ranges is between the limits of the other range
# 
# The break length (sum of break lengths) isn't larger than one of the time ranges (or the overlap)

if __name__ == "__main__":
    test_multiple_time()