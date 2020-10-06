'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod


class Clothing(ABC):
    @abstractmethod
    def consumption(self):
        return float


class Coat(Clothing):
    def __init__(self, name: str, size: float, quantity=1):
        self.name = name
        self.size = size
        self.quantity = quantity

    @property
    def consumption(self):
        return (self.size / 6.5 + 0.5) * self.quantity


class Suit(Clothing):
    def __init__(self, name: str, height: float, quantity=1):
        self.name = name
        self.height = height
        self.quantity = quantity

    @property
    def consumption(self):
        return (2 * self.height + 0.3) * self.quantity


coat = Coat('Winter coat', 25)
print(coat.consumption)

suit = Suit('Business suit', 30.80)
print(suit.consumption)






