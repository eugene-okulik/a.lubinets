def repeat_me(count):
    def decorator_repeat(func):
        def wrapper(*args):
            for _ in range(count):
                func(*args)
        return wrapper
    return decorator_repeat


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')


def func_decorator(func):
    def wrapper(text, count):
        for _ in range(count):
            func(text)
    return wrapper


@func_decorator
def example(text):
    print(text)


example('print me again', count=2)
