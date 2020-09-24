'''
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

б) итератор, повторяющий элементы некоторого списка, определенного заранее

'''

from sys import argv
from itertools import cycle

script_name = argv
b_list, b_repeat_times = [1, 2, 3, 4, 5], 3
try:
    b_list = list(b_list)
    try:
        b_repeat_times = int(b_repeat_times)
        for num in cycle(b_list):
            print(num)
            if num == b_list[-1]:
                b_repeat_times -= 1
                print('---')
            if not b_repeat_times:
                break
    except ValueError:
        print('Please user only whole numbers!')
except ValueError:
    print('First parameter must be a list!')