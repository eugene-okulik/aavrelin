def repeat_me(count):
    def function(func):
        def wrapper(text):
            a = 0
            while a != count:
                func(text)
                a += 1
        return wrapper
    return function


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
