text = 'результат операции: 42\n\
результат операции: 514\n\
результат работы программы: 9'

number_1_index_1 = text.index(':')
number_1_index_2 = text.find('р', number_1_index_1)
number_1 = text[number_1_index_1 + 2:number_1_index_2]

number_2_index_1 = text.index(':',number_1_index_1 + 1)
number_2_index_2 = text.find('р', number_2_index_1)
number_2 = text[number_2_index_1 + 2:number_2_index_2]

number_3_index_1 = text.index(':',number_2_index_1 + 1)
number_3 = text[number_3_index_1 + 2:]

print(int(number_1)+10+int(number_2)+10+int(number_3)+10)
