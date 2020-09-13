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