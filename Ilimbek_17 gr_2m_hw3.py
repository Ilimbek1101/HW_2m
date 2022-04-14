# Выполнение домашнего задания 3, ООП (2 месяц).
# Операции с дробями и палиндромные числа.

class Fraction:

    def __init__(self, numertor, denumerator):
        self.numertor = numertor
        self.denumerator = denumerator

    def _get_fraction(self):
        print(f'{self.numertor} / {self.denumerator}')

    def __add__(self, other):
        print("Is Dunder Method __add__")
        self.numertor = num1.numertor * num2.denumerator + num2.numertor * num1.denumerator
        self.denumerator = num1.denumerator * num2.denumerator
        self._get_fraction()

    def __sub__(self, other):
        print("Is Dunder Method __sub__")
        self.numertor = num1.numertor * num2.denumerator - num2.numertor * num1.denumerator
        self.denumerator = num1.denumerator * num2.denumerator
        self._get_fraction()

    def __mul__(self, other):
        print("Its Dunder Method __mul__")
        self.numertor = num1.numertor * num2.numertor
        self.denumerator = num1.denumerator * num2.denumerator
        self._get_fraction()

    def __floordiv__(self, other):
        print("Its Dunder Method __floordiv__")
        self.numertor = num1.numertor * num2.denumerator
        self.denumerator = num1.denumerator * num2.numertor
        self._get_fraction()

num1 = Fraction(2, 3)
num2 = Fraction(4, 5)

num1 + num2
# num1 - num2
# num1 * num2
# num1 // num2


# ExtraTask:
def palindrome():
    x = int(input('Задайте число x = '))
    if x == int(str(x)[::-1]):
        print(f'Число {x} является палиндромом')
    else:
        print(f'Число {x} не является палиндромом')

palindrome()

