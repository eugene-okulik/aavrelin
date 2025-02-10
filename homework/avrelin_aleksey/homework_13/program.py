import os
import datetime

file_name = 'data.txt'
base_path = os.path.dirname(__file__)
homework_path_path = os.path.dirname(os.path.dirname(os.path.dirname(base_path)))
data_file_path_okulik = os.path.join(
    homework_path_path, 'homework', 'eugene_okulik', 'hw_13', file_name
)
print(data_file_path_okulik)


# Открываем файл для прочтения
def read_file():
    try:
        with open(data_file_path_okulik, 'r', encoding='utf-8') as data_file:
            for line in data_file.readlines():
                yield line
    except FileNotFoundError:
        print(f'Файл {file_name} не найден')


# Вычитываем дату из строки
def read_file_number(line):
    try:
        number_and_date = line.split(' -')[0]
        separation_number, separation_date = number_and_date.split('. ', 1)
        number = int(separation_number)
        result_date = datetime.datetime.strptime(
            separation_date, '%Y-%m-%d %H:%M:%S.%f'
        )

        if number == 1:
            new_date = result_date + datetime.timedelta(weeks=1)
            print(new_date)

        elif number == 2:
            print(result_date.strftime('%A'))

        elif number == 3:
            day_ago = (datetime.datetime.now() - result_date).days
            print(day_ago)

    except ValueError:
        print('Ошибка преобразования')


# Выполняем код условия
for line in read_file():
    read_file_number(line)
