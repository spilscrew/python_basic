'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
'''


class Custom_Zero_Division_Error(Exception):
    error_text = 'You cannot divide by zero!'

    def __init__(self):
        print(Custom_Zero_Division_Error.error_text)


def custom_division(dividend, divisor):
    if not divisor:
        raise Custom_Zero_Division_Error

    return dividend / divisor


ask_dividend = 'Please enter dividend!\n'
ask_divisor = 'Please enter divisor!\n'

while True:
    dividend_input = input(ask_dividend)
    divisor_input = input(ask_divisor)
    try:
        dividend_input = float(dividend_input)
        divisor_input = float(divisor_input)
        print(custom_division(dividend_input, divisor_input))
        break
    except ValueError:
        print('Values must be numbers!\n')
    except Custom_Zero_Division_Error as error:
        ''




