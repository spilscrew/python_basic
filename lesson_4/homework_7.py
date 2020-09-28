'''
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''

from math import factorial


def fact(num: float):
    yield factorial(num)


for el in fact(4):
    print(el)


def fact_custom(num: float):
    '''
    The function gets the number and returns factorial steps.
    :param num: float
    :return: number num factorial steps
    '''
    try:
        num = float(num)
        if num <= 0:
            raise ValueError
    except ValueError:
        return 'Number must be positive!'
    counter = 1
    result = 1
    while counter <= num:
        yield result
        counter += 1
        result *= counter


for el in fact_custom(4):
    print(el)