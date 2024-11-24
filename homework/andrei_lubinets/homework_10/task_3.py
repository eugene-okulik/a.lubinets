def decorator_replace(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(second, first, '-')
        elif second > first:
            return func(first, second, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')
    return wrapper


@decorator_replace
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


first, second, operation = (int(input("Enter first number: ")),
                            int(input("Enter second number: ")),
                            input("enter type of operation :"))

print(f"Result {calc(first, second)}")
