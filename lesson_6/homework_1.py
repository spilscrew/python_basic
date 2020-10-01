'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
 реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
 Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
 на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
 (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
'''

from threading import Timer


class TrafficLights:
    __states = {
        'stop': {
            'color': 'red',
            'time': 7
        },
        'ready': {
            'color': 'yellow',
            'time': 2
        },
        'go': {
            'color': 'green',
            'time': 5
        }
    }
    __current_state = __states['stop']
    __next_state = __states['go']

    def __init__(self, __idx=0):
        self.__idx = __idx
        self.__color = self.__current_state['color']
        self.__state_time = self.__current_state['time']

    def start(self):
        self.state_timer()
        idx_str = '#' + str(self.__idx) + ' ' if self.__idx else ''
        print(f'{idx_str}TrafficLights state: {self.__color}')

    def state_timer(self):
        Timer(self.__state_time, self.state_switcher).start()

    def state_switcher(self):
        if self.__current_state == self.__states['ready']:
            self.__current_state = self.__next_state
            self.__next_state = self.next_state_init()
        else:
            self.__current_state = self.__states['ready']
        self.__color = self.__current_state['color']
        self.__state_time = self.__current_state['time']
        self.start()

    def next_state_init(self):
        return self.__states['go'] if self.__next_state == self.__states['stop'] else self.__states['stop']


traffic_lights_1 = TrafficLights(1)
traffic_lights_1.start()

traffic_lights_2 = TrafficLights(2)
Timer(3, traffic_lights_2.start).start()
