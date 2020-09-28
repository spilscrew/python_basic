'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

import os

file_name = 'homework_4.txt'
generated_file_name = 'homework_4_g.txt'
file_folder = os.path.dirname(__file__)
file_path = os.path.join(file_folder, file_name)
generated_file_path = os.path.join(file_folder, generated_file_name)

changed_values_list = ['Один', 'Два', 'Три', 'Четыре']
with open(file_path, encoding='UTF-8') as file:
    for index, line in enumerate(file):
        with open(generated_file_path, 'a', encoding='UTF-8') as generated_file:
            first_part = line.split('—')[0]
            second_part = line.split('—')[1]
            last_break = '\n' if str(index + 1) == line[-1] else ''
            generated_file.write(first_part.replace(first_part, changed_values_list[index]) + ' — ' + second_part +
                                 last_break)
