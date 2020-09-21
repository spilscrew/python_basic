'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
'''


def user_data(name: str, surname: str, birth_year: int, city: str, email: str, phone: int):
    '''
    Put user data parameters in dictionary and return it.
    :param name: user name (str)
    :param surname: user surname (str)
    :param birth_year: user birth_year (int)
    :param city: user city (str)
    :param email: user email (str)
    :param phone: user phone (int)
    :return: use_obj (dict)
    '''
    usr_obj = {
        'name': name,
        'surname': surname,
        'birth year': birth_year,
        'city': city,
        'email': email,
        'phone': phone
    }
    return usr_obj


data = user_data(name='Vasja', surname='Pupkin', birth_year=1984, city='Abu Dhabi', email='mas101km@gmail.com',
                 phone=34567865)

print(f"{data['name']} {data['surname']} {data['birth year']} {data['city']} {data['email']} {data['phone']}")