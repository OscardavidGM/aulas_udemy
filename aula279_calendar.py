import calendar
from datetime import date

# print(calendar.calendar(2023))
# print(calendar.month(2023, 3))

primer_dia, ultima_dia = calendar.monthrange(2023, 3)

# print(calendar.day_name[primer_dia])

for week in calendar.monthcalendar(2023, 3):
    for day in week:
        if day == 0:
            continue
        current_day = date(2023, 3, day)
        print(day, current_day.strftime('%A'))
