'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''

source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
generated_list = [element for idx, element in enumerate(source_list) if element != source_list[0] and source_list[idx] > source_list[idx - 1]]
print(generated_list)  # [12, 44, 4, 10, 78, 123]

source_list = [-54.5, 24, 0, 434, 3.4, 1.4, 4.456, 1203, 34.4, 5060, -123, -122, 456]
generated_list = [element for idx, element in enumerate(source_list) if element != source_list[0] and source_list[idx] > source_list[idx - 1]]
print(generated_list)  # [24, 434, 4.456, 1203, 5060, -122, 456]
