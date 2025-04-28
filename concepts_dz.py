class BankAccount:
    def __init__(self):
        self.__balance = 0  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Баланс пополнен на {amount} сом')

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'Вы сняли {amount} сом')
        else:
            print('Недостаточно средств')

    def get_balance(self):
        return self.__balance


client = BankAccount()
client.deposit(1000)
client.withdraw(500)
print(client.get_balance())

print('---------------------------')

# 2. Класс User
class User:
    def __init__(self, name):
        self.name = name
        self.__password = "ne_znyau17"  # приватный пароль

    def get_password(self):
        return '*' * len(self.__password)

    def set_password(self, new_password):
        if len(new_password) > 6:
            self.__password = new_password


account = User('Faha')
print(account.name)
print(account.get_password())
account.set_password('faha2009')
print(account.get_password())

print('---------------------------')

# 3. Класс Employee
class Employee:
    def __init__(self, salary, name):
        self.__salary = salary  # приватное свойство
        self.name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 30000:
            self.__salary = salary


warrior = Employee(30000, 'Faha')
warrior.set_salary(10000)  # зарплата не обновится, так как 10000 < 30000
print(warrior.get_salary())

print('---------------------------')

# 4. Классы Circle и Cylinder
from math import pi

class Circle:
    def __init__(self, radius):
        self._radius = None
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            print("Радиус не может быть меньше или равен нулю!")

    def area(self):
        return pi * self._radius ** 2


class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self._height = None
        self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print('Высота не может быть меньше или равна нулю!')


krug = Circle(10)
print(krug.area())    # площадь круга
print(krug.radius)    # радиус круга

print('---------------------------')

cylinder = Cylinder(5, 7)
print(cylinder.radius)  # ➤ 5
print(cylinder.height)  # ➤ 7
print(cylinder.area())