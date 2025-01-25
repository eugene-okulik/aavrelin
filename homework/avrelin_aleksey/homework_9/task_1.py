import datetime


my_date = "Jan 15, 2023 - 12:05:33"
python_format = datetime.datetime.strptime(my_date,'%b %d, %Y - %H:%M:%S')
print(python_format.strftime('%B'))
print(python_format.strftime('%d.%m.%Y, %H:%M'))
