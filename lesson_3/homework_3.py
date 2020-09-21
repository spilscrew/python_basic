'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
'''


def my_func(a, b, c):
    '''
    Sum of 2 the largest parameters.
    :param a: first number (int)
    :param b: second number (int)
    :param c: third number (int)
    :return: sum of largest param
    '''
    values_list = [a, b, c]
    first_max = max(values_list)
    values_list.remove(first_max)
    second_max = max(values_list)
    return first_max + second_max


print(my_func(4, 9, 5))  # output is 14
