# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod  # abc stands for abstract class. A module for implementing abcs.


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):

    def go(self):
        print("You drive the car")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")


car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()








