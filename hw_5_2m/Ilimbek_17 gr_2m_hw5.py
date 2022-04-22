# Выполнение домашнего задания 5, ООП (2 месяц).
# Регулярные выражения.

import re

class ValidCarNumber:

    def is_valid(self, number):
        is_valid = re.search(r"[0]([1-9]{1})([KG]{2})([0-9]{3})([A-Z]{3})", number)
        if is_valid == None:
            print(f'номер {number} не валидный!')
        else:
            print(f'номер {number} валидный!')

number = ValidCarNumber()
number.is_valid('01KG777BMW')
number.is_valid('hhh777hhh')
number.is_valid('09KG007BMW')
number.is_valid('14KG783AAQ')