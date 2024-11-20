res1 = "результат операции: 42"
res2 = "результат операции: 514"
res3 = "результат работы программы: 9"
res4 = 'результат: 2'


def func(value):
    return int(value[value.index(':') + 1:]) + 10


print(func(res1))
print(func(res2))
print(func(res3))
print(func(res4))
