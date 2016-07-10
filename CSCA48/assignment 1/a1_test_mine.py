from a1 import *
def pr_row(M):
    row = M._head.get_down()
    while(row is not None):
        curr = row.get_right()
        while(curr is not None):
            print(curr.get_contents(), curr.get_row(), curr.get_col())
            curr = curr.get_right()
        row = row.get_down()

def pr_col(M):
    col = M._head.get_right()
    while(col is not None):
        curr = col.get_down()
        while(curr is not None):
            print(curr.get_contents(), curr.get_row(), curr.get_col())
            curr = curr.get_down()
        col = col.get_right()

M = Matrix(3,3)
# just method testing
head = M._head
# check add to end works
for a in range(0,2):
    head.add_down(MatrixNode(a))

for a in range(1,3):
    head.add_right(MatrixNode(a))

a = MatrixNode(5)
# test set_col/row
a.set_col(head.get_right())
a.set_row(head.get_down())
# test get_col/row
print(a.get_col(), a.get_row())
# test add from row/column
head.get_down().add_right(a)
head.get_right().add_down(a)
print(head.get_down().get_right().get_contents(), head.get_right().get_down().get_contents())
print('MatrixNode tests succesful\n')

M = Matrix(3,3)
# hardcoded cell setup
row = MatrixNode(2)
col = MatrixNode(2)
a = MatrixNode(12)
a.set_row(row)
a.set_col(col)
row.set_right(a)
col.set_down(a)
M._head.set_right(col)
M._head.set_down(row)
print('created Matrix')

print('Matrix methods test below')
print(M.in_bounds(0,0), M.in_bounds(6,6))
print('test find row/col')
print(M._find_row(0), M._find_col(0))
print(M._find_row(1), M._find_col(1))
print(M._find_row(2), M._find_col(2))
print('cleared finding row/col')
a = M._head.get_down().get_right()
print(a.get_contents(), a.get_row(), a.get_col())
a = M._get_cell(2,2)
print(a.get_contents(), a.get_row(), a.get_col())
print(M._get_cell(1,2))
print('found cell check')

# checking default remove
M.set_val(2,2, 0)

print('checking values')
row = M._head.get_down()
while(row is not None):
    curr = row.get_right()
    while(curr is not None):
        print(curr.get_contents(), curr.get_row(), curr.get_col())
        curr = curr.get_right()
    row = row.get_down()

'''
print('trying _add_row and _add_col')
a = MatrixNode(5)
M._add_to_row(1,2,a)
M._add_to_col(1,2,a)
a = MatrixNode(4)
M._add_to_row(2,2,a)
M._add_to_col(2,2,a)

print('checking values')
row = M._head.get_down()
while(row is not None):
    curr = row.get_right()
    while(curr is not None):
        print(curr.get_contents(), curr.get_row(), curr.get_col())
        curr = curr.get_right()
    row = row.get_down()
'''
M = Matrix(3,3)
print('setting values') # fix set_val
M.set_val(0,0, 11)
M.set_val(0,1, 22)
M.set_val(0,2, 33)
M.set_val(1,0, 44)
M.set_val(1,1, 55)
M.set_val(1,2, 66)
M.set_val(2,0, 77)
M.set_val(2,1, 88)
M.set_val(2,2, 99)

print('checking values')
row = M._head.get_down()
while(row is not None):
    curr = row.get_right()
    while(curr is not None):
        print(curr.get_contents(), curr.get_row(), curr.get_col())
        curr = curr.get_right()
    row = row.get_down()

print('removing some values')
M._remove(2,2)
M._remove(1,2)
M._remove(0,1)

print('trying to get all objects')
print(M.get_val(0,0))
print(M.get_val(0,1))
print(M.get_val(0,2))
print(M.get_val(1,0))
print(M.get_val(1,1))
print(M.get_val(1,2))
print(M.get_val(2,0))
print(M.get_val(2,1))
print(M.get_val(2,2))
print('got all objects')

# checking row removal
M._remove(0,2)
M._remove(0,0)
# checking col removal
M._remove(1,2)

print('checking values from row after row/col removal test')
print(M._head.get_right().get_down().get_contents())
pr_row(M)

print('checking values from col after row/col removal test')
pr_col(M)

# begin Vector tests
print('beginning vector tests')
V = OneDimensionalMatrix(3)
print(len(V))
print(V.get_next_item())
print(V.get_item(0))
print(V.set_item(1, 5))
print(V.get_item(0))
print(V.get_next_item())
curr = V.get_next_item()
print(V.get_index(curr))
print('clear OneDimensionalMatrix methods')

# begin methods with OneDimensionalVectors
V = M.get_row(0)
print(V.get_item(0),V.get_item(1),V.get_item(2))
V = M.get_row(1)
print(V.get_item(0),V.get_item(1),V.get_item(2))
V = M.get_row(2)
print(V.get_item(0),V.get_item(1),V.get_item(2))
print('testing set_row')
M.set_row(0, V)
V = M.get_row(0)
print(V.get_item(0),V.get_item(1),V.get_item(2))
M.set_row(1, V)
M.set_row(2, V)
V = M.get_row(2)
print(V.get_item(0),V.get_item(1),V.get_item(2))
V = OneDimensionalMatrix(3)
print(V.get_item(0),V.get_item(1),V.get_item(2))
M.set_row(0, V)
V = M.get_row(0)
print(V.get_item(0),V.get_item(1),V.get_item(2))
print('testing get/set _ col')
V = M.get_col(0)
print(V.get_item(0),V.get_item(1),V.get_item(2))
V = M.get_col(1)
print(V.get_item(0),V.get_item(1),V.get_item(2))
V = M.get_col(2)
print(V.get_item(0),V.get_item(1),V.get_item(2))
print('test set')
V.set_item(0,2)
V.set_item(1,4)
V.set_item(2,8)
M.set_col(2, V)
V = M.get_col(2)
print(V.get_item(0),V.get_item(1),V.get_item(2))
M.set_col(0, V)
V = M.get_col(0)
print(V.get_item(0),V.get_item(1),V.get_item(2))
V = OneDimensionalMatrix(3)
M.set_col(1,V)
V = M.get_col(1)
print(V.get_item(0),V.get_item(1),V.get_item(2))
print('clear set/get row/col')

print('\ntesting swaps')
print('checking values before')
V = OneDimensionalMatrix(3)
V.set_item(2, 5)
V.set_item(0, 3)
M.set_col(0, V)

pr_row(M)
print()
pr_col(M)
M.swap_rows(0,2)
print('checking values after 0-2')
pr_row(M)
print()
pr_col(M)

print('trying a swap of Null row')
V = OneDimensionalMatrix(3)

M.set_row(1, V)
print('trying to set a null row before')
pr_row(M)
print()
pr_col(M)
M.swap_cols(0, 2)
print('checking values of col')
pr_col(M)
print('checking values of null')
M.swap_cols(0, 1)
pr_col(M)
print('checking values of null')
M.swap_cols(2, 0)
pr_col(M)
print('checking scalar')
M.add_scalar(3)
pr_row(M)
print(M.default)
print('checking subtract')
M.subtract_scalar(3)
pr_row(M)
print(M.default)
print('checking multiply')
M.multiply_scalar(2)
pr_row(M)
print(M.default)
print('reverting')
M.multiply_scalar(0.5)
pr_row(M)
print(M.default)


print('testing matrix matrix methods')
pr_row(M)
A = Matrix(3,3,1)
M = M.add_matrix(A)
pr_row(M)
A = Matrix(3,3, -1)
M = M.add_matrix(A)
pr_row(M)
print('default case passed')
A = Matrix(3, 3)
A.set_val(0,0,1)
A.set_val(0,1,1)
A.set_val(0,2,1)
A.set_val(2,0,1)
A.set_val(2,2,1)
A.set_val(1,1,1)
print('created matrix A')
pr_row(A)
print('trying add')
M = M.add_matrix(A)
pr_row(M)
print('reverting')
A.set_val(0,0,-1)
A.set_val(0,1,-1)
A.set_val(0,2,-1)
A.set_val(2,0,-1)
A.set_val(2,2,-1)
A.set_val(1,1,-1)
M = M.add_matrix(A)
pr_row(M)

print('trying multiply Identity')
A = IdentityMatrix(3)
M = M.multiply_matrix(A)
pr_row(M)

# 5 8 0
# 0 0 0
# 3 2 0

# 2 2 2
# 0 0 0
# 0 0 0

# 10 10 10
# 0 0 0
# 6 6 6
print('trying row')
A = Matrix(3,3)

A.set_val(0,1,2)
A.set_val(0,2,2)
A.set_val(0,0,2)

M = M.multiply_matrix(A)
pr_row(M)
# check swap row and column for circular lists


print('\n\n\nchecking other classes')
print('trying to create the Matrices')
O = OneDimensionalMatrix(3, 5)
S = SquareMatrix(3, 5)
Sym = SymmetricMatrix(3, 5)
D = DiagonalMatrix(3, 5)
I = IdentityMatrix(3)
print('created properly')

print('\nplaying with Vector')
try:
    O.set_val(1,2, 3)
except MatrixInvalidOperationError:
    print('pass')

print(I.get_dimensions())
pr_row(O)
pr_row(I)
M = O.multiply_matrix(I)
pr_row(M)
print('testing Square')
S.transpose()
S.set_val(0,2,3)
S.set_val(0,1,4)
S.set_val(2,0,9)
S.set_val(1,1,1)
pr_row(S)
print('transposing')
S.transpose()
pr_row(S)
print('trying to get diagonal')
diagonal = S.get_diagonal()
print(diagonal.get_item(0),diagonal.get_item(1),diagonal.get_item(2))
print('trying to set diagonal')
diagonal = OneDimensionalMatrix(3)
S.set_diagonal(diagonal)
diagonal = S.get_diagonal()
print(diagonal.get_item(0),diagonal.get_item(1),diagonal.get_item(2))

print('testing Diagonal')
D.set_item(2, 3)
pr_row(D)

