'''
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

а) итератор, генерирующий целые числа, начиная с указанного

'''

from sys import argv
from itertools import count

script_name, a_start_number, a_end_number = argv

try:
    a_start_number, a_end_number = int(a_start_number), int(a_end_number)
    for num in count(a_start_number):
        print(num)
        if num == a_end_number:
            break
except ValueError:
    print('Please user only whole numbers!')

