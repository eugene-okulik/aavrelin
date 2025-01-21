import random


salary_input = int(input("Введи целое число: "))


def two_case(salary):
    bonus = random.choice([True, False])
    bonus_random = random.randint(1,100000)
    salary_bonus = salary + int(bonus_random)
    if bonus is True:
        print(f"{salary}, {bonus} - '${salary_bonus}'")
    else:
        print(f"{salary}, {bonus} - '$ {salary}")


two_case(salary_input)
