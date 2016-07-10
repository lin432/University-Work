import math


class Parallelogram():
    '''a representation of a parallelogram
       with methods to do the calculations of
       a parallelogram
    '''
    def __init__(self, base, side, deg):
        '''
        (Parallelogram, float, float, float) -> NoneType
        Creates a parallelogram object
        '''
        self._type = "Parallelogram"
        self._base = float(base)
        self._side = float(side)
        self._deg = float(deg)

    def area(self):
        '''
        (Parallelogram) -> float
        calculates and returns the area of the parallelogram
        based on the values inside the parallelogram
        '''
        sin = math.sin(math.radians(self._deg))
        return self._base * self._side * sin

    def bst(self):
        '''
        (Parallelogram) -> list of float
        returns a list of the properties: base, side, deg in that order
        as a list
        '''
        return[self._base, self._side, self._deg]

    def __str__(self):
        '''
        (Parallelogram) -> string
        returns a string representation of a parallelogram
        '''
        return "I am a " + self._type + " with area " + str(self.area())


class Rectangle(Parallelogram):
    '''a class that represents a Rectangle'''
    def __init__(self, base, side):
        '''
        (Rectangle, float, float) -> NoneType
        creates a Rectangle object
        '''
        self._type = "Rectangle"
        self._base = float(base)
        self._side = float(side)
        self._deg = 90.0


class Rhombus(Parallelogram):
    ''' a class that represents a rhombus'''
    def __init__(self, base, deg):
        '''
        (Rhombus, float, float) -> NoneType
        creates a Rhombus object
        '''
        self._type = "Rhombus"
        self._base = float(base)
        self._side = float(base)
        self._deg = float(deg)


class Square(Rectangle, Rhombus):
    ''' a class that represents a square'''
    def __init__(self, base):
        '''
        (Square, float) -> NoneType
        creates a rectangle object
        '''
        self._type = "Square"
        self._base = base
        self._side = base
        self._deg = 90.0
