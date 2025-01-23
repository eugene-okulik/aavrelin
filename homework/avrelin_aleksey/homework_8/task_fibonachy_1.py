# Учитываем, что первым числом в фибоначи идет 0
def fibon(*args):
    fn1 = 0
    fn2 = 1
    fn = 0
    n = 0
    while True:
        for a in args:
            if n + 1 == a:
                yield f"{a}-ым числом фибоначи является: {fn}"
        fn = fn1 + fn2
        fn2 = fn1
        fn1 = fn
        n += 1


# number = input('Введи номер результата,через запятую: ')
# args = [int(a) for a in number.split(',')]
# args = (5, 200, 1000, 10)
# result = list(fibon(*args))
# for b in result:
#     print(b)
args = (5, 200, 1000, 10)
for result in fibon(*args):
    print(result)