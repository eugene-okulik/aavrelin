words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def new_function(**kwargs):
    for name, number in kwargs.items():
        print(name * number)


new_function(**words)
