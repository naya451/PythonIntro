import math 

class Triangle:
    a = 0
    b = 0
    c = 0
    ex = False
    def __init__(self, x, y, z):
        self.a = float(x)
        self.b = float(y)
        self.c = float(z)
        if (x <= 0 or y <= 0 or z <= 0):
            self.ex = False
            return
        if (x + y <= z or x + z <= y or y + z <= x):
            self.ex = False
            return

        self.ex = True            

    def __abs__(self):
        if self.ex:
            p = (self.a + self.b + self.c) / 2
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        else:
            return 0
    
    def __eq__(self, other):
        return all([math.isclose(s, o) for s, o in zip(sorted([self.a, self.b, self.c]), sorted([other.a, other.b, other.c]))])
        

    def __str__(self):
        return str(self.a) + ':' + str(self.b) + ':' + str(self.c)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def __bool__(self):
        return self.ex


