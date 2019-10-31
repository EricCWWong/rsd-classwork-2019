from times import overlap_time, time_range
import datetime

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_class_time():
    large = time_range("2010-01-12 09:05:00", "2010-01-12 13:55:00")
    short = time_range("2010-01-12 10:05:00", "2010-01-12 12:55:00", 3, 600)
    result = overlap_time(large, short)
    expected = short
    assert result == expected

def test_20mins():
    first = time_range("2010-01-12 00:00:00", "2010-01-12 23:50:00", 24, 600)
    second = time_range("2010-01-12 00:30:00", "2010-01-12 23:55:00", 24, 35*60)
    for i in range (len(overlap_time(first, second))):
        t0_s = datetime.datetime.strptime(overlap_time(first, second)[i][0], "%Y-%m-%d %H:%M:%S")
        t1_s = datetime.datetime.strptime(overlap_time(first, second)[i][1], "%Y-%m-%d %H:%M:%S")
        result = (t1_s - t0_s).total_seconds()
        expected = 1200
        assert result == expected

# Testing ideas
#  - times don't overlap
#  - times are identical
#  - wrong time format
#  - Gap longer than the time period
#  - If the time is not divisiable by the number of gaps