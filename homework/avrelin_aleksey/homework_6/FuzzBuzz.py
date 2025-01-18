test = range(1, 101)
for a in test:
    if a >= 1 or a <= 100:
        if a % 3 == 0 and a % 5 == 0:
            a = "FuzzBuzz"
            print(a)
        elif a % 3 == 0 and a % 5 != 0:
            a = "Fuzz"
            print(a)
        elif a % 3 != 0 and a % 5 == 0:
            a = "Buzz"
            print(a)
        else:
            print(a)
