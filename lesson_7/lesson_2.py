class Speed:
    __slots__ = ('kmh',)

    def __init__(self):
        self.kmh = 0

    @property
    def meters_sec(self):
        return self.kmh / 3.6

    @meters_sec.setter
    def meters_sec(self, value):
        self.kmh = value * 3600

    @property
    def mph(self):
        return self.kmh / 1.609

    @mph.setter
    def mph(self, value):
        self.kmh = value * 1.609


if __name__ == '__main__':
    speed = Speed()
    speed.kmh = 100
    print(1)
