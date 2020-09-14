'''
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
'''

variable_list = [1, True, 3.4, 'string', ['a', 'b', 'c'], {1, 2, 3}, {1: 1, 2: 2, 3: 3}, (1, 2, 3)]

for data in variable_list:
    message = str(data) + ' is ' + str(type(data))
    if type(data) == int:
        print(message)
    elif type(data) == bool:
        print(message)
    elif type(data) == float:
        print(message)
    elif type(data) == str:
        print(message)
    elif type(data) == list:
        print(message)
    elif type(data) == set:
        print(message)
    elif type(data) == dict:
        print(message)
    elif type(data) == tuple:
        print(message)