'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
'''

calendar = {
    1: {
        'season': 'winter',
        'name': 'january'
    },
    2: {
        'season': 'winter',
        'name': 'february'
    },
    3: {
        'season': 'spring',
        'name': 'march'
    },
    4: {
        'season': 'spring',
        'name': 'april'
    },
    5: {
        'season': 'spring',
        'name': 'may'
    },
    6: {
        'season': 'summer',
        'name': 'june'
    },
    7: {
        'season': 'summer',
        'name': 'july'
    },
    8: {
        'season': 'summer',
        'name': 'august'
    },
    9: {
        'season': 'autumn',
        'name': 'september'
    },
    10: {
        'season': 'autumn',
        'name': 'october'
    },
    11: {
        'season': 'autumn',
        'name': 'november'
    },
    12: {
        'season': 'winter',
        'name': 'december'
    }
}

ask_month_number = 'Please enter number of month:\n'
input_error_type_message = 'Please use only whole numbers!\n'
input_error_interval_message = 'Please enter a number from 1 till 12!\n'

month_number = input(ask_month_number)

while True:
    if not month_number.isdigit():
        month_number = input(input_error_type_message + ask_month_number)
        continue
    elif int(month_number) > 12 or int(month_number) < 1:
        month_number = input(input_error_interval_message + ask_month_number)
        continue
    else:
        month_number = int(month_number)
        break

print((calendar[month_number]['name']).capitalize() + ' is ' + (calendar[month_number]['season']).capitalize() + ' season!')