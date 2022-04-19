# Выполнение домашнего задания 4, ООП (2 месяц).
# Создание пакетов и модулей, импорт модулей, классов и методов.

from create_car import Car
from get_car_info import get_car_info

Bmw = Car('BMW', '525', '1555 kg', 192, 260, '220 km/h', 'red')

Bmw.start_engine()
Bmw.stop_engine()
get_car_info(Bmw)