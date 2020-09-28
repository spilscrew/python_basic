'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка.
'''

import os

file_name = 'homework_1.txt'
file_folder = os.path.dirname(__file__)
file_path = os.path.join(file_folder, file_name)

with open(file_path, 'w', encoding='UTF-8') as file:
    input_text = True
    while input_text:
        input_text = input('Please input line:\n')
        file.write(input_text + '\n')
