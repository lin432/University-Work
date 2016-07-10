# unittests
# jpg/pdf/png uml diagram


class Matrix():
    '''A representation of a mathematical matrix
       with support for addition, multiplication, subtraction
       and some basic matrix operations
    '''

    def __init__(self, matrix, b=None):
        '''
        (Matrix, list of list of objects or int, int) -> None
        Creates a matrix object based on whether the matrix input
        is a premade nested list with objects representing numbers or
        a and b representing the dimensions of the matrix to be created
        '''
        self._matrix = None

        if(type(matrix) == int):
            pass
        else:
            pass

        pass

    def __add__(self, a, b):
        '''
        (Matrix, Matrix, Matrix) -> Matrix
        adds the two matrixes based on matrix rules
        if there is a string then it creates
        string + num
        '''
        pass

    def __sub__(self, a, b):
        '''
        (Matrix, Matrix, Matrix) -> Matrix
        subtracts matrices, a-b by matrix properties
        if there is a string then it creates string-num
        '''
        pass

    def __mul__(self, a, b):
        '''
        (Matrix, Matrix, Matrix) -> Matrix
        Multiplies a*b following matrix multiplication
        rules, if given string attempts to simplify into
        num*string + num
        '''
        pass

    def __str__(self):
        '''
        (Matrix) -> string
        prints a string representation of the matrix
        '''
        pass

    def getVal(self, row, col):
        '''
        (Matrix, int, int) -> object
        returns the object at the location of the matrix
        '''
        pass

    def setVal(self, row, col, value):
        '''
        (Matrix, int, int, object) -> None
        changes the object at the location of the matrix
        '''
        pass

    def getRow(self, row):
        '''
        (Matrix, int) -> list of objects
        retrieves a row of the matrix
        '''
        pass

    def setRow(self, row, values):
        '''
        (Matrix, int, list of objects) -> None
        sets a row of the matrix
        '''

    def getCol(self, col):
        '''
        (Matrix, int) -> list of objects
        retrieves a column of object
        '''

    def setCol(self, col, values):
        '''
        (Matrix, int, list of objects) -> None
        sets a column of the matrix
        '''

    def swapRow(self, a, b):
        '''
        (Matrix, int, int) -> None
        switches the rows a <-> b
        '''
        pass

    def swapCol(self, a, b):
        '''
        (Matrix, int, int) -> None
        switches the columns a<->b
        '''
        pass

    def transpose(self):
        '''
        (Matrix) -> Matrix
        return the transpose of the current Matrix
        '''
        pass


class Square(Matrix):
    '''
    A class representation of a square matrix taking
    basic operational methods from Matrix class
    '''

    def __init__(self, matrix):
        '''
        (Square, list of list of objects or int) -> None
        creates a square object based on a properly formatted
        premade matrix or creates one based on int as the
        dimensions of the matrix.

        REQ: matrix be a list of size n filled with list of size n
        '''
        pass

    def setDiagonal(self, values):
        '''
        (Square, list of objects) -> None
        replaces the diagonal of the matrix with the values
        of the list.

        REQ: len(values) == len(self._matrix)
        '''
        pass

    def getDiagonal(self):
        '''
        (Square) -> list of objects
        returns a list of the objects diagonal (top-left -> bottom-right)
        in the matrix
        '''
        pass

    def determinent(self):
        '''
        (Square) -> object
        returns the determinent of the matrix

        REQ: len(self._matrix) == 2 and len(self._matrix[0]) == 2
        '''
        pass

    def createSymmetry(self):
        '''
        (Square) -> None
        mirrors the matrix based on the area with most non-zero values
        '''
        pass


class Identity(Square):
    '''
    A class representation of an Identity matrix
    '''

    def __init__(self, size, val):
        '''
        (Identity, int, object) -> None
        creates and identity matrix based on the size
        of the square matrix and the value to fill
        the diagonal
        '''
        pass


class Vector(Matrix):
    '''
    A class representation of Vector or row/col matrix
    '''

    def __init__(self, matrix, row=True):
        '''
        (Vector, list of objects, bool) -> None
        creates a vector object based on a list of objects
        the bool represents whether this vector lies on a row
        or on a column
        '''
        self._base = 0
        self._row = row
        pass

    def getVal(self, n):
        '''
        (Vector, int) -> object
        returns the object at that position in the list
        '''
        pass

    def setVal(self, n, value):
        '''
        (Vector, int, object) -> None
        set the Vector at the position into the value
        '''
        pass
