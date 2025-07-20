import datetime

def solve():
    """
    Solves the Project Euler Problem 19.

    Question:
    You are given the following information:
    - 1 Jan 1900 was a Monday.
    - Thirty days has September, April, June and November. All the rest have
      thirty-one, Saving February alone, which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    - A leap year occurs on any year evenly divisible by 4, but not on a
      century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?

    Solution Idea:
    Instead of manually calculating the day of the week and handling all the
    complex rules for leap years, we can use Python's built-in `datetime`
    module, which has this logic implemented correctly.

    The plan is to iterate through every year from 1901 to 2000. For each
    year, we iterate through every month from 1 to 12. We then create a
    `datetime.date` object for the first day of that specific month and year.
    The `date` object has a `weekday()` method that tells us the day of the
    week (where Monday is 0 and Sunday is 6). We simply check if the day is
    a Sunday and increment a counter if it is.
    """
    sunday_count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if datetime.date(year, month, 1).weekday() == 6:
                sunday_count += 1
                
    print(f"The number of Sundays that fell on the first of the month is: {sunday_count}")

solve()