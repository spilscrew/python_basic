'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''

import moment


class Data:
    def __init__(self, date):
        self.date = date

    @property
    def get_date(self):
        return self.date

    @staticmethod
    def date_validation(data: dict):
        response = {
            'status': True,
            'message': []
        }

        try:
            data = dict(data)
        except ValueError:
            response['status'] = False
            response['message'].append('For validate date please, use date_to_dict() format')
            return response

        if not data['day'] in range(1, 31):
            response['status'] = False
            response['message'].append('Day is invalid')
        if not data['month'] in range(1, 12):
            response['status'] = False
            response['message'].append('Month is invalid')
        if response['status']:
            response['message'].append('Date is valid')

        return response

    @classmethod
    def date_to_dict(cls, date):
        date_list = date.split('-')
        date_dict = {
            'day': int(date_list[0]),
            'month': int(date_list[1]),
            'year': int(date_list[2]),
        }
        return date_dict


data_date = moment.now().format('DD-M-YYYY')
data_1 = Data(data_date)
print(f'{id(data_1)}: {data_1.get_date}')
print(data_1.date_validation(data_1.get_date))

print('\n###########################\n')

data_date_2 = moment.now().subtract(days=1, months=1, years=2).format('DD-M-YYYY')
data_2 = Data(data_date_2)
print(f'{id(data_2)}: {data_2.get_date}')
data_2__date_dict = data_2.date_to_dict(data_2.get_date)
print(f'{id(data_2)}: {data_2__date_dict}')
print(data_2.date_validation(data_2__date_dict))

print('\n###########################\n')

data_date_3 = '32-13-2020'
data_3 = Data(data_date_3)
print(f'{id(data_3)}: {data_3.get_date}')
data_3__date_dict = data_3.date_to_dict(data_3.get_date)
print(f'{id(data_3)}: {data_3__date_dict}')
print(data_3.date_validation(data_3__date_dict))



