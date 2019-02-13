"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
`calendar.py month [year]`
and does the following:
- If the user doesn't specify any input, your program should 
print the calendar for the current month. The 'datetime'
module may be helpful for this.
- If the user specifies one argument, assume they passed in a
month and render the calendar for that month of the current year.
- If the user specifies two arguments, assume they passed in
both the month and the year. Render the calendar for that 
month and year.
- Otherwise, print a usage statement to the terminal indicating
the format that your program expects arguments to be given.
Then exit the program.
"""

import sys
import calendar
from datetime import datetime


def get_month(m=datetime.today().month, y=datetime.today().year):
    print(calendar.month(y, m))


if len(sys.argv) < 2:
    get_month()
elif len(sys.argv) == 2:
    if int(sys.argv[1]) > 0 and int(sys.argv[1]) < 13:
        get_month(int(sys.argv[1]))
    else:
        print('\n----------\nPlease enter a valid month (integer from 1-12).\n----------\n')
elif len(sys.argv) == 3:
    if int(sys.argv[1]) > 0 and int(sys.argv[1]) < 13:
        get_month(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print('\n----------\nPlease enter a valid month (integer from 1-12).\n----------\n')
else:
    print(
        '\n----------\nPlease enter a month and a year in the following format where both arguments are integers: cal.py [Month] [Year]\n[Year] can be omitted to get a month in the current year.\nBoth can be omitted to get the current month of the current year.\n----------\n')
