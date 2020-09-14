'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
'''

ask_words = 'Please enter words separated with space:\n'

words = input(ask_words).split()
max_length = 10

for index in range(len(words)):
    word = words[index]
    print(str(index + 1) + '. ' + word[0:10] + '...' if len(word) > 10 else str(index + 1) + '. ' + word)