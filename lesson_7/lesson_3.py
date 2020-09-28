import time


class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __del__(self):
        print('I\'am your father!')

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return type(self)(other.name, self.surname)


class GarageIter:
    def __init__(self, box):
        self.__idx = 0
        self.__box = box

    def __next__(self):
        while self.__idx < len(self.__box):
            self.__idx += 1
            if self.__box[self.__idx - 1].vin:
                return self.__box[self.__idx - 1]

        raise StopIteration


class Garage:
    def __init__(self, name):
        self.name = name
        self.__box = []

    def set_car(self, car):
        self.__box.append(car)

    def __getitem__(self, item):
        return self.__box[item]

    def __iter__(self):
        return GarageIter(self.__box)


class Car:
    def __init__(self, name, vin=None):
        self.name = name
        self.vin = vin


if __name__ == '__main__':
    '''
    human = Human('Dart', 'Vader')
    human2 = Human('Princess', 'Lea')
    human3 = human + human2  # equal human3 = human.__add__(human2)
    print(human3)
    a = str(human)
    print(human)
    print(a)

    a = 1
    b = 2
    c = a + b
    '''
    garage = Garage('Crazy Monkey')
    garage.set_car(Car('Ford', 14444))
    garage.set_car(Car('GMC', 40504))
    garage.set_car(Car('BMW', 43456))
    print(garage[0])
    for car in garage:
        print(car)
