'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
'''


class Worker:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.position = str
        self._income = {'salary': float(), 'award': float()}

    def get_worker_full_name(self):
        full_name = f'{self.name} {self.surname}'
        print(full_name)
        return full_name


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, salary: float, award: float):
        super().__init__(name, surname)
        self.position = position
        self._income['salary'] = salary
        self._income['award'] = award

    def get_worker_total_income(self):
        total_income = self._income['salary'] + self._income['award']
        print(total_income)
        return total_income


worker_1 = Position('Ivan', 'Ivanov', 'Manager', 500.0, 100.0)
worker_1.get_worker_full_name()
worker_1.get_worker_total_income()

worker_2 = Worker('Sergey', 'Petrov')
worker_2.get_worker_full_name()
worker_2 = Position('Sergey', 'Petrov', 'CTO', 3000, 400)
worker_2.get_worker_full_name()
worker_2.get_worker_total_income()
