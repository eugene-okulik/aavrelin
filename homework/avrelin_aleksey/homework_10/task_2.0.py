def repeat_me(func):
    def wrapper(x, count):
        a = 0
        result = None
        while a != count:
            result = func(x)
            a += 1
        return result
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
