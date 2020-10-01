'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см *
число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''


class Road:
    def __init__(self, length=0.0, width=0.0):
        self.__flag = True
        try:
            self._length = float(length)
            self._width = float(width)
            if self._length <= 0 or self._width <= 0:
                raise ValueError
        except ValueError or AttributeError:
            print('Length and width must be positive number!')
            self.__flag = False

    def asphalt_mass_calc(self, mass=0.0, thickness=0.0):
        if self.__flag:
            try:
                mass = float(mass)
                thickness = float(thickness)
                if mass <= 0 or thickness <= 0:
                    raise ValueError
                else:
                    print(self._length * self._width * mass * thickness)
                    return self._length * self._width * mass * thickness
            except ValueError or TypeError:
                print('Mass and thickness must be positive numbers!')


asphalt_mass = Road(20, 5000).asphalt_mass_calc(25, 5)
