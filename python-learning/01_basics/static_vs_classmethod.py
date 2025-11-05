class Toy:
    toys_created = 0  # class variable shared by all dogs

    def __init__(self, name, age):
        self.name = name     # instance variable
        self.age = age
        Toy.toys_created += 1

    # 1️⃣ Instance method — works with *one* specific dog
    def bark(self):
        print(f"{self.name} says woof!")

    # 2️⃣ Class method — works with *the whole class*
    @classmethod
    def total_toys(cls):
        print(f"We have created {cls.toys_created} toys so far.")

    # 3️⃣ Static method — just a helper (no access to dog or class)
    @staticmethod
    def is_puppy(age):
        return age < 1

        
d1 = Toy("Buddy", 2)
d2 = Toy("Charlie", 0.5)

# Instance method → uses self (each dog)
d1.bark()        # Buddy says woof!
d2.bark()        # Charlie says woof!

# Class method → uses cls (the whole class)
Dog.total_toys() # We have created 2 toys so far.

# Static method → plain helper function
print(Toy.is_puppy(0.5))  # True
print(Toy.is_puppy(2))    # False


"""
Kind                    What it touches        What it’s good for                        Real example
Instance (self)        One object              Regular behavior                          Deposit, bark, send email
Class (cls)            Whole class             Alternate constructor, shared counters    from_json(), from_db(), total users
Static (none)          Nothing                 Helper / utility                          Validate input, math ops, format strings
"""
