import calendar

month, day, year = map(int, input().split())

day_name = calendar.weekday(year, month, day)

print(calendar.day_name[day_name].upper())