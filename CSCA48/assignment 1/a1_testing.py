# test add
# test add w/ string
# test add w/ identity
# test add w/ square
# test add w/ vector
# test sub
# test sub w/ string
# test sub w/ identity
# test sub w/ square
# test sub w/ vector
# test mul
# test mul w/ string
# test mul w/ identity
# test mul w/ square
# test mul w/ vector
# test swap Row and Column
# test swap with Identity
# test transpose
# test transpose vector
# test setDiagonal
# test Determinent
# test symmetry
# test Identity
# test get/set of vector
import a1_design as a1
import unittest


class TestMatrix(unittest.TestCase):

    def test_add(self):
        # creates matrices to add
        m1 = a1.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m2 = a1.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m = m1 + m2

        # expected return from new matrix
        key = [2, 4, 6, 8, 10, 12, 14, 16, 18]
        test = []

        # gets added values
        for a in range(0, 3):
            for b in range(0, 3):
                test += m.getVal(a, b)

        # checks and returns message
        self.assertEqual(key, test, 'added wrong')

    def test_add_string(self):
        # creates matrices again except with letters
        m1 = a1.Matrix([['a', 'b', 3], [4, 5, 6], [7, 8, 9]])
        m2 = a1.Matrix([[1, 2, 'c'], [4, 5, 6], [7, 8, 9]])
        m = m1 + m2

        # checks only the first row as only the first row have letters
        key = ['a+1', 'b+1', 'c+1']
        test = []

        # gets value
        for a in range(0, 3):
            test += m.getVal(0, a)

        # checks
        self.assertEqual(key, test, 'adding incompatible with words')

    def test_sub(self):
        # creates matrices and then subtracts
        m1 = a1.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m2 = a1.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m = m1 - m2

        # expected result
        key = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        test = []

        # grabs values
        for a in range(0, 3):
            for b in range(0, 3):
                test += m.getVal(a, b)

        self.assertEqual(key, test, 'Not subtracted properly')

    def test_mul(self):
        # creates matrices and then multiplies
        m1 = a1.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m2 = a1.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m = m1 * m2

        # create key to check
        key = [30, 36, 42, 66, 81, 96, 102, 126, 150]
        test = []

        # gets values
        for a in range(0, 3):
            for b in range(0, 3):
                test += m.getVal(a, b)

        self.assertEqual(key, test, 'Not multiplied properly')

    def test_get_Row(self):
        # creates matrix and gets a row
        m = a1.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        test = m.getRow(0)
        key = [1, 2, 3]

        # checks
        self.assertEqual(key, test, 'did not get the Row')

    def test_set_Row(self):
        # creates matrix and swaps rows
        m = a1.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        # sets row
        m.setRow(0, [9, 9, 9])
        key = [9, 9, 9]

        # gets values
        test = []
        for a in range(0, 3):
            test += m.getVal(0, a)

        # checks
        self.assertEqual(key, test, 'did not set the row')

    def test_get_Col(self):
        # creates matrix and gets a col
        m = a1.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        test = m.getCol(0)
        key = [1, 4, 7]

        # checks
        self.assertEqual(key, test, 'did not get the column')

    def test_set_Col(self):
        # creates matrix and swaps columns
        m = a1.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        # sets column
        m.setCol(0, [9, 9, 9])
        key = [9, 9, 9]

        # gets values
        test = []
        for a in range(0, 3):
            test += m.getVal(a, 0)

        # checks
        self.assertEqual(key, test, 'did not set the column')

    def test_swap_row(self):
        # creates matrix and swaps rows
        m = a1.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m.swapRow(0, 2)

        # expected return
        key = [7, 8, 9, 4, 5, 6, 1, 2, 3]
        test = []

        # gets values and checks
        for a in range(0, 3):
            for b in range(0, 3):
                test += m.getVal(a, b)

        self.assertEqual(test, key, 'Rows not swapped properly')

    def test_swap_col(self):
        # creates matrix and swaps columns
        m = a1.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m.swapCol(0, 2)

        # expected return
        key = [3, 2, 1, 6, 5, 4, 9, 8, 7]
        test = []

        # checks
        for a in range(0, 3):
            for b in range(0, 3):
                test += m.getVal(a, b)

        self.assertEqual(test, key, 'Columns not swapped properly')

    def test_transpose(self):
        # creates and transposes
        m = a1.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m = m.transpose()

        # creates key
        key = [1, 4, 7, 2, 5, 8, 3, 6, 9]
        test = []

        # gets values
        for a in range(0, 3):
            for b in range(0, 3):
                test += m.getVal(a, b)

        # checks
        self.assertEqual(test, key, 'Not transposed properly')


class TestSquare(unittest.TestCase):

    def test_add(self):
        # creates matrices and adds
        m1 = a1.Square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m2 = a1.Square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m = m1 + m2

        # creates key
        key = [2, 4, 6, 8, 10, 12, 14, 16, 18]
        test = []

        # gets values
        for a in range(0, 3):
            for b in range(0, 3):
                test += m.getVal(a, b)

        # checks
        self.assertEqual(key, test, 'added wrong')

    def test_sub(self):
        # creates matrices and subtracts
        m1 = a1.Square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m2 = a1.Square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m = m1 - m2

        # creates key
        key = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        test = []

        # gets values
        for a in range(0, 3):
            for b in range(0, 3):
                test += m.getVal(a, b)

        # checks
        self.assertEqual(key, test, 'Not subtracted properly')

    def test_mul(self):
        # creates matrices and multiplies
        m1 = a1.Square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m2 = a1.Square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m = m1 * m2

        # creates key
        key = [30, 36, 42, 66, 81, 96, 102, 126, 150]
        test = []

        # gets values
        for a in range(0, 3):
            for b in range(0, 3):
                test += m.getVal(a, b)

        # checks
        self.assertEqual(key, test, 'Not multiplied properly')

    def test_set_diagonal(self):
        # creates matrix and sets Diagonal
        m = a1.Square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m.setDiagonal([0, 0, 0])

        # creates key
        key = [0, 0, 0]
        test = []

        # checks
        for a in range(0, 3):
            test += m.getVal(a, a)

        # checks
        self.assertEqual(key, test, 'Diagonal not set')

    def test_get_Diagonal(self):
        # creates matrix and gets Diagonal
        m = a1.Square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        # grabs diagonal
        check = m.getDiagonal()
        key = [1, 5, 9]

        # checks
        self.assertEqual(key, check, 'did not get expected')

    def test_determinent(self):
        # creates matrix
        m = a1.Square([1, 2], [3, 4])

        # gets answer
        key = 10
        test = m.determinent()

        # compares to expected
        self.assertEqual(key, test, 'Failed value')

    def test_symmetry(self):
        # creates array
        m = a1.Square([[1, 2, 3], [0, 5, 6], [0, 0, 9]])

        # creates symmetry
        m.createSymmetry()

        # creates key
        key = [1, 2, 3, 2, 5, 6, 3, 6, 9]
        test = []

        # get values
        for a in range(0, 3):
            for b in range(0, 3):
                test += m.getVal(a, b)

        # checks
        self.assertEqual(key, test, 'Symmetry not achieved')


class TestIdentity(unittest.TestCase):

    def test_create(self):
        # creates key of expected number
        # the 5's represent the diagonal, the 0 is some spot not on diagonal
        key = [5, 5, 5, 5]
        m = a1.Identity(4, 5)
        test = []

        # gets values
        for i in range(0, 4):
            test += m.getVal(i, i)

        # gets a value that should be empty
        test += m.getVal(0, 3)

        # checks
        self.assertEqual(key, test, 'not an identity')


class TestVector(unittest.TestCase):

    def test_set(self):
        # creates a vector
        m = a1.Vector([0, 1])

        # sets value and key
        m.setVal(0, 5)
        key = [5, 1]
        test = [m.getVal(0), m.getVal(1)]

        # checks
        self.assertEqual(key, test, 'not set')

    def test_get(self):
        # creates array and checks
        m = a1.Vector([16, 7])
        self.assertEqual(m.getVal(1), 7, 'not retrieved')

    def test_add(self):
        # creates vectors
        m1 = a1.Vector([1, 2, 3])
        m2 = a1.Vector([1, 2, 3])

        # adds and gets keys
        m = m1 + m2
        key = [2, 4, 6]
        test = []

        # gets values
        for a in range(0, 3):
            test += m.getVal(a)

        # checks
        self.assertEqual(key, test, 'not added properly')

    def test_sub(self):
        # creates vectors
        m1 = a1.Vector([1, 2, 3])
        m2 = a1.Vector([1, 2, 3])

        # subtracts vectors and creates keys
        m = m1 - m2
        key = [0, 0, 0]
        test = []

        # gets values
        for a in range(0, 3):
            test += m.getVal(a)

        # checks
        self.assertEqual(key, test, 'not subtracted properly')

    def test_mul(self):
        # creates vectors
        m1 = a1.Vector([1, 2, 3])
        m2 = a1.Vector([1, 2, 3])

        # multiplies vectors
        m = m1 * m2
        key = 14

        # checks
        self.assertEqual(m, key, 'not multiplied properly')

unittest.main()
