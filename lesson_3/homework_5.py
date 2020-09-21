'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
'''


def input_sum(input_list: list):
    '''
    Gets input_list (float, int) and sum items
    :param input_list: list of numbers to sum
    :return: result of list items sum, flag for cycle stop if found not digit symbol
    '''
    result = 0
    stop_flag = False
    for val in input_list:
        try:
            result += float(val)
        except ValueError:
            stop_flag = True
            break
    return result, stop_flag


ask_input = 'Please enter numbers space separated:\n'
final_sum = 0
while True:
    _input_list = input(ask_input).split(' ')
    _input_list_sum, _stop_flag = input_sum(_input_list)
    final_sum += _input_list_sum
    print(final_sum)
    if _stop_flag:
        break
