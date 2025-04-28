from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def move(self):
        print("Car is moving on the road")

class Plane(Transport):
    def move(self):
        print("Plane is flying in the sky")

car = Car()
plane = Plane()
car.move()
plane.move()

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата {amount} через Credit Card")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата {amount} через PayPal")

card = CreditCard()
paypal = PayPal()
card.pay(1000)
paypal.pay(500)

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(10, 20)

print("Площадь круга:", circle.area())
print("Площадь прямоугольника:", rectangle.area())

class OutputDevice(ABC):
    @abstractmethod
    def display(self, text):
        pass

class Monitor(OutputDevice):
    def display(self, text):
        print(f"[Monitor] {text}")

class Printer(OutputDevice):
    def display(self, text):
        print(f"[Printer] {text}")

monitor = Monitor()
printer = Printer()

monitor.display("Hello, world!")
printer.display("Hello, world!")

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу!")

dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        return 5000

class Manager(Employee):
    def calculate_salary(self):
        return 7000

dev = Developer()
man = Manager()

print("Зарплата разработчика:", dev.calculate_salary())
print("Зарплата менеджера:", man.calculate_salary())

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Подключение к MySQL")

    def disconnect(self):
        print("Отключение от MySQL")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Подключение к PostgreSQL")

    def disconnect(self):
        print("Отключение от PostgreSQL")

mysql = MySQLDatabase()
postgres = PostgreSQLDatabase()

mysql.connect()
mysql.disconnect()

postgres.connect()
postgres.disconnect()
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def move(self):
        print("Car is moving on the road")

class Plane(Transport):
    def move(self):
        print("Plane is flying in the sky")

car = Car()
plane = Plane()
car.move()
plane.move()

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата {amount} через Credit Card")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата {amount} через PayPal")

card = CreditCard()
paypal = PayPal()
card.pay(1000)
paypal.pay(500)

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(10, 20)

print("Площадь круга:", circle.area())
print("Площадь прямоугольника:", rectangle.area())

class OutputDevice(ABC):
    @abstractmethod
    def display(self, text):
        pass

class Monitor(OutputDevice):
    def display(self, text):
        print(f"[Monitor] {text}")

class Printer(OutputDevice):
    def display(self, text):
        print(f"[Printer] {text}")

monitor = Monitor()
printer = Printer()

monitor.display("Hello, world!")
printer.display("Hello, world!")

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу!")

dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        return 5000

class Manager(Employee):
    def calculate_salary(self):
        return 7000

dev = Developer()
man = Manager()

print("Зарплата разработчика:", dev.calculate_salary())
print("Зарплата менеджера:", man.calculate_salary())

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Подключение к MySQL")

    def disconnect(self):
        print("Отключение от MySQL")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Подключение к PostgreSQL")

    def disconnect(self):
        print("Отключение от PostgreSQL")

mysql = MySQLDatabase()
postgres = PostgreSQLDatabase()

mysql.connect()
mysql.disconnect()

postgres.connect()
postgres.disconnect()
