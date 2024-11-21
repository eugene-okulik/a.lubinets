import datetime


date = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(date, '%b %d, %Y - %H:%M:%S')
print(python_date.strftime("%B"))

changed_python_date = python_date.strftime('%d.%m.%Y, %H:%M')
print(changed_python_date)
