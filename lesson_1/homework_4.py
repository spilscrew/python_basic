'''
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.
'''

ask_number = 'Please enter positive number:\n'

number = input(ask_number)

if number.isdigit():
    number_for_check = int(number)
    the_biggest_digit = 0
    while number_for_check:
        current_number = number_for_check % 10
        if current_number > the_biggest_digit:
            the_biggest_digit = current_number
        number_for_check = number_for_check // 10
    else:
        print('The biggest digit in ' + number + ' is ' + str(the_biggest_digit))
else:
    print('Wrong data is entered!\nPlease enter the whole positive number.')