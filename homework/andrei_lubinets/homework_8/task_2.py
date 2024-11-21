def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


count = 0
for num in fibonacci():
    if count == 10:
        print(num)
    elif count == 200:
        print(num)
    elif count == 1000:
        print(num)
    elif count == 100000:
        print(num)
        break
    count += 1
