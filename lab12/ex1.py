class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


person1 = Person("Alice", 25)
print(person1.introduce())


# Class vs. Instance Variables
class Employee:
    company = "TechCorp"

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def details(self):
        return f"{self.name} works as a {self.position} at {self.company}."


e1 = Employee("Bob", "Developer")
print(e1.details())


# Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount}. New balance: {self.__balance}"

    def get_balance(self):
        return self.__balance


account = BankAccount("Charlie", 500)
print(account.deposit(200))
print(account.get_balance())


# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())


# Polymorphism
class Bird:
    def fly(self):
        return "Birds can fly."


class Penguin(Bird):
    def fly(self):
        return "Penguins can't fly."


bird = Bird()
penguin = Penguin()
print(bird.fly())
print(penguin.fly())

# Abstraction
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "Car engine started!"


car = Car()
print(car.start_engine())


# Method Overriding
class Parent:
    def show(self):
        return "Parent class method"


class Child(Parent):
    def show(self):
        return "Child class method"


c = Child()
print(c.show())


# Multiple Inheritance
class A:
    def method_a(self):
        return "Method A"


class B:
    def method_b(self):
        return "Method B"


class C(A, B):
    pass


c = C()
print(c.method_a())
print(c.method_b())
