my_dict = {'tuple': (), 'list': [], 'dict': {}, 'set': {}}

my_dict['tuple'] = (42, 2, 'Hello', True, 111)
my_dict['list'] = [1, 2, 3, 'Python', False, 2.2]
my_dict['dict'] = {'number': 456, 'text': 'Aleksey', 'valid': True, 1: 1, 'one': 'onw'}
my_dict['set'] = {5, 1, 4, 'apple', True, None, 3.14, 4, 'orange', False, 5, 7}

print("Последний элемент словаря:", my_dict['tuple'][-1])
my_dict['list'].append('333')
print("В конец списка добавлен '333':", my_dict['list'])
my_dict['list'].pop(1)
print("Удален второй элемент списка:", my_dict['list'])
my_dict['dict']['three'] = 'value3'
print("Добавлен ('three':'value3') в словарь 'dict':", my_dict['dict'])
my_dict['dict'].pop('number')
print("Удален 'number' в словаре 'dict':", my_dict['dict'])
my_dict['set'].add('new_word')
print("Добавлено 'new_word' в множество 'set':", my_dict['set'])
my_dict['set'].pop()
print("Удален любой элемент из множества 'set':", my_dict['set'])
print("\nИтоговый словарь my_dict:", my_dict)
