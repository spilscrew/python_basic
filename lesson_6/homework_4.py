'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'The "{self.name}" car started moving!'

    def stop(self):
        return f'The "{self.name}" car stopped!'

    def turn(self, direction):
        direction = direction.lower()
        if direction.lower() == 'left' or direction.lower() == 'right':
            return f'The "{self.name}" car turned on the {direction}!'
        else:
            return f'"{direction}" is wrong direction!'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        self.speed = speed

    def show_speed(self):
        try:
            self.speed = float(self.speed)
            if self.speed > 60:
                return f'"{self.name}" car speed is {self.speed}. Please slow down!'
            else:
                return f'"{self.name}" car speed is {self.speed}'
        except ValueError:
            return 'Speed must be positive number!'


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        try:
            self.speed = float(self.speed)
            if self.speed > 40:
                return f'"{self.name}" car speed is {self.speed}. Please slow down!'
            else:
                return f'"{self.name}" car speed is {self.speed}'
        except ValueError:
            return 'Speed must be positive number!'


class PoliceCar(Car):
    def __init__(self, speed):
        super().__init__(speed, 'Black & White', 'BMW', True)


town_car = TownCar(50, 'red', 'Audi')
print(town_car.speed)
print(town_car.color)
print(town_car.name)
print(town_car.go())
print(town_car.stop())
print(town_car.turn('left'))
print(town_car.turn('RIGHT'))
print(town_car.turn('error'))
print(town_car.show_speed())
town_car.speed = 65
print(town_car.show_speed())
work_car = WorkCar(60, 'green', 'Volvo')
print(work_car.show_speed())
police_car = PoliceCar(0)
print(police_car.color)
print(police_car.is_police)
print(town_car.is_police)