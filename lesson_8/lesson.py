import requests


class CustomError(Exception):
    def __init__(self, text=None):
        self.text = text

'''
def custom_f(number):
    for num in range(number):
        if num == 15:
            raise CustomError('Custom error text')


try:
    custom_f(30)
except CustomError as e:
    print('error', e)
'''


class Product:
    id = ''
    name = ''

    def __init_(self, data: dict):
        for key, value in data.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Parser:
    __headers = {}
    __params = {
        'records_per_page': 50,
        'categories': ''
    }

    def __init__(self, stat_url: str):
        self.__start_url = stat_url
        self.products = []

    def parse(self):
        url = self.__start_url
        while url:
            response = requests.get(url, params=self.__params, header=self.__headers)
            data = response.json()
            url = None  # data['next']
            self.products.extend(Product(itm) for itm in data['results'])
