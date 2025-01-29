PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price = PRICE_LIST.split()
PRICE_LIST_for_everyone = zip(price[::2], price[1::2])
PRICE_dict = {x: y[:-1] for x, y in PRICE_LIST_for_everyone}
print(PRICE_dict)
