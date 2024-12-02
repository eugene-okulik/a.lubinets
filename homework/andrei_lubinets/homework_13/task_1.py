import datetime
import os

bace_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(bace_path))
file_path = os.path.join(homework_path, "eugene_okulik", "hw_13", "data.txt")
print(file_path)


def read_file():
    with open(file_path, "r") as file:
        for line1 in file.readlines():
            yield line1


for line in read_file():
    if line.startswith("1"):
        date = datetime.datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f')
        delta = datetime.timedelta(weeks=1)
        print(f"Через 1 неделю от {date} будет дата {date + delta}")
    elif line.startswith("2"):
        date = datetime.datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f')
        print(f"В данную дату {date} день недели являлся {date.strftime('%A')}")
    elif line.startswith("3"):
        date = datetime.datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f')
        date_now = datetime.datetime.now()
        print(f"С текущей даты {date} прошло {(date_now - date).days} дня(ей)")
