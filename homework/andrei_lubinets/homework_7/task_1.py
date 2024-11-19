number = 7

while True:
    if int(input("Введите цифру, проверьте вашу интуицию:\n")) != number:
        print("попробуйте снова")
        continue
    else:
        print("Поздравляю! Вы угадали!")
        break
