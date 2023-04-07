from datetime import datetime

data_hour = '2023-3-19 8:32:20'
data_format = '%Y-%m-%d %H:%M:%S'

date = datetime.strptime(date_hour, data_format)
print(date)
