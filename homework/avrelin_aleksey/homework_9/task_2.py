temperatures = [20, 15, 32, 34, 21, 19,
                25, 27, 30, 32, 34, 30,
                29, 25, 27, 22, 22, 23,
                25, 29, 29, 31, 33, 31,
                30, 32, 30, 28, 24, 23]


def new_temperatures(x):
    if x > 28:
        return x


hot_days = list(filter(None, map(new_temperatures, temperatures)))
print('Минимальная температура: ', min(hot_days))
print('Средняя температура: ', round(sum(hot_days) / len(hot_days)))
print('Макмальная температура: ', max(hot_days))
