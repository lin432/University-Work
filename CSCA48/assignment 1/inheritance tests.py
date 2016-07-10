class Person():
    def __init__(self, i):
        self.i = i

    def ret(self):
        return self.operation()

    def operation(self):
        return 6

class Worker(Person):
    def __init__(self):
        Person.__init__(self,5)

    def operation(self):
        return 999

    def raise_Error(self):
        val = 'got row:' + str(5) + ' max row:' + str(4)
        val = val + ' got col:' + str(5) + ' max col:' + str(4)
        raise MatrixIndexError(val)
        
class MatrixIndexError(Exception):
    '''An attempt has been made to access an invalid index in this matrix'''
    def __init__(self, value):
        self.message = 'An attempt has been made to access an invalid index'
        self.message = self.message + 'in this matrix' + str(value)
    def __str__(self):
        return repr(self.message)
class MatrixDimensionError(Exception):
    '''An attempt has been made to perform an operation on this matrix which
    is not valid given its dimensions'''
    def __init__(self, value):
        self.message = 'An attempt has been made to perform an operation on'
        self.message = self.message + 'this matrix which is not valid given'
        self.message = self.message + 'its dimensions ' + str(value)
    def __str__(self):
        return repr(self.message)

class MatrixInvalidOperationError(Exception):
    '''An attempt was made to perform an operation on this matrix which is
    not valid given its type'''
    def __init__(self, value):
        self.message = 'An attempt was made to perform an operation on'
        self.message = self.message + 'this matrix which is not valid given'
        self.message = self.message + 'its type '
    def __str__(self):
        return repr(self.message)

m = Worker()

