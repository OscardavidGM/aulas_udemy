from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pytz import timezone

data_hour = '2023-3-19 8:32:20'
data_format = '%Y-%m-%d %H:%M:%S'


date = datetime.strptime(data_hour, data_format)
date2 = datetime.strptime('2020-3-19 8:54:20', data_format)
delta = relativedelta(date, date2)
# print(delta)
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())

times_more = timedelta(days=10)
date2 = date2 + relativedelta(years=2)
delta = relativedelta(date, date2)
print(date2)

#########################

# Aula277

# fecha = datetime.strptime('2021-12-01 10:50:30', '%Y-%m-%d %H:%M:%S')
# print(fecha.strftime('%d/%m/%Y \n %H:%M AM \n'))
