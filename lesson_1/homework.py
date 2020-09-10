'''
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и
сохраните в переменные, выведите на экран.
'''

question_name = 'What\'s your name?\n'
question_age = 'How old are you?\n'

name = input(question_name)
age = input(question_age)

if age.isdigit():
    print('Hello ' + name + '!\n' + 'Your age is ' + age + '.')
else:
    print('Hello ' + name + '!\n' + 'We cannot recognise your age' + '.')

'''
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.
'''

ask_seconds = 'Enter the time in seconds:\n'

seconds = input(ask_seconds)

if seconds.isdigit():
    seconds = int(seconds)
    hours = seconds // 3600 % 24
    minutes = seconds // 60 % 60
    seconds = seconds % 60
    print('%02d:%02d:%02d' % (hours, minutes, seconds))
else:
    print('Wrong data is entered!\nPlease enter the whole number.')

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

'''
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает 
фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. 
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''

#  Не хватило времени.

'''
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
'''

#  Не хватило времени.