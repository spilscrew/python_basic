'''
class Animal:
    name = 'Animal name'
    age = 0
    mass = 1


print(animal_1.age)
animal_2.age = 23
print(animal_2.age)  # 23
Animal.age = 5
print(animal_2.age)  # 23
animal_2.test = 500
print(animal_2.test)
'''

import random
NAMES = ('Barsik', 'Lonik', 'Bobik', 'Sharik')  # Константа


class Animal:
    _mass = 1  # _Protected
    __age = 0  # __Private
    __population = []

    def __init__(self, a_type, mass):
        print('--- START INIT ---')
        print(id(self))
        self.a_type = a_type
        self.mass = mass
        print('--- END INIT ---')
        self.__population.append(self)

    def say(self):
        print(f'{self.a_type} VOICE')

    def get_age(self):
        return self.__age

    def get_population(self):
        return tuple(self.__population)

    def breeding(self, other):
        cls = random.choice((type(self), type(other)))
        return cls(self.a_type, random.randint(1, 10))


class Dog(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__('Dog', random.randint(1, 3))

    def say(self):
        print('Bark bark')

    def breeding(self, other):
        cls = random.choice((type(self), type(other)))
        return cls(random.choice(NAMES))


class Cat(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__('Cat', random.randint(1, 3))

    def say(self):
        print('Meow meow')


animal_1 = Animal('Dog', 15)
dog_1 = Dog('Muhtar')
dog_2 = Dog('Bobik')
animal_2 = Animal('Cat', 18)
cat_1 = Cat('Barsik')
cat_2 = Cat('Lonik')
