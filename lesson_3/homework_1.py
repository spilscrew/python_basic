'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
'''

ask_dividend, ask_divisor = 'Please enter dividend number:\n', 'Please enter divisor number:\n'


def number_input(ask):
    num = input(ask)
    try:
        int(num) or float(num)
    except ValueError:
        return False
    return num


'''
if number_input(ask_dividend):
    print(True)
else:
    print(False)

def division(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError as e:
        print('nope')

print(division(3,'a'))
'''