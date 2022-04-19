# Выполнение домашнего задания 4, ООП (2 месяц).
# Создание пакетов и модулей, импорт методов.

class Car:

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