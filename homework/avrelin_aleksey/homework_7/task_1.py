safe = int(input("Введи цифру которая будет храниться в переменной 'safe': "))

def result (number):
    while number != safe:
        print ('попробуйте снова')
        number= int(input("Угадай цифру: "))
    else:
        print('Поздравляю! Вы угадали!')

result(int(input("Угадай цифру: ")))
