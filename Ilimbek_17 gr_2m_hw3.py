# Выполнение домашнего задания 3, ООП (2 месяц).
# .

class Fraction:

    def __init__(self, numertor, denumerator):
        self.numertor = numertor
        self.denumerator = denumerator

    def __add__(self, other):
        print("Is Dunder Method __add__")
        num = self.numertor/self.denumerator + other
        print(num)

    def __sub__(self, other):
        print("Is Dunder Method __sub__")
        num = self.numertor / self.denumerator - other
        print(num)

    def __mul__(self, other):
        print("Its Dunder Method __mul__")
        num = self.numertor / self.denumerator * other
        print(num)

    def __floordiv__(self, other):
        print("Its Dunder Method __floordiv__")
        num = int(self.numertor / self.denumerator) // other
        print(num)

num = Fraction(92, 15)

num + 10
num - 11
num * 60
num // 3


# ExtraTask:
def palindrome():
    x = int(input('Задайте число x = '))
    if x == int(str(x)[::-1]):
        print(f'Число {x} является палиндромом')
    else:
        print(f'Число {x} не является палиндромом')

palindrome()

