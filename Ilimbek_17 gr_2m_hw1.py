# Выполнение домашнего задания 1, ООП (2 месяц).
# Создание классов машин, атрибуты, методы.

class Cars:

    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f'{self.title} {self.model} engine started!')

    def stop_engine(self):
        print(f'{self.title} {self.model} engine stoped!')

    def info(self):
        print(f' Title: {self.title}\n Model: {self.model}\n Weight: {self.weight}\n Hp: {self.hp}\n'
              f' Nm: {self.nm}\n Max_speed: {self.max_speed}\n Color: {self.color}\n')

Bmw = Cars('BMW', '525', '1555 kg', 192, 260, '220 km/h', 'red')
Bmw.start_engine()
Bmw.stop_engine()
Bmw.info()

Mersedes = Cars('Mersedes', 'S600', '2180 kg', 517, 830, '250 km/h', 'black')
Mersedes.start_engine()
Mersedes.stop_engine()
Mersedes.info()