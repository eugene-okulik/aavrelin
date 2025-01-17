text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel.\
 Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
words = text.split()
print(words)
new_text = []
for word in words:
    if '.' in word:
        word_new = word.replace('.','ing.')
        new_text.append(word_new)
    elif ',' in word:
        word_new = word.replace(',', 'ing,')
        new_text.append(word_new)
    else:
        new_text.append(word + 'ing')
print(' '.join(new_text))