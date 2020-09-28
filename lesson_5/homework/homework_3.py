'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто
 из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
 сотрудников.
'''

import os

file_name = 'homework_3.txt'
file_folder = os.path.dirname(__file__)
file_path = os.path.join(file_folder, file_name)

with open(file_path) as file:
    staff_obj = {}
    for index, line in enumerate(file):
        line_item = line.split(':')
        staff_obj[index] = {'name': line_item[0], 'salary': line_item[1].rstrip()}


def currency_format(symbol: str, amount: float):
    '''
    Return amount in currency format.
    :param symbol: currency prefix symbol
    :param amount: amount to format
    :return: formatted string
    '''
    return str(symbol + '{:,.2f}'.format(amount))


salary_avg = 0
for worker in staff_obj.values():
    try:
        worker_salary = float(worker['salary'])
        if worker_salary <= 0:
            raise ValueError
        if worker_salary < 20000:
            print(f'{worker["name"]} have less than ₽20.000 ({currency_format("₽", worker_salary)}) salary!')
        salary_avg += int(worker['salary'])
    except ValueError:
        print(f'{worker["name"]} salary value must be positive number!')
salary_avg = salary_avg / len(staff_obj)

print(f'Staff average salary: {currency_format("₽", salary_avg)}')

