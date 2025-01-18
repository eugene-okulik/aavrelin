result_1 = 'результат операции: 42'
result_2 = 'результат операции: 54'
result_3 = 'результат работы программы: 209'
result_4 = 'результат: 2'


def sum_result(*args):
    sum_all = 0
    for result in args:
        a = int((result.split())[-1]) + 10
        sum_all += a
    print(sum_all)


sum_result(result_1, result_2, result_3, result_4)
