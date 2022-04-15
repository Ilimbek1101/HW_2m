# Выполнение домашнего задания 3, ООП (2 месяц).
# Операции с дробями и палиндромные числа.

class Fraction:

    def __init__(self, numertor, denumerator):
        self.numertor = numertor
        self.denumerator = denumerator

    def _get_fraction(self):
        print(f'{self.numertor} / {self.denumerator}')

    def __add__(self, other):
        num = self.numertor
        self.numertor = self.numertor + self.denumerator*other
        self._get_fraction()
        self.numertor = num

    def __sub__(self, other):
        num = self.numertor
        self.numertor = self.numertor - self.denumerator * other
        self._get_fraction()
        self.numertor = num

    def __mul__(self, other):
        num = self.numertor
        self.numertor = self.numertor * other
        self._get_fraction()
        self.numertor = num

    def __floordiv__(self, other):
        num = self.denumerator
        self.denumerator = self.denumerator * other
        self._get_fraction()
        self.denumerator = num


num = Fraction(2, 3)

num + 10
num - 1
num * 2
num // 4

# ExtraTask:
def palindrome():
    x = int(input('Задайте число x = '))
    if x == int(str(x)[::-1]):
        print(f'Число {x} является палиндромом')
    else:
        print(f'Число {x} не является палиндромом')

palindrome()