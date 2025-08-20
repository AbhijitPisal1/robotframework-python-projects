# Method Overloading:
# Python does not support true method overloading but achieves similar effect
# using default arguments or *args to handle multiple method signatures.

class MathOps:
    def add(self, a, b, c=0):
        return a + b + c

m = MathOps()
print(m.add(2, 3))       # 5
print(m.add(2, 3, 4))    # 9
