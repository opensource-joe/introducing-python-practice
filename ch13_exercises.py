# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch13.html#:-:text=Things%20to%20Do

# 13.1 Write the current date as a string to the text file today.txt.

# from datetime import date, datetime
# today = date.today()
# today_str = today.isoformat()

# with open('today.txt', 'wt') as output:
#     print(today_str, file=output)

# 13.2 Read the text file today.txt into the string today_string.

# with open ('today.txt', 'rt') as input:
#     today_string = input.read()
# print(today_string)

# 13.3 Parse the date from today_string.

# fmt = '%Y-%m-%d\n'
# print(datetime.strptime(today_string, fmt))

# 13.4 Create a date object of your day of birth.

# my_day = date(1975, 2, 25)
# print(my_day)

# 13.5 What day of the week was your day of birth?

# print(my_day.weekday())
# print(my_day.isoweekday())

# 13.6 When will you be (or when were you) 10,000 days old?

# from datetime import timedelta
# party_day = my_day + timedelta(days=10000)
# print(party_day)