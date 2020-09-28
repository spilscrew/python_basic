'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

import os

file_name = 'homework_6.txt'
file_folder = os.path.dirname(__file__)
file_path = os.path.join(file_folder, file_name)

lessons_obj = {}
with open(file_path, 'r', encoding='UTF-8') as file:
    for line in file:
        lesson_obj_value = (line.split(':')[1].rstrip().replace('(l)', '').replace('(pw)', '').replace('(lab)', ''))\
            .split(' ')
        itm_sum = 0
        for itm in lesson_obj_value:
            try:
                itm = int(itm)
                itm_sum += itm
            except ValueError:
                pass
        lessons_obj[line.split(':')[0]] = itm_sum

print(lessons_obj)  # result is {'Math': 125, 'Biology': 140, 'Sport': 95, 'Crafts': 80, 'Chemistry': 90}
