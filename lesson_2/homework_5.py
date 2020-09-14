'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''

rating = [1, 9, 5, 6, 3]
rating.sort(reverse=True)

ask_number = 'Please enter number:\n'
input_error = 'Please enter whole positive number!\n'

number = input(ask_number)

while True:
    if not number.isdigit():
        number = input(input_error + ask_number)
        continue
    elif int(number) == 0:
        number = input(input_error + ask_number)
        continue
    else:
        number = int(number)
        break

if number in rating:
    rating.insert(rating.index(number), number)
else:
    counter = 0
    for element in rating:
        if number >= element:
            rating.insert(counter, number)
            break
        counter += 1

print(rating)