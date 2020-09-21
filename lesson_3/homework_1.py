'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
'''

ask_dividend, ask_divisor = 'Please enter dividend number:\n', 'Please enter divisor number:\n'


def input_number_check(message: str):
    '''
    Input number type check.
    :param message: Input message (str)
    :return: Input number (int or float)
    '''
    while True:
        num = input(message)
        try:
            num = int(num)
        except ValueError:
            try:
                num = float(num)
            except ValueError:
                print('Please use only numbers!')
                pass
            else:
                break
        else:
            break
    return num


def division_func(dividend: int or float, divisor: int or float):
    '''
    Input numbers division function;
    Input numbers zero division check.
    :param dividend: dividend (int or float)
    :param divisor: divisor (int or float)
    :return: result of division dividend on the divisor
    '''
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        print('You can\'t divide by zero!')
        return False
    return result


_dividend = input_number_check(ask_dividend)
_divisor = input_number_check(ask_divisor)
_result = division_func(_dividend, _divisor)

print(f"{_dividend} / {_divisor} = {_result}" if _result else '')


