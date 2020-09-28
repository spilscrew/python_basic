'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
'''

import os

file_name = 'homework_5.txt'
file_folder = os.path.dirname(__file__)
file_path = os.path.join(file_folder, file_name)

nums_to_sum = '10 10.5 20.5 50 2 30'
with open(file_path, 'w+', encoding='UTF-8') as file:
    file.write(nums_to_sum)
    file.seek(0)
    print(sum(map(float, file.read().split(' '))))  # sum of nums_to_sum is 123
