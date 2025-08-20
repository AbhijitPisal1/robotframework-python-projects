# Abstraction:
# Hides complex implementation details and shows only essential features using abstract base classes.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")

# Usage
car = Car()
motorcycle = Motorcycle()
car.start_engine()
motorcycle.start_engine()
