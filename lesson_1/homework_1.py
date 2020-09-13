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