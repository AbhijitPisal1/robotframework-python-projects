class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} is moving at {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def car_info(self):
        print(f"{self.brand} | {self.speed} km/h | {self.fuel_type}")

class Bike(Vehicle):
    def __init__(self, brand, speed, cc):
        super().__init__(brand, speed)
        self.cc = cc

    def bike_info(self):
        print(f"{self.brand} | {self.speed} km/h | {self.cc}cc")


# Usage
c = Car("Toyota", 180, "Petrol")
b = Bike("Yamaha", 120, 150)

c.move()
c.car_info()

b.move()
b.bike_info()


"""
Inheritance – "Avoid code repetition"

Inheritance allows one class to inherit the properties and behavior of another class. For example, both a Car and a Bike are types of Vehicles — they share movement, speed, and brand but differ in fuel type or engine capacity.

This avoids writing the same code in multiple places and makes the code more modular. Changes to the parent class automatically apply to all children, reducing maintenance.

It's used when multiple objects have similar functionality but also require specific custom behavior.
"""