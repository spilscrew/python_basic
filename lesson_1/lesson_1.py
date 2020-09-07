# PEP 8 - START
snake_case = 1
CamelCase = 2
# /PEP 8 - END

variable_string = "Hello world!"  # str()
variable_string_2 = 'Hello world!'  # str()

variable_integer = 1  # int()
variable_float = 2.3445  # float()
variable_bool = True  # bool()

# + - сложение
# - - вычитание
# * - умножение
# / - деление
# // - целочисленное деление (без остатка)
# % - остаток деления
# ** - степень

# '2' + 2 - ошибка
# int(variable_string) ошибка

'''
ask_name = "Введите имя \n"
ask_age = "Введите возраст \n"
name = input(ask_name)

print("Здравствуйте", name, end='!\n', sep=', ')

age = input(ask_age)

if age.isdigit():
    age = int(age)

    if age >= 18:
        print("Полный доступ")
    elif age >= 16:
        print("Доступ к боевикам")
    else:
        print("Доступ к мультикам")
else:
    print("Неверные данные \n")

print(isinstance(age, int) and age > 0)

if age % 2:
    print("Не чётное число")
else:
    print('Чётное число')

if not age % 2:
    print('Чётное число')
else:
    print("Не чётное число")
'''

number = 12345

while number:
    tmp = number % 10
    number = number // 10
    # или number //= 10
    if tmp == 5:
        continue  # break
    print(tmp)
else:
    print("ELSE")

number_2 = 12345
temporary = number_2
while tmp := temporary % 10 or temporary:
    temporary //= 10
    print(tmp, temporary)
else:
    print("ELSE")