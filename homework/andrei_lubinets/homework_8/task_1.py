import random


def get_bonus():
    salary = int(input("Enter salary: "))
    bonus = random.choice([True, False])
    if bonus is True:
        res1 = salary * random.randrange(5, 16)
        print(f"{salary}, {bonus} - '${res1}'")
    else:
        res2 = salary * 1
        print(f"{salary}, {bonus} - '${res2}'")


get_bonus()
get_bonus()
get_bonus()
