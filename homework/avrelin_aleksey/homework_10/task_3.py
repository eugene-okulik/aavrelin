def arithmetic(func):

    def wrapper(x, y, operation):
        if x < 0 or y < 0:
             operation = '*'
        elif x == y:
             operation = '+'
        elif x > y:
             operation = '-'
        elif x < y:
             operation = '/'
        return func(first, second, operation)

    return wrapper


@arithmetic
def calc(first, second, operation):
    if second == 0:
        print('На ноль делить нельзя')
    else:
        if operation == '+':
            return first + second
        elif operation == '-':
            return first - second
        elif operation == '*':
            return first * second
        elif operation == '/':
            return first / second


first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))


result_calc = calc(first, second, None)
print(result_calc)
