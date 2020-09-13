'''
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. 
Считаем 3 + 33 + 333 = 369.
'''

ask_number = 'Please enter number:\n'

number = input(ask_number)

if number.isdigit():
    number_1 = int(number)
    number_2 = int(number + number)
    number_3 = int(number + number + number)
    print(number_1 + number_2 + number_3)
else:
    print('Wrong data is entered!\nPlease enter the whole number.')