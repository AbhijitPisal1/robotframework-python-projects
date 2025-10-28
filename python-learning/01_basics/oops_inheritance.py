class Parent:
    """Represents a parent class with a basic greeting method."""
    
    def greet(self):
        """Return a greeting message from the parent."""
        return "Hello from parent"
        

class Child(Parent):
    """
    Represents a child class inheriting from Parent.
    
    The 'self' parameter refers to the instance of the class,
    allowing access to its attributes and methods.
    """
    
    def greetChild(self):
        """Return a greeting message from the child."""
        return "Hello from child"
    

# Create an instance of Child and call its methods
a = Child()
print(a.greet())        # Uses Parent.greet() directly (no override → no need for super)
print(a.greetChild())


class Parent2:
    """Represents another parent class with a greeting method."""
    
    def greeting(self):
        """Return a greeting message from the parent."""
        return "Hello from parent"
        

class Child2(Parent2):
    """
    Represents a child class inheriting from Parent2 with an overridden greeting.
    """
    
    def __init__(self, title):
        """Initialize Child2 with a title."""
        self.title = title
        
    def greeting(self):
        """
        Return a combined greeting from parent and child using the title.
        
        The 'super()' function is used to call the parent class's method inside
        the overridden version. This allows the child to *extend* the behavior
        instead of completely replacing it.
        
        Here 'super().greeting()' calls the parent's version of greeting().
        Alternatively, you could call it manually with 'Parent2.greeting(self)',
        but 'super()' is preferred since it adapts automatically in multiple
        inheritance or deeper hierarchies.
        """
        return super().greeting() + " hello from " + self.title
        

# Create an instance of Child2 and call its overridden method
b = Child2("Abhijit")
print(b.greeting())
