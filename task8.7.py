class ComplexNum:
    def __init__(self, a, b):
        self.x = complex(a, b)

    def __add__(self, other):
        return self.x + other.x

    def __mul__(self, other):
        return self.x * other.x


c1 = ComplexNum(1, 2)
c2 = ComplexNum(3, 4)
c3 = c1 + c2
c4 = c1 * c2
print(c3)
print(c4)
