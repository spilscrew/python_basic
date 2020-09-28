'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

import os

file_name = 'homework_2.txt'
file_folder = os.path.dirname(__file__)
file_path = os.path.join(file_folder, file_name)

with open(file_path) as file:
    for index, line in enumerate(file, start=1):
        lines_count = index
        print('Line number ' + str(index) + ' words count: ' + str(len(line.split(' '))))
    print(lines_count)
