# Выполнение домашнего задания 3 с сокращением дробей.

class Fraction:

    def __init__(self, numertor, denumerator):
        self.numertor = numertor
        self.denumerator = denumerator

    def _reduce_fraction(self, n, k):
        maxdel = 1
        i = 1
        while i != k+1:
            if n // i == n / i and k // i == k / i:
                maxdel = i
                # print(maxdel)
            i += 1
        n //= maxdel
        k //= maxdel
        print(f'{n}/{k}')

    def __add__(self, other):
        n = self.numertor
        d = self.denumerator

        print("Is Dunder Method __add__")
        self.numertor = num1.numertor * num2.denumerator + num2.numertor * num1.denumerator
        self.denumerator = num1.denumerator * num2.denumerator
        self._reduce_fraction(self.numertor, self.denumerator)

        num1.numertor = n
        num1.denumerator = d

    def __sub__(self, other):
        n = self.numertor
        d = self.denumerator

        print("Is Dunder Method __sub__")
        self.numertor = num1.numertor * num2.denumerator - num2.numertor * num1.denumerator
        self.denumerator = num1.denumerator * num2.denumerator
        self._reduce_fraction(self.numertor, self.denumerator)

        num1.numertor = n
        num1.denumerator = d

    def __mul__(self, other):
        n = self.numertor
        d = self.denumerator

        print("Its Dunder Method __mul__")
        self.numertor = num1.numertor * num2.numertor
        self.denumerator = num1.denumerator * num2.denumerator
        self._reduce_fraction(self.numertor, self.denumerator)

        num1.numertor = n
        num1.denumerator = d

    def __floordiv__(self, other):
        n = self.numertor
        d = self.denumerator

        print("Its Dunder Method __floordiv__")
        self.numertor = num1.numertor * num2.denumerator
        self.denumerator = num1.denumerator * num2.numertor
        self._reduce_fraction(self.numertor, self.denumerator)

        num1.numertor = n
        num1.denumerator = d

num1 = Fraction(1, 6)
num2 = Fraction(3, 8)

num1 + num2
num1 - num2
num1 * num2
num1 // num2


# ExtraTask:
def palindrome():
    x = int(input('Задайте число x = '))
    if x == int(str(x)[::-1]):
        print(f'Число {x} является палиндромом')
    else:
        print(f'Число {x} не является палиндромом')

palindrome()