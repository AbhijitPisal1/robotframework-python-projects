# Inheritance:
# Allows a class (child) to inherit attributes and methods from another class (parent),
# enabling code reuse and method overriding for customized behavior.

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Usage
dog = Dog()
cat = Cat()
dog.speak()  # Dog barks
cat.speak()  # Cat meows
