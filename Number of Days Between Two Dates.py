# Number of Days Between Two Dates
# Write a program to count the number of days between two dates.

# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))
        return abs(int((datetime.datetime(y1, m1, d1) - datetime.datetime(y2, m2, d2)).days))
