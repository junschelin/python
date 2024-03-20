import datetime
from datetime import datetime as dt

today = dt.strptime('2024-03-15', '%Y-%m-%d')

print(today, type(today), type('2024-03-15'))

#D-day 만들기

print(today + datetime.timedelta(days=42))