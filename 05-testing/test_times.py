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
    test_given_input()