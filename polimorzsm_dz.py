# 1. Универсальный принтер
import math

class Document:
    def print_info(self):
        pass

class PDFDocument(Document):
    def print_info(self):
        print("Это PDF документ.")

class WordDocument(Document):
    def print_info(self):
        print("Это Word документ.")

def print_document_info(doc):
    doc.print_info()

pdf = PDFDocument()
word = WordDocument()

documents = [pdf, word]

for doc in documents:
    print_document_info(doc)


# 2. Животные говорят

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу!")

class Cow(Animal):
    def make_sound(self):
        print("Муу!")

def make_animals_talk(animals):
    for animal in animals:
        animal.make_sound()

animals = [Dog(), Cat(), Cow()]

make_animals_talk(animals)


# 3. Игрушки

class Toy:
    def play_sound(self):
        pass

class Car(Toy):
    def play_sound(self):
        print("Врум-врум!")

class Doll(Toy):
    def play_sound(self):
        print("Кукла издает звук!")

class Drum(Toy):
    def play_sound(self):
        print("Барабан бьет!")

toys = [Car(), Doll(), Drum()]

for toy in toys:
    toy.play_sound()


# 4. Фигуры и площадь

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(5), Rectangle(10, 20), Triangle(10, 5)]

for shape in shapes:
    print(f"Площадь: {shape.area()}")


# 5. Банкомат

class Card:
    def withdraw(self, amount):
        pass

class CreditCard(Card):
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Баланс кредитной карты после снятия: {self.balance}")

class DebitCard(Card):
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств на дебетовой карте!")
        else:
            self.balance -= amount
            print(f"Баланс дебетовой карты после снятия: {self.balance}")
