'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
'''


class Storage:
    def __init__(self):
        pass


class OfficeEquipment:
    __units_all = 0
    __units_added = 0

    def __init__(self, units=0):
        self.__units = units
        self.__units_added = self.__units_added

    @property
    def units_all(self):
        return self.__units

    @property
    def units_added(self):
        return self.__units_added

    @units_added.setter
    def units_set(self, __units_added):
        self.__units_added += __units_added


class Printer(OfficeEquipment):
    def __init__(self, brand: str, quantity: int):
        super().__init__()
        self.brand = brand
        self.quantity = quantity
        print(self.units_added)

        if quantity > 0:
            self.units_set(self, quantity)
        pass


class Scanner(OfficeEquipment):
    def __init__(self, brand: str, quantity: int):
        super().__init__()
        self.brand = brand
        self.quantity = quantity
        if quantity > 0:
            OfficeEquipment.units_set(self, quantity)
        pass


class Xerox(OfficeEquipment):
    def __init__(self, brand: str, quantity: int):
        super().__init__()
        self.brand = brand
        self.quantity = quantity
        if quantity > 0:
            OfficeEquipment.units_set(self, quantity)
        pass


storage = Storage()
office_equip = OfficeEquipment(units=100)
print(office_equip.units_all)

sony_printers = Printer(brand='Sony', quantity=15)
samsung_printers = Printer(brand='Samsung', quantity=25)

sony_scanners = Scanner(brand='Sony', quantity=10)
samsung_scanners = Scanner(brand='Samsung', quantity=10)

sony_xerox = Xerox(brand='Sony', quantity=10)
samsung_xerox = Xerox(brand='Samsung', quantity=10)
