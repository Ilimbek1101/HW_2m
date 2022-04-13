# Выполнение домашнего задания 2, ООП (2 месяц).
# Абстракция, наследование, полиморфизм, инкапсуляция.


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Jack(Person):

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance

class Vito(Jack):

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name, phone_number, balance)

    def changes(self):
        if wer.balance >= n:
            wer.balance -= n
            der.balance += n
            print(f'Jack balance = {wer.balance}\n'
                  f'Vito balance = {der.balance}')
        else:
            print(f'Jack, Ваш баланс недостаточен для подключения услуги в {n} сом')


n = int(input('Задайте число для вычета/добавления от/к баланса/у: '))

wer = Jack('Jack', 'Ferguson', '0553545454', 100)
der = Vito('Vito', 'Corleone', '0778252525', 50)

der.changes()

# while wer.balance >= n:
#     der.changes()


