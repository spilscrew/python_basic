'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import os
from statistics import mean
import json

file_name = 'homework_7.txt'
file_folder = os.path.dirname(__file__)
file_path = os.path.join(file_folder, file_name)

companies_data = []
with open(file_path, 'r', encoding='UTF-8') as file:
    average_profit = []
    companies_data.append({})
    for line in file:
        line_list = line.split(' ')
        profit = int(line_list[2]) - int(line_list[3])
        companies_data[0][line_list[0]] = profit
        if profit > 0:
            average_profit.append(profit)
    companies_data.append({'average_profit': round(mean(average_profit), 2)})

json_file_name = 'homework_7.json'
json_file_path = os.path.join(file_folder, json_file_name)

with open(json_file_path, 'w') as file:
    json.dump(companies_data, file)


