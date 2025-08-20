# Polymorphism:
# Enables objects of different classes to be treated through a common interface,
# with methods having the same name behaving differently based on the object.

class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def lets_fly(obj):
    obj.fly()

b = Bird()
a = Airplane()

lets_fly(b)  # Bird is flying
lets_fly(a)  # Airplane is flying
