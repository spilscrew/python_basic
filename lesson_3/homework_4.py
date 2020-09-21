'''
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''


def my_func(x: float, y: int):
    '''
    Program get x and y, check if y is negative whole number and return x to the power of y.
    :param x: number (float)
    :param y: whole number (negative int)
    :return: x ** -y
    '''
    try:
        if y < 0 and isinstance(y, int):
            result = x ** y
        else:
            return 'Second parameter must be negative whole number!'
    except ValueError and TypeError:
        return 'First parameter must be number.\nSecond parameter must be negative whole number.'
    else:
        return result


print(my_func(2, -4))  # result: 0.0625


def my_func(x: float, y: int):
    '''
    Program get x and y, check if y is negative whole number and return x to the power of y.
    :param x: number (float)
    :param y: whole number (negative int)
    :return: x ** -y
    '''
    result = 0
    try:
        if y < 0 and isinstance(y, int):
            for _ in range(abs(y)):
                result += x * x
            result = 1 / result
        else:
            return 'Second parameter must be negative whole number!'
    except ValueError and TypeError:
        return 'First parameter must be number.\nSecond parameter must be negative whole number.'
    else:
        return result


print(my_func(2, -4))  # result: 0.0625
