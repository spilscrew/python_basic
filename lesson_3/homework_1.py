'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
'''

ask_number_1, ask_number_2 = 'Please enter first number:\n', 'Please enter second number:\n'

def divide_func():
    num_1, num_2 = True, True


    def ask_input_1():
        num_1 = input(ask_number_1)


    def ask_input_2():
        num_2 = input(ask_number_2)

    ask_input_1()
    ask_input_2()

    try:
        int(num_1), float(num_1)
    except ValueError:
        print('First input is wrong! Please use numbers!\n')
        ask_input_1()

    try:
        int(num_2), float(num_2)
    except ValueError:
        print('First input is wrong! Please use numbers!\n')
        ask_input_2()

    print(num_1 / num_2)


divide_func()