class MatrixIndexError(Exception):
    '''An attempt has been made to access an invalid index in this matrix'''
    def __init__(self, value):
        self.message = 'An attempt has been made to access an invalid index'
        self.message = self.message + 'in this matrix ' + str(value)

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


class MatrixNode():
    '''A general node class for a matrix'''

    def __init__(self, contents, right=None, down=None):
        '''(MatrixNode, obj, MatrixNode, MatrixNode) -> NoneType
        Create a new node holding contents, that is linked to right
        and down in a matrix
        '''
        self._contents = contents
        self._right = right
        self._down = down
        # added col and row nodes that direct where to find the row and col
        self._col = None
        self._row = None

    def __str__(self):
        '''(MatrixNode) -> str
        Return the string representation of this node
        '''
        return str(self._contents)

    def get_col(self):
        '''(MatrixNode) -> int
        returns the col value indicating the col position of the node

        REQ: self._col = MatrixNode'''
        # since col is a MatrixNode I just go and check for contents
        return self._col.get_contents()

    def get_col_node(self):
        '''(MatrixNode) -> MatrixNode
        returns the col node indicating the col position of the node'''
        return self._col

    def set_col(self, val):
        '''(MatrixNode, int) -> int
        sets the column value of the node'''
        self._col = val

    def set_row(self, val):
        '''(MatrixNode, int) -> int
        set the row value of the node'''
        self._row = val

    def get_row(self):
        '''(MatrixNode) -> str
        returns the row value indicating the row position of the node

        REQ: self._row = MatrixNode'''
        # since row is a MatrixNode I need to get the contents
        return self._row.get_contents()

    def get_row_node(self):
        '''(MatrixNode) -> MatrixNode
        returns the row node indicating the row position of the node'''
        return self._row

    def get_contents(self):
        '''(MatrixNode) -> obj
        Return the contents of this node
        '''
        return self._contents

    def set_contents(self, new_contents):
        '''(MatrixNode, obj) -> NoneType
        Set the contents of this node to new_contents
        '''
        self._contents = new_contents

    def get_right(self):
        '''(MatrixNode) -> MatrixNode
        Return the node to the right of this one
        '''
        return self._right

    def set_right(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set the new_node to be to the right of this one in the matrix
        '''
        self._right = new_node

    def add_right(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Adds the new_node to the right of this node if no node exists
        otherwise places new node to right and gives it it's children
        '''
        # grab the value to the right
        curr = self.get_right()
        if(curr is not None):
            # exists so we need to replace it
            new_node.set_right(curr)
            self.set_right(new_node)
        else:
            # doesn't exist
            self.set_right(new_node)

    def remove_right(self):
        '''(MatrixNode) -> NoneType
        removes the node to the right and replaces it with any children
        the right node has'''
        # checks to see if a right Node exists
        if(self._right is not None):
            # checks for children
            if(self._right._right is not None):
                self.set_right(self._right._right)
            else:
                self.set_right(None)

    def get_down(self):
        '''(MatrixNode) -> MatrixNode
        Return the node below this one
        '''
        return self._down

    def set_down(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set new_node to be below this one in the matrix
        '''
        self._down = new_node

    def add_down(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Adds the new_node to the bottom of this node if no node exists
        otherwise places new node to bottom and gives it it's children

        REQ: new_node.get_right() == None
        REQ: new_node.get_down() == None
        '''
        # grab the value to the right
        curr = self.get_down()
        if(curr is not None):
            # exists so we need to replace it
            new_node.set_down(curr)
            self.set_down(new_node)
        else:
            # doesn't exist
            self.set_down(new_node)

    def remove_down(self):
        '''(MatrixNode) -> NoneType
        removes the node to the bottom and replaces it with any children
        the node below has'''
        # checks whether down exists
        if(self._down is not None):
            # checks for children
            if(self._down._down is not None):
                self.set_down(self._down._down)
            else:
                self.set_down(None)


class Matrix():
    '''A class to represent a mathematical matrix'''

    def __init__(self, m, n, default=0):
        '''(Matrix, int, int, float) -> NoneType
        Create a new m x n matrix with all values set to default
        '''
        self._head = MatrixNode(None)
        # _max_row and _max_col are numbers to check and make sure that
        # the program does not go over the Matrix size
        self._max_row = m
        self._max_col = n
        self.default = default

    def _find_row(self, row_num):
        '''(Matrix, int, MatrixNode) -> MatrixNode
        Helper function that isolates the head where the row starts
        and returns it, if it's not found then it returns None'''
        ret = None
        curr = self._head.get_down()
        # loops until row num is greater
        while(curr is not None and curr.get_contents() < row_num):
            curr = curr.get_down()
        # checks for right row and returns appropriate decision
        if(curr is not None and curr.get_contents() == row_num):
            ret = curr
        return ret

    def _find_col(self, col_num):
        '''(Matrix, int, MatrixNode) -> MatrixNode
        Helper function that isolates the head where the row starts
        and returns it, if it's not found then it returns None'''
        ret = None
        curr = self._head.get_right()
        # loops until col num is greater
        while(curr is not None and curr.get_contents() < col_num):
            curr = curr.get_right()
        # checks for right col and returns appropriate decision
        if(curr is not None and curr.get_contents() == col_num):
            ret = curr
        return ret

    def _get_cell(self, i, j):
        '''(Matrix, int, int) -> MatrixNode
        Returns the cell at the position, if it doesn't exist then it
        returns None

        REQ: self.in_bounds(i, j) == True'''
        ret = None

        # sets curr as first row
        curr = self._head.get_down()
        if(curr is not None):
            # gets row
            curr = self._find_row(i)
            # checks to see if it found the row
            if(curr is not None):

                curr = curr.get_right()
                # searching for the value based on the col value in MatrixNode
                while(curr is not None and curr.get_col() < j):
                    curr = curr.get_right()

                # checks to see if it's found
                if(curr is not None and curr.get_col() == j):
                    ret = curr
                # not found
                else:
                    ret = None
            else:
                ret = None

        return ret

    def _remove(self, i, j):
        '''(Matrix, int, int) -> NoneType
        removes the selected node. this method is to increase efficiency
        This method is private as generally the Matrix will just return
        the default value'''
        # tries to get row
        row = self._find_row(i)
        temp_row = MatrixNode(None)

        if(row is not None):
            temp_row = row
            # recurses till it finds the col value to the right of the
            # current node
            while(row.get_right() is not None and
                  row.get_right().get_col() < j):
                row = row.get_right()

            # checks if they found the node
            if(row.get_right() is not None and row.get_right().get_col() == j):
                row.remove_right()

        # tries to get column
        col = self._find_col(j)
        temp_col = MatrixNode(None)

        if(col is not None):
            temp_col = col
            # recurses till it finds the row value under the current node
            while(col.get_down() is not None and
                  col.get_down().get_row() < i):
                col = col.get_down()

            # checks if program found node
            if(col.get_down() is not None and col.get_down().get_row() == i):
                col.remove_down()

        # uses previously saved temp_row/col values to go through and
        # eliminate any empty row/columns
        if(temp_row.get_right() == None):
            self._remove_row(i)
        if(temp_col.get_down() == None):
            self._remove_col(j)

    def _remove_row(self, i):
        '''(Matrix, int) -> NoneType
        Removes the row indicated as a pointer'''
        # loops and tries to find the row in question
        curr = self._head
        while(curr.get_down() is not None and
              curr.get_down().get_contents() < i):
            curr = curr.get_down()
        # checks if the node was found
        if(curr.get_down() is not None and
           curr.get_down().get_contents() == i):
            curr.remove_down()

    def _remove_col(self, j):
        '''(Matrix, int) -> NoneType
        Removes the col indicated as a pointer'''
        # loops and tries to find the column in question
        curr = self._head
        while(curr.get_right() is not None and
              curr.get_right().get_contents() < j):
            curr = curr.get_right()

        # checks if column was found
        if(curr.get_right() is not None and
           curr.get_right().get_contents() == j):
            curr.remove_right()

    def _add_to_row(self, i, j, cell):
        '''(Matrix, int, MatrixNode) -> NoneType
        a helper method that adds a new cell
        to a row if it exists and if it doesn't
        it creates a new one

        REQ: M(i, cell.get_col()) does not previously exist, that is
             _get_cell(i, j) == None
        REQ: in_bounds(i, j) == True'''
        # tries to find row
        row = self._find_row(i)

        # row is not found so we need to add row
        if(row is None):
            # we need to create a new row as it does not exist
            row = MatrixNode(i)
            # tries to order the row by finding the last row < i
            curr = self._head
            while(curr.get_down() is not None and
                  curr.get_down().get_contents() < i):
                curr = curr.get_down()
            # adds row
            curr.add_down(row)

        # tries to order the values by finding the last cell with col < j
        curr = row
        while(curr.get_right() is not None and curr.get_right().get_col() < j):
            curr = curr.get_right()
        curr.add_right(cell)

        # sets the row node of the cell
        cell.set_row(row)

    def _add_to_col(self, i, j, cell):
        '''(Matrix, int, MatrixNode) -> NoneType
        a helper method that adds a new cell
        to a col if it exists and if it doesn't
        it creates a new one

        REQ: M(cell.get_row(), j) does not previously exist, that is
             _get_cell(i, j) == None
        REQ: in_bounds(i, j) == True'''
        # tries to find column
        col = self._find_col(j)

        # column is not found
        if(col is None):
            # we need to create a new row as it does not exist
            col = MatrixNode(j)
            # tries to order the row by finding the last row < i
            curr = self._head
            while(curr.get_right() is not None and
                  curr.get_right().get_contents() < j):
                curr = curr.get_right()
            # adds row
            curr.add_right(col)

        # tries to order the values by finding the last cell with row < i
        curr = col
        while(curr.get_down() is not None and curr.get_down().get_row() < i):
            curr = curr.get_down()
        curr.add_down(cell)

        # sets the row node of the cell
        cell.set_col(col)

    def in_bounds(self, i, j):
        '''(Matrix, int, int) -> boolean
        returns a true if the value exists in the Matrix'''
        ret = False
        if(i < self._max_row and j < self._max_col and i >= 0 and j >= 0):
            ret = True
        return ret

    def set_val(self, i, j, new_val):
        '''(Matrix, int, int, float) -> NoneType
        Set the value of m[i,j] to new_val for this matrix m
        '''
        # checks if the search is in bounds
        if(self.in_bounds(i, j)):
            # attempts to get cell
            cell = self._get_cell(i, j)
            # cell is found we're done
            if(cell is not None):
                if(new_val == self.default):
                    self._remove(i, j)
                else:
                    cell.set_contents(new_val)
            # cell is not found so we need to add it
            else:
                if(new_val != self.default):
                    # creates cell
                    cell = MatrixNode(new_val)
                    # calls methods to add cell
                    self._add_to_row(i, j, cell)
                    self._add_to_col(i, j, cell)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

    def get_val(self, i, j):
        '''(Matrix, int, int) -> float
        Return the value of m[i,j] for this matrix m
        '''
        # checks if value is in matrix
        if(self.in_bounds(i, j)):
            # tries and find cell
            ret = self._get_cell(i, j)

            # checks if cell is different from default
            if(ret is not None):
                # is so it gets non-default value
                ret = ret.get_contents()
            else:
                ret = self.default

            return ret
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

    def get_row(self, row_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the row_num'th row of this matrix
        '''
        ret = None

        # insures that the row asked for is in the index
        if(self.in_bounds(row_num, 0)):
            # calls recursive helper to get the row asked
            row = self._find_row(row_num)

            # creates a default row
            ret = OneDimensionalMatrix(self._max_col, self.default)

            # None tells us that the row does not exist
            # and as such we just return the default OneDimensionalMatrix
            if(row is not None):
                # moves to first data
                curr = row.get_right()
                # fills OneDimensionalMatrix
                while(curr is not None):
                    ret.set_item(curr.get_col(), curr.get_contents())
                    curr = curr.get_right()
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

        return ret

    def set_row(self, row_num, new_row):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the row_num'th row of this matrix to those of new_row
        '''
        # checks that the row to be set is in bounds
        if(new_row is not None):
            if(self.in_bounds(row_num, len(new_row) - 1)):
                if(self.default == new_row.default):
                    # has to delete everything the row first
                    row = self._find_row(row_num)
                    while(row is not None and row.get_right() is not None):
                        curr = row.get_right()
                        self._remove(row_num, curr.get_col())

                    # gets items from row and puts them in matrix
                    curr = new_row.get_next_item()
                    while(curr is not None):
                        self.set_val(row_num, new_row.get_index(curr),
                                     curr.get_contents())
                        curr = new_row.get_next_item(curr)
                else:
                    i = row_num
                    new_row_values = new_row.get_list()
                    for x in range(0, len(new_row)):
                        self.set_val(i, x, new_row.get_item(x))
            else:
                val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
                val = val + ', got col:' + str(j)
                val = val + ', max col:' + str(self._max_col)
                raise MatrixIndexError(val)
        else:
            # erases row
            row = self._find_row(row_num)
            while(row is not None and row.get_right() is not None):
                curr = row.get_right()
                self._remove(row_num, curr.get_col())

    def get_col(self, col_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the col_num'th column of this matrix
        '''
        ret = None

        # insures that the column asked for is in the index
        if(self.in_bounds(0, col_num)):
            # calls recursive helper to get the row asked
            col = self._find_col(col_num)

            # creates a default row
            ret = OneDimensionalMatrix(self._max_row, self.default)

            # None tells us that the row does not exist
            # and as such we just return the default OneDimensionalMatrix
            if(col is not None):
                # moves to first data
                curr = col.get_down()
                # fills OneDimensionalMatrix
                while(curr is not None):
                    ret.set_item(curr.get_row(), curr.get_contents())
                    curr = curr.get_down()
        else:
            val = 'got col:' + str(col_num)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

        return ret

    def set_col(self, col_num, new_col):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the col_num'th column of this matrix to
        those of new_row '''
        # checks that the column to be set is in bounds
        if(new_col is not None):
            if(self.in_bounds(len(new_col) - 1, col_num)):
                if(self.default == new_col.default):
                    # has to delete everything the col first
                    col = self._find_col(col_num)
                    while(col is not None and col.get_down() is not None):
                        curr = col.get_down()
                        self._remove(curr.get_row(), col_num)

                    # gets items from column and puts them in matrix
                    curr = new_col.get_next_item()
                    while(curr is not None):
                        self.set_val(new_col.get_index(curr),
                                     col_num, curr.get_contents())
                        curr = new_col.get_next_item(curr)
                else:
                    i = col_num
                    new_col_values = new_col.get_list()
                    for x in range(0, len(new_col)):
                        self.set_val(x, i, new_col.get_item(x))
            else:
                val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
                val = val + ', got col:' + str(j)
                val = val + ', max col:' + str(self._max_col)
                raise MatrixIndexError(val)
        else:
            # erases column
            col = self._find_col(col_num)
            while(col is not None and col.get_down() is not None):
                curr = col.get_down()
                self._remove(curr.get_row(), col_num)

    def swap_rows(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of rows i and j in this matrix
        '''
        # checks for index error
        if(i < self._max_row and j < self._max_row):
            i_node = self._find_row(i)
            j_node = self._find_row(j)

            if(i_node is not None):
                # can find both i and j
                if(j_node is not None):
                    # replaces i with j and j with i
                    i_vector = self.get_row(i)
                    self.set_row(i, self.get_row(j))
                    self.set_row(j, i_vector)

                # can find only i
                else:
                    # replaces i in j spot and makes i empty
                    self.set_row(j, self.get_row(i))
                    self.set_row(i, None)

            # can only find j
            elif(j is not None):
                # replace j in i and makes j empty
                self.set_row(i, self.get_row(j))
                self.set_row(j, None)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j) + ', max col:'
            val = val + str(self._max_col)
            raise MatrixIndexError(val)

    def swap_cols(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of columns i and j in this matrix
        '''
        # checks for index error
        if(i < self._max_col and j < self._max_col):
            i_node = self._find_col(i)
            j_node = self._find_col(j)

            if(i_node is not None):
                # can find both i and j
                if(j_node is not None):
                    # replaces i with j and j with i
                    i_vector = self.get_col(i)
                    self.set_col(i, self.get_col(j))
                    self.set_col(j, i_vector)

                # can find only i
                else:
                    # replaces i in j spot and makes i empty
                    self.set_col(j, self.get_col(i))
                    self.set_col(i, None)

            # can only find j
            elif(j is not None):
                # replace j in i and makes j empty
                self.set_col(i, self.get_col(j))
                self.set_col(j, None)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j) + ', max col:'
            val = val + str(self._max_col)
            raise MatrixIndexError(val)

    def add_scalar(self, add_value):
        '''(Matrix, float) -> NoneType
        Increase all values in this matrix by add_value
        '''
        # changes default values
        self.default = self.default + add_value

        # gets first row
        curr_row = self._head.get_down()
        while(curr_row is not None):
            # gets first cell
            curr = curr_row.get_right()
            while(curr is not None):
                # gets cell value and changes it
                val = curr.get_contents()
                curr.set_contents(val + add_value)
                # goes to next cell
                curr = curr.get_right()
            # goes to next row
            curr_row = curr_row.get_down()

    def subtract_scalar(self, sub_value):
        '''(Matrix, float) -> NoneType
        Decrease all values in this matrix by sub_value
        '''
        # changes default values
        self.default = self.default - sub_value

        # gets first row
        curr_row = self._head.get_down()
        while(curr_row is not None):
            # gets first cell
            curr = curr_row.get_right()
            while(curr is not None):
                # gets cell value and changes it
                val = curr.get_contents()
                curr.set_contents(val - sub_value)
                # goes to next cell
                curr = curr.get_right()
            # goes to next row
            curr_row = curr_row.get_down()

    def multiply_scalar(self, mult_value):
        '''(Matrix, float) -> NoneType
        Multiply all values in this matrix by mult_value
        '''
        # changes default values
        self.default = self.default * mult_value

        # gets first row
        curr_row = self._head.get_down()
        while(curr_row is not None):
            # gets first cell
            curr = curr_row.get_right()
            while(curr is not None):
                # gets cell value and changes it
                val = curr.get_contents()
                curr.set_contents(val * mult_value)
                # goes to next cell
                curr = curr.get_right()
            # goes to next row
            curr_row = curr_row.get_down()

    def get_default(self):
        '''(Matrix) -> float
        returns the default value'''
        return self.default

    def get_first_row(self):
        '''(Matrix) -> MatrixNode
        returns the first row'''
        return self._head.get_down()

    def get_first_col(self):
        '''(Matrix) -> MatrixNode
        returns the frist col'''
        return self._head.get_right()

    def get_dimensions(self):
        '''(Matrix) -> (int, int)
        returns the max row,col of the matrix'''
        return (self._max_row, self._max_col)

    def add_matrix(self, adder_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the sum of this matrix and adder_matrix
        '''
        # check dimensions
        if(adder_matrix.get_dimensions() == self.get_dimensions()):
            # create a new matrix
            default = self.default + adder_matrix.get_default()
            M = Matrix(self._max_row, self._max_col, default)

            # gets default for use later
            default = adder_matrix.get_default()

            # get the first row of values
            row_1 = self._head.get_down()
            row_2 = adder_matrix.get_first_row()

            # keeps looping while there still exists both rows
            while(row_1 is not None and row_2 is not None):
                # checks the relationship of the rows
                if(row_1.get_contents() == row_2.get_contents()):
                    # they are equal so we need to consider the case
                    # that some numbers are the same
                    self._add_matrix(M, [row_1, row_2], self.default, default)
                    # iterates
                    row_1 = row_1.get_down()
                    row_2 = row_2.get_down()
                elif(row_1.get_contents() < row_2.get_contents()):
                    # only uses row1
                    self._add_matrix(M, [row_1], default)
                    row_1 = row_1.get_down()
                else:
                    # only uses row2
                    self._add_matrix(M, [row_2], self.default)
                    row_2 = row_2.get_down()

            while(row_1 is not None):
                # only uses row1 since only row_1 exists
                self._add_matrix(M, [row_1], default)
                row_1 = row_1.get_down()

            while(row_2 is not None):
                # only uses row2
                self._add_matrix(M, [row_2], self.default)
                row_2 = row_2.get_down()

            return M
        else:
            val = 'This Matrix dimensions: ' + self.get_dimensions()
            val = val + ', adding matrix dimensions: '
            val = val + adder_matrix.get_dimensions()
            raise MatrixDimensionError(val)

    def _add_matrix(self, M, row_nodes, default1, default2=None):
        '''(Matrix, Matrix, list of MatrixNode, float, float)-> NoneType
        helper method to add_matrix, deals with case
        of list having a length of 1 or 2

        REQ: len(row_node) == 1 or  len(row_node) == 2
        REQ: row_nodes[0] is not None'''
        # case where there is more than one row
        if(len(row_nodes) > 1):
            # gets rows
            row1 = row_nodes[0].get_right()
            row2 = row_nodes[1].get_right()
            row_val = row1.get_row()

            # goes through all the columns
            while(row1 is not None and row2 is not None):
                # checks where the rows are in terms of column
                if(row1.get_col() == row2.get_col()):
                    # same place so we add both together
                    val1 = row1.get_contents()
                    val2 = row2.get_contents()

                    M.set_val(row_val, row1.get_col(), (val1 + val2))
                    # iterates
                    row1 = row1.get_right()
                    row2 = row2.get_right()
                elif(row1.get_col() < row2.get_col()):
                    # row1 is smaller so we add it first
                    val1 = row1.get_contents()
                    # add default of second matrix as well
                    M.set_val(row_val, row1.get_col(), (val1 + default2))
                    row1 = row1.get_right()
                else:
                    # row2 is smaller so we add it first
                    val1 = row2.get_contents()
                    M.set_val(row_val, row2.get_col(), (val1 + default1))
                    row2 = row2.get_right()

            while(row1 is not None):
                # only row1 exists
                val1 = row1.get_contents()
                M.set_val(row_val, row1.get_col(), (val1 + default2))
                row1 = row1.get_right()

            while(row2 is not None):
                # only row2 exists
                val1 = row2.get_contents()
                M.set_val(row_val, row2.get_col(), (val1 + default1))
                row2 = row2.get_right()

        else:
            # only one row was passed
            row = row_nodes[0]
            curr = row.get_right()
            while(curr is not None):
                M.set_val(row.get_contents(),
                          curr.get_col(), (curr.get_contents() + default1))
                curr = curr.get_right()

    def dot_product(self, row1, row2):
        '''(Matrix, OneDimensionalMatrix, OneDimensionalMatrix) -> float
        returns the dotproduct of two vectors, returns zero
        in all other situations'''
        ret = 0
        # goes through all the cells and adds them to total
        # only if the lengths are the same
        if(len(row1) == len(row2)):
            for a in range(0, len(row1)):
                ret = ret + (row1.get_item(a)*row2.get_item(a))
        else:
            val = 'given unequal lengths: ' + len(row1) + ' : ' + len(row2)
            raise MatrixDimensionError(val)

        return ret

    def multiply_matrix(self, mult_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the product of this matrix and mult_matrix
        '''
        M = None
        if(mult_matrix is not None):
            # gets row/col of matrix to multiply
            rows = None
            cols = None
            (rows, cols) = mult_matrix.get_dimensions()
            # check whether this is a valid multiplication
            if(self._max_col == rows):
                # creates matrix
                M = Matrix(self._max_row, cols, self.default)

                # goes through all columns and rows
                for x in range(0, self._max_row):
                    vector1 = self.get_row(x)
                    for y in range(0, cols):
                        vector2 = mult_matrix.get_col(y)
                        val = self.dot_product(vector1, vector2)
                        M.set_val(x, y, val)

                return M
            else:
                val = 'col: ' + str(self._max_col) + ', does not equal'
                val = val + ' col: ' + str(rows) + ' to make a valid'
                val = val + ' matrix multiplication'
                raise MatrixDimensionError(val)


class OneDimensionalMatrix(Matrix):
    '''A 1xn or nx1 matrix.
    (For the purposes of multiplication, we assume it's 1xn)'''
    def __init__(self, m, default=0):
        '''(OneDimensionalMatrix, int, boolean, float)
        A representation of a OneDimensionalMatrix that uses Matrix
        to help fill its methods'''
        Matrix.__init__(self, m, m, default)
        self._length = m

    def get_list(self):
        '''(OneDimensionalMatrix) -> list of float
        returns the list representation of the OneDimensionalMatrix'''
        # create array of length with default variables
        ret = []
        for a in range(0, len(self)):
            ret[a] = self.default

        # fills in different variables
        if(self._head.get_down() is not None):
            curr = self._head.get_down().get_right()
            while(curr is not None):
                ret[curr.get_row()] = curr.get_contents()

        return ret

    def __len__(self):
        '''(OneDimensionalMatrix) -> int
        returns the length of the OneDimensionalMatrix'''
        return self._length

    def get_index(self, cell):
        '''(OneDimensionalMatrix) -> int
        returns the spot the value is in'''
        return cell.get_row()

    def get_item(self, i):
        '''(OneDimensionalMatrix, int) -> float
        Return the i'th item in this matrix
        '''
        ret = self.default
        row = self._find_row(i)
        # tries to find row and if it does not then it returns default value
        if(row is not None):
            ret = row.get_right().get_contents()

        return ret

    def get_next_item(self, node=None):
        '''(OneDimensionalMatrix, MatrixNode) -> MatrixNode
        based on this one dimensional array we return the Node
        that appears next
        REQ: type(node) == MatrixNode'''
        ret = None
        # None means that we want first
        if(node is None):
            # checks if there are any nodes
            if(self._head.get_down() is not None):
                ret = self._head.get_down().get_right()
        else:
            # returns the node below
            ret = node.get_down()

        return ret

    def get_val(self, i, j):
        '''(OneDimensionalMatrix(), int, int) -> float
        a method that insures OneDiemnsionalMatrix does not error
        during a call'''
        ret = None
        # checks if i is in domain
        if(i < self.get_max_row):
            # checks if they are trying to access a row
            if(j == 0):
                ret = self.get_item(i)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        # checks for j in domain
        elif(j < self.get_max_row):
            # checks if they are trying acces a row
            if(i == 0):
                ret = self.get_item(j)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        else:
            val = 'got:' + str(i) + ', ' + str(j) + ', max is:'
            val = val + str(self._max_row)
            raise MatrixIndexError(val)

        return ret

    def set_val(self, i, j, new_val):
        '''(OneDimensionalMatrix(), int, int) -> float
        a method that insures OneDimensionalMatrix does not error
        '''
        # checks for i > j case
        if(i < self._max_row):
            # checks if they are trying to access a row
            if(j == 0):
                self.set_item(i, new_val)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        # checks for j > i case
        elif(j < self.get_max_row):
            # checks if they are trying to access a row
            if(i == 0):
                self.set_item(i, new_val)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        else:
            val = 'got:' + str(i) + ', ' + str(j) + ', max is:'
            val = val + str(self._max_row)
            raise MatrixIndexError(val)

    def set_item(self, i, new_val):
        '''(OneDimensionalMatrix, int, float) -> NoneType
        Set the i'th item in this matrix to new_val
        '''
        # checks for bounds
        if(self.in_bounds(i, 0)):
            # tries to find row
            row = self._find_row(i)
            # checks if value is default
            if(new_val == self.default):
                # if it is then we need to worry about case of
                # deletion
                if(row is not None):
                    self._remove(i, 0)
                # we don't need to worry about non-existant since
                # it is already default
            else:
                if(row is not None):
                    # changes value
                    row.get_right().set_contents(new_val)
                else:
                    # creates a new value and adds it
                    cell = MatrixNode(new_val)
                    self._add_to_row(i, 0, cell)
                    self._add_to_col(i, 0, cell)

        else:
            val = 'got:' + str(i) + ', max is:'
            val = val + str(self._max_row)
            raise MatrixIndexError(val)

    def multiply_matrix(self, mult_matrix):
        '''(OneDimensionalMatrix, Matrix) -> Matrix
        since I store my vector as just a column I need
        to create a case when we multiply it'''
        M = None
        col_size = None
        row_size = None
        # checks the dimensions
        (row_size, col_size) = mult_matrix.get_dimensions()
        if(self._max_row == row_size):
            # creates array which will be the result
            M = OneDimensionalMatrix(col_size, self.default)
            # goes through all the columns
            curr = mult_matrix
            for a in range(0, col_size):
                curr = curr.get_col(a)
                # sends itself since it is a OneDimensionalMatrix
                M.set_item(a, self.dot_product(self, curr))

            return M
        else:
            val = 'col: ' + str(self._max_col) + ', does not equal'
            val = val + ' col: ' + str(rows) + ' to make a valid'
            val = val + ' matrix multiplication'
            raise MatrixDimensionError(val)


class SquareMatrix(Matrix):
    '''A matrix where the number of rows and columns are equal'''

    def __init__(self, m, default=0):
        '''(SquareMatrix, int, float) -> NoneType
        creates a SquareMatrix'''
        Matrix.__init__(self, m, m, default)

    def transpose(self):
        '''(SquareMatrix) -> NoneType
        Transpose this matrix
        '''
        # goes through and transposes by turning the pointer right-down into
        # down-right since transpose is just i,j -> j,i
        row = self._head
        # starts with head node as it needs to be switched as well

        while(row is not None):
            curr = row
            while(curr is not None):
                # starts going through the columns and switching rows to
                # columns and columns to rows
                temp = curr.get_down()
                curr.set_down(curr.get_right())
                curr.set_right(temp)
                # changes col/row indicators
                temp = curr.get_col_node()
                curr.set_col(curr.get_row_node())
                curr.set_row(temp)
                # columns are now rows so it goes to next column
                curr = curr.get_down()
            # rows are now columns so it gets from columns
            # in order to progress down the rows
            row = row.get_right()

    def get_diagonal(self):
        '''(Squarematrix) -> OneDimensionalMatrix
        Return a one dimensional matrix with the values of the diagonal
        of this matrix
        '''
        M = OneDimensionalMatrix(self._max_row, self.default)
        # gets first calue and gets the index to find
        row = self._head.get_down()
        val_check = row.get_contents()
        # goes through all rows
        while(row is not None):
            curr = row.get_right()
            # goes through columns until it reaches a number greater or
            # the end of the column nodes
            while(curr is not None and curr.get_col() < val_check):
                curr = curr.get_right()

            # checks for right node before adding
            if(curr is not None and curr.get_col() == val_check):
                M.set_item(val_check, curr.get_contents())

            # iterates rows and sets next index
            row = row.get_down()
            if(row is not None):
                val_check = row.get_contents()

        return M

    def set_diagonal(self, new_diagonal):
        '''(SquareMatrix, OneDimensionalMatrix) -> NoneType
        Set the values of the diagonal of this matrix to those of new_diagonal
        '''
        # check the dimensions
        if(len(new_diagonal) == self._max_row):
            # checks the default values
            if(new_diagonal.get_default() == self.default):
                # default values are the same so we only need to add
                # unique values
                # gets the first item and sets it
                curr = new_diagonal.get_next_item()
                while(curr is not None):
                    # sets value and asks for next unique value
                    index = curr.get_row()
                    self.set_val(index, index, curr.get_contents())
                    curr = new_diagonal.get_next_item(curr)
            else:
                # set the entire diagonal as new since default
                # is not the same
                for a in range(0, len(new_diagonal)):
                    self.set_val(a, a, new_diagonal.get_item(a))

        else:
            val = 'The length of the OneDimensionalMatrices are not equal'
            raise MatrixDimensionError(val)


class SymmetricMatrix(SquareMatrix):
    '''A Symmetric Matrix, where m[i, j] = m[j, i] for all i and j'''

    def __init__(self, m, default=0):
        '''(SymmetricMatrix, int, float) ->NoneType
        create a new symmetric matrix'''
        SquareMatrix.__init__(self, m, default)

    def set_val(self, m, n, val):
        '''(SymmetricMatrix, int, int, float)
        insures all values are symmetric'''
        SquareMatrix.set_val(m, n, val)
        SquareMatrix.set_val(n, m, val)

    def set_row(self, i, new_row):
        '''(SymmetricMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_row()
        '''
        raise MatrixInvalidOperationError('invalid type')

    def set_col(self, i, new_row):
        '''(SymmetricMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_col()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_rows(self, i, j):
        '''(SymmetricMatrix, int, int) -> NoneType
        deals with swap_row()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_cols(self, i, j):
        '''(SymmetricMatrix, int, int) -> NoneType
        deals with swap_cols()'''
        raise MatrixInvalidOperationError('invalid type')

    def add_scalar(self, add_val):
        '''(SymmetricMatrix, int) -> Nonetype
        deals with add_sccalar'''
        raise MatrixInvalidOperationError('invalid type')

    def subtract_scalar(self, sub_val):
        '''(SymmetricMatrix, int) -> Nonetype
        deals with sub_scalar'''
        raise MatrixInvalidOperationError('invalid type')


class DiagonalMatrix(SquareMatrix, OneDimensionalMatrix):
    '''A square matrix with 0 values everywhere but the diagonal'''

    def __init__(self, m, default=0):
        '''(DiagonalMatrix, int) -> NoneType
        Creates a diagonal matrix'''
        OneDimensionalMatrix.__init__(self, m, 0)
        SquareMatrix.__init__(self, m, 0)
        self._max_col = m

    def set_val(self, i, j, new_val):
        '''(DiagonalMatrix, int, int, float) -> NoneType
        adds based on the rules of a Matrix'''
        if(self.in_bounds(i, j)):
            # checks that it's asking for diagonal
            if(i == j):
                # changes matrices
                SquareMatrix.set_val(self, i, j, new_val)
                OneDimensionalMatrix.set_item(self, i, new_val)
            else:
                val = 'This is a diagonal Matrix and its values'
                val = val + ' cannot be adjusted at: ' + str(i)
                val = val + ' : ' + str(j)
                raise MatrixInvalidOperationError(val)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j) + ', max col:'
            val = val + str(self._max_col)
            raise MatrixIndexError(val)

    def set_item(self, i, new_val):
        '''(DiagonalMatrix, int, float) -> NoneType
        adds item based on the rules of a OneDimensional Matrix'''
        if(self.in_bounds(i, i)):
            OneDimensionalMatrix.set_item(self, i, new_val)
            SquareMatrix.set_val(self, i, i, new_val)
        else:
            val = 'got row:' + str(i) + ', max size:' + str(self._max_row)
            raise MatrixIndexError(val)

    def get_val(self, i, j):
        '''(DiagonalMatrix, int, int) -> float
        Return the value of m[i,j] for this matrix m
        '''
        # deals with vertical case since this Matrix
        # stores in both vertical and diagonal
        ret = None
        if(i == j):
            SquareMatrix.get_val(self, i, j)
        else:
            return 0

    def get_row(self, i):
        '''(DiagonalMatrix, int) -> OneDimensionalMatrix
        deals with getting the row of a DiagonalMatrix'''
        ret = SquareMatrix.get_row(self, i)

        # checks for case where we are accessing 0
        # since I have values going down col 0
        if(i != 0):
            ret.set_val(0, 0)

        return ret

    def get_col(self, i):
        '''(Matrix, int) -> OneDimensionalMatrix
        deals with getting a column in DiagonalMatrix
        '''
        ret = None

        # if we're getting col 0 I need to send them just
        # the first value of the column since there are
        # other values in col 0
        if(i == 0):
            ret = OneDimensionalMatrix(len(self))
            ret.set_item(0, self.get_item(0))
        else:
            ret = SquareMatrix.get_col(self, i)

        return ret

    def set_row(self, i, new_row):
        '''(DiagonalMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_row()'''
        raise MatrixInvalidOperationError('invalid type')

    def set_col(self, i, new_row):
        '''(DiagonalMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_col()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_rows(self, i, j):
        '''(DiagonalMatrix, int, int) -> NoneType
        deals with swap_row()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_cols(self, i, j):
        '''(DiagonalMatrix, int, int) -> NoneType
        deals with swap_cols()'''
        raise MatrixInvalidOperationError('invalid type')

    def add_scalar(self, add_val):
        '''(DiagonalMatrix, int) -> Nonetype
        deals with add_sccalar'''
        raise MatrixInvalidOperationError('invalid type')

    def subtract_scalar(self, sub_val):
        '''(DiagonalMatrix, int) -> Nonetype
        deals with sub_scalar'''
        raise MatrixInvalidOperationError('invalid type')

    def add_matrix(self, add_Matrix):
        '''(DiagonalMatrix, Matrix) -> Nonetype
        deals with add_matrix'''
        raise MatrixInvalidOperationError('invalid type')


class IdentityMatrix(DiagonalMatrix):
    '''A matrix with 1s on the diagonal and 0s everywhere else'''

    def __init__(self, m):
        '''(Matrix, int) -> NoneType
        creates an identity matrix'''
        DiagonalMatrix.__init__(self, m)
        # fills the values with 1
        for a in range(0, m):
            DiagonalMatrix.set_val(self, a, a, 1)

    def set_val(self, i, j, val):
        '''(IdentityMatrix, int, int, float)
        deals with set_val'''
        raise MatrixInvalidOperationError('invalid type')


class MatrixIndexError(Exception):
    '''An attempt has been made to access an invalid index in this matrix'''
    def __init__(self, value):
        self.message = 'An attempt has been made to access an invalid index'
        self.message = self.message + 'in this matrix ' + str(value)

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


class MatrixNode():
    '''A general node class for a matrix'''

    def __init__(self, contents, right=None, down=None):
        '''(MatrixNode, obj, MatrixNode, MatrixNode) -> NoneType
        Create a new node holding contents, that is linked to right
        and down in a matrix
        '''
        self._contents = contents
        self._right = right
        self._down = down
        # added col and row nodes that direct where to find the row and col
        self._col = None
        self._row = None

    def __str__(self):
        '''(MatrixNode) -> str
        Return the string representation of this node
        '''
        return str(self._contents)

    def get_col(self):
        '''(MatrixNode) -> int
        returns the col value indicating the col position of the node

        REQ: self._col = MatrixNode'''
        # since col is a MatrixNode I just go and check for contents
        return self._col.get_contents()

    def get_col_node(self):
        '''(MatrixNode) -> MatrixNode
        returns the col node indicating the col position of the node'''
        return self._col

    def set_col(self, val):
        '''(MatrixNode, int) -> int
        sets the column value of the node'''
        self._col = val

    def set_row(self, val):
        '''(MatrixNode, int) -> int
        set the row value of the node'''
        self._row = val

    def get_row(self):
        '''(MatrixNode) -> str
        returns the row value indicating the row position of the node

        REQ: self._row = MatrixNode'''
        # since row is a MatrixNode I need to get the contents
        return self._row.get_contents()

    def get_row_node(self):
        '''(MatrixNode) -> MatrixNode
        returns the row node indicating the row position of the node'''
        return self._row

    def get_contents(self):
        '''(MatrixNode) -> obj
        Return the contents of this node
        '''
        return self._contents

    def set_contents(self, new_contents):
        '''(MatrixNode, obj) -> NoneType
        Set the contents of this node to new_contents
        '''
        self._contents = new_contents

    def get_right(self):
        '''(MatrixNode) -> MatrixNode
        Return the node to the right of this one
        '''
        return self._right

    def set_right(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set the new_node to be to the right of this one in the matrix
        '''
        self._right = new_node

    def add_right(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Adds the new_node to the right of this node if no node exists
        otherwise places new node to right and gives it it's children
        '''
        # grab the value to the right
        curr = self.get_right()
        if(curr is not None):
            # exists so we need to replace it
            new_node.set_right(curr)
            self.set_right(new_node)
        else:
            # doesn't exist
            self.set_right(new_node)

    def remove_right(self):
        '''(MatrixNode) -> NoneType
        removes the node to the right and replaces it with any children
        the right node has'''
        # checks to see if a right Node exists
        if(self._right is not None):
            # checks for children
            if(self._right._right is not None):
                self.set_right(self._right._right)
            else:
                self.set_right(None)

    def get_down(self):
        '''(MatrixNode) -> MatrixNode
        Return the node below this one
        '''
        return self._down

    def set_down(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set new_node to be below this one in the matrix
        '''
        self._down = new_node

    def add_down(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Adds the new_node to the bottom of this node if no node exists
        otherwise places new node to bottom and gives it it's children

        REQ: new_node.get_right() == None
        REQ: new_node.get_down() == None
        '''
        # grab the value to the right
        curr = self.get_down()
        if(curr is not None):
            # exists so we need to replace it
            new_node.set_down(curr)
            self.set_down(new_node)
        else:
            # doesn't exist
            self.set_down(new_node)

    def remove_down(self):
        '''(MatrixNode) -> NoneType
        removes the node to the bottom and replaces it with any children
        the node below has'''
        # checks whether down exists
        if(self._down is not None):
            # checks for children
            if(self._down._down is not None):
                self.set_down(self._down._down)
            else:
                self.set_down(None)


class Matrix():
    '''A class to represent a mathematical matrix'''

    def __init__(self, m, n, default=0):
        '''(Matrix, int, int, float) -> NoneType
        Create a new m x n matrix with all values set to default
        '''
        self._head = MatrixNode(None)
        # _max_row and _max_col are numbers to check and make sure that
        # the program does not go over the Matrix size
        self._max_row = m
        self._max_col = n
        self.default = default

    def _find_row(self, row_num):
        '''(Matrix, int, MatrixNode) -> MatrixNode
        Helper function that isolates the head where the row starts
        and returns it, if it's not found then it returns None'''
        ret = None
        curr = self._head.get_down()
        # loops until row num is greater
        while(curr is not None and curr.get_contents() < row_num):
            curr = curr.get_down()
        # checks for right row and returns appropriate decision
        if(curr is not None and curr.get_contents() == row_num):
            ret = curr
        return ret

    def _find_col(self, col_num):
        '''(Matrix, int, MatrixNode) -> MatrixNode
        Helper function that isolates the head where the row starts
        and returns it, if it's not found then it returns None'''
        ret = None
        curr = self._head.get_right()
        # loops until col num is greater
        while(curr is not None and curr.get_contents() < col_num):
            curr = curr.get_right()
        # checks for right col and returns appropriate decision
        if(curr is not None and curr.get_contents() == col_num):
            ret = curr
        return ret

    def _get_cell(self, i, j):
        '''(Matrix, int, int) -> MatrixNode
        Returns the cell at the position, if it doesn't exist then it
        returns None

        REQ: self.in_bounds(i, j) == True'''
        ret = None

        # sets curr as first row
        curr = self._head.get_down()
        if(curr is not None):
            # gets row
            curr = self._find_row(i)
            # checks to see if it found the row
            if(curr is not None):

                curr = curr.get_right()
                # searching for the value based on the col value in MatrixNode
                while(curr is not None and curr.get_col() < j):
                    curr = curr.get_right()

                # checks to see if it's found
                if(curr is not None and curr.get_col() == j):
                    ret = curr
                # not found
                else:
                    ret = None
            else:
                ret = None

        return ret

    def _remove(self, i, j):
        '''(Matrix, int, int) -> NoneType
        removes the selected node. this method is to increase efficiency
        This method is private as generally the Matrix will just return
        the default value'''
        # tries to get row
        row = self._find_row(i)
        temp_row = MatrixNode(None)

        if(row is not None):
            temp_row = row
            # recurses till it finds the col value to the right of the
            # current node
            while(row.get_right() is not None and
                  row.get_right().get_col() < j):
                row = row.get_right()

            # checks if they found the node
            if(row.get_right() is not None and row.get_right().get_col() == j):
                row.remove_right()

        # tries to get column
        col = self._find_col(j)
        temp_col = MatrixNode(None)

        if(col is not None):
            temp_col = col
            # recurses till it finds the row value under the current node
            while(col.get_down() is not None and
                  col.get_down().get_row() < i):
                col = col.get_down()

            # checks if program found node
            if(col.get_down() is not None and col.get_down().get_row() == i):
                col.remove_down()

        # uses previously saved temp_row/col values to go through and
        # eliminate any empty row/columns
        if(temp_row.get_right() == None):
            self._remove_row(i)
        if(temp_col.get_down() == None):
            self._remove_col(j)

    def _remove_row(self, i):
        '''(Matrix, int) -> NoneType
        Removes the row indicated as a pointer'''
        # loops and tries to find the row in question
        curr = self._head
        while(curr.get_down() is not None and
              curr.get_down().get_contents() < i):
            curr = curr.get_down()
        # checks if the node was found
        if(curr.get_down() is not None and
           curr.get_down().get_contents() == i):
            curr.remove_down()

    def _remove_col(self, j):
        '''(Matrix, int) -> NoneType
        Removes the col indicated as a pointer'''
        # loops and tries to find the column in question
        curr = self._head
        while(curr.get_right() is not None and
              curr.get_right().get_contents() < j):
            curr = curr.get_right()

        # checks if column was found
        if(curr.get_right() is not None and
           curr.get_right().get_contents() == j):
            curr.remove_right()

    def _add_to_row(self, i, j, cell):
        '''(Matrix, int, MatrixNode) -> NoneType
        a helper method that adds a new cell
        to a row if it exists and if it doesn't
        it creates a new one

        REQ: M(i, cell.get_col()) does not previously exist, that is
             _get_cell(i, j) == None
        REQ: in_bounds(i, j) == True'''
        # tries to find row
        row = self._find_row(i)

        # row is not found so we need to add row
        if(row is None):
            # we need to create a new row as it does not exist
            row = MatrixNode(i)
            # tries to order the row by finding the last row < i
            curr = self._head
            while(curr.get_down() is not None and
                  curr.get_down().get_contents() < i):
                curr = curr.get_down()
            # adds row
            curr.add_down(row)

        # tries to order the values by finding the last cell with col < j
        curr = row
        while(curr.get_right() is not None and curr.get_right().get_col() < j):
            curr = curr.get_right()
        curr.add_right(cell)

        # sets the row node of the cell
        cell.set_row(row)

    def _add_to_col(self, i, j, cell):
        '''(Matrix, int, MatrixNode) -> NoneType
        a helper method that adds a new cell
        to a col if it exists and if it doesn't
        it creates a new one

        REQ: M(cell.get_row(), j) does not previously exist, that is
             _get_cell(i, j) == None
        REQ: in_bounds(i, j) == True'''
        # tries to find column
        col = self._find_col(j)

        # column is not found
        if(col is None):
            # we need to create a new row as it does not exist
            col = MatrixNode(j)
            # tries to order the row by finding the last row < i
            curr = self._head
            while(curr.get_right() is not None and
                  curr.get_right().get_contents() < j):
                curr = curr.get_right()
            # adds row
            curr.add_right(col)

        # tries to order the values by finding the last cell with row < i
        curr = col
        while(curr.get_down() is not None and curr.get_down().get_row() < i):
            curr = curr.get_down()
        curr.add_down(cell)

        # sets the row node of the cell
        cell.set_col(col)

    def in_bounds(self, i, j):
        '''(Matrix, int, int) -> boolean
        returns a true if the value exists in the Matrix'''
        ret = False
        if(i < self._max_row and j < self._max_col and i >= 0 and j >= 0):
            ret = True
        return ret

    def set_val(self, i, j, new_val):
        '''(Matrix, int, int, float) -> NoneType
        Set the value of m[i,j] to new_val for this matrix m
        '''
        # checks if the search is in bounds
        if(self.in_bounds(i, j)):
            # attempts to get cell
            cell = self._get_cell(i, j)
            # cell is found we're done
            if(cell is not None):
                if(new_val == self.default):
                    self._remove(i, j)
                else:
                    cell.set_contents(new_val)
            # cell is not found so we need to add it
            else:
                if(new_val != self.default):
                    # creates cell
                    cell = MatrixNode(new_val)
                    # calls methods to add cell
                    self._add_to_row(i, j, cell)
                    self._add_to_col(i, j, cell)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

    def get_val(self, i, j):
        '''(Matrix, int, int) -> float
        Return the value of m[i,j] for this matrix m
        '''
        # checks if value is in matrix
        if(self.in_bounds(i, j)):
            # tries and find cell
            ret = self._get_cell(i, j)

            # checks if cell is different from default
            if(ret is not None):
                # is so it gets non-default value
                ret = ret.get_contents()
            else:
                ret = self.default

            return ret
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

    def get_row(self, row_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the row_num'th row of this matrix
        '''
        ret = None

        # insures that the row asked for is in the index
        if(self.in_bounds(row_num, 0)):
            # calls recursive helper to get the row asked
            row = self._find_row(row_num)

            # creates a default row
            ret = OneDimensionalMatrix(self._max_col, self.default)

            # None tells us that the row does not exist
            # and as such we just return the default OneDimensionalMatrix
            if(row is not None):
                # moves to first data
                curr = row.get_right()
                # fills OneDimensionalMatrix
                while(curr is not None):
                    ret.set_item(curr.get_col(), curr.get_contents())
                    curr = curr.get_right()
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

        return ret

    def set_row(self, row_num, new_row):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the row_num'th row of this matrix to those of new_row
        '''
        # checks that the row to be set is in bounds
        if(new_row is not None):
            if(self.in_bounds(row_num, len(new_row) - 1)):
                if(self.default == new_row.default):
                    # has to delete everything the row first
                    row = self._find_row(row_num)
                    while(row is not None and row.get_right() is not None):
                        curr = row.get_right()
                        self._remove(row_num, curr.get_col())

                    # gets items from row and puts them in matrix
                    curr = new_row.get_next_item()
                    while(curr is not None):
                        self.set_val(row_num, new_row.get_index(curr),
                                     curr.get_contents())
                        curr = new_row.get_next_item(curr)
                else:
                    i = row_num
                    new_row_values = new_row.get_list()
                    for x in range(0, len(new_row)):
                        self.set_val(i, x, new_row.get_item(x))
            else:
                val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
                val = val + ', got col:' + str(j)
                val = val + ', max col:' + str(self._max_col)
                raise MatrixIndexError(val)
        else:
            # erases row
            row = self._find_row(row_num)
            while(row is not None and row.get_right() is not None):
                curr = row.get_right()
                self._remove(row_num, curr.get_col())

    def get_col(self, col_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the col_num'th column of this matrix
        '''
        ret = None

        # insures that the column asked for is in the index
        if(self.in_bounds(0, col_num)):
            # calls recursive helper to get the row asked
            col = self._find_col(col_num)

            # creates a default row
            ret = OneDimensionalMatrix(self._max_row, self.default)

            # None tells us that the row does not exist
            # and as such we just return the default OneDimensionalMatrix
            if(col is not None):
                # moves to first data
                curr = col.get_down()
                # fills OneDimensionalMatrix
                while(curr is not None):
                    ret.set_item(curr.get_row(), curr.get_contents())
                    curr = curr.get_down()
        else:
            val = 'got col:' + str(col_num)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

        return ret

    def set_col(self, col_num, new_col):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the col_num'th column of this matrix to
        those of new_row '''
        # checks that the column to be set is in bounds
        if(new_col is not None):
            if(self.in_bounds(len(new_col) - 1, col_num)):
                if(self.default == new_col.default):
                    # has to delete everything the col first
                    col = self._find_col(col_num)
                    while(col is not None and col.get_down() is not None):
                        curr = col.get_down()
                        self._remove(curr.get_row(), col_num)

                    # gets items from column and puts them in matrix
                    curr = new_col.get_next_item()
                    while(curr is not None):
                        self.set_val(new_col.get_index(curr),
                                     col_num, curr.get_contents())
                        curr = new_col.get_next_item(curr)
                else:
                    i = col_num
                    new_col_values = new_col.get_list()
                    for x in range(0, len(new_col)):
                        self.set_val(x, i, new_col.get_item(x))
            else:
                val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
                val = val + ', got col:' + str(j)
                val = val + ', max col:' + str(self._max_col)
                raise MatrixIndexError(val)
        else:
            # erases column
            col = self._find_col(col_num)
            while(col is not None and col.get_down() is not None):
                curr = col.get_down()
                self._remove(curr.get_row(), col_num)

    def swap_rows(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of rows i and j in this matrix
        '''
        # checks for index error
        if(i < self._max_row and j < self._max_row):
            i_node = self._find_row(i)
            j_node = self._find_row(j)

            if(i_node is not None):
                # can find both i and j
                if(j_node is not None):
                    # replaces i with j and j with i
                    i_vector = self.get_row(i)
                    self.set_row(i, self.get_row(j))
                    self.set_row(j, i_vector)

                # can find only i
                else:
                    # replaces i in j spot and makes i empty
                    self.set_row(j, self.get_row(i))
                    self.set_row(i, None)

            # can only find j
            elif(j is not None):
                # replace j in i and makes j empty
                self.set_row(i, self.get_row(j))
                self.set_row(j, None)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j) + ', max col:'
            val = val + str(self._max_col)
            raise MatrixIndexError(val)

    def swap_cols(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of columns i and j in this matrix
        '''
        # checks for index error
        if(i < self._max_col and j < self._max_col):
            i_node = self._find_col(i)
            j_node = self._find_col(j)

            if(i_node is not None):
                # can find both i and j
                if(j_node is not None):
                    # replaces i with j and j with i
                    i_vector = self.get_col(i)
                    self.set_col(i, self.get_col(j))
                    self.set_col(j, i_vector)

                # can find only i
                else:
                    # replaces i in j spot and makes i empty
                    self.set_col(j, self.get_col(i))
                    self.set_col(i, None)

            # can only find j
            elif(j is not None):
                # replace j in i and makes j empty
                self.set_col(i, self.get_col(j))
                self.set_col(j, None)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j) + ', max col:'
            val = val + str(self._max_col)
            raise MatrixIndexError(val)

    def add_scalar(self, add_value):
        '''(Matrix, float) -> NoneType
        Increase all values in this matrix by add_value
        '''
        # changes default values
        self.default = self.default + add_value

        # gets first row
        curr_row = self._head.get_down()
        while(curr_row is not None):
            # gets first cell
            curr = curr_row.get_right()
            while(curr is not None):
                # gets cell value and changes it
                val = curr.get_contents()
                curr.set_contents(val + add_value)
                # goes to next cell
                curr = curr.get_right()
            # goes to next row
            curr_row = curr_row.get_down()

    def subtract_scalar(self, sub_value):
        '''(Matrix, float) -> NoneType
        Decrease all values in this matrix by sub_value
        '''
        # changes default values
        self.default = self.default - sub_value

        # gets first row
        curr_row = self._head.get_down()
        while(curr_row is not None):
            # gets first cell
            curr = curr_row.get_right()
            while(curr is not None):
                # gets cell value and changes it
                val = curr.get_contents()
                curr.set_contents(val - sub_value)
                # goes to next cell
                curr = curr.get_right()
            # goes to next row
            curr_row = curr_row.get_down()

    def multiply_scalar(self, mult_value):
        '''(Matrix, float) -> NoneType
        Multiply all values in this matrix by mult_value
        '''
        # changes default values
        self.default = self.default * mult_value

        # gets first row
        curr_row = self._head.get_down()
        while(curr_row is not None):
            # gets first cell
            curr = curr_row.get_right()
            while(curr is not None):
                # gets cell value and changes it
                val = curr.get_contents()
                curr.set_contents(val * mult_value)
                # goes to next cell
                curr = curr.get_right()
            # goes to next row
            curr_row = curr_row.get_down()

    def get_default(self):
        '''(Matrix) -> float
        returns the default value'''
        return self.default

    def get_first_row(self):
        '''(Matrix) -> MatrixNode
        returns the first row'''
        return self._head.get_down()

    def get_first_col(self):
        '''(Matrix) -> MatrixNode
        returns the frist col'''
        return self._head.get_right()

    def get_dimensions(self):
        '''(Matrix) -> (int, int)
        returns the max row,col of the matrix'''
        return (self._max_row, self._max_col)

    def add_matrix(self, adder_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the sum of this matrix and adder_matrix
        '''
        # check dimensions
        if(adder_matrix.get_dimensions() == self.get_dimensions()):
            # create a new matrix
            default = self.default + adder_matrix.get_default()
            M = Matrix(self._max_row, self._max_col, default)

            # gets default for use later
            default = adder_matrix.get_default()

            # get the first row of values
            row_1 = self._head.get_down()
            row_2 = adder_matrix.get_first_row()

            # keeps looping while there still exists both rows
            while(row_1 is not None and row_2 is not None):
                # checks the relationship of the rows
                if(row_1.get_contents() == row_2.get_contents()):
                    # they are equal so we need to consider the case
                    # that some numbers are the same
                    self._add_matrix(M, [row_1, row_2], self.default, default)
                    # iterates
                    row_1 = row_1.get_down()
                    row_2 = row_2.get_down()
                elif(row_1.get_contents() < row_2.get_contents()):
                    # only uses row1
                    self._add_matrix(M, [row_1], default)
                    row_1 = row_1.get_down()
                else:
                    # only uses row2
                    self._add_matrix(M, [row_2], self.default)
                    row_2 = row_2.get_down()

            while(row_1 is not None):
                # only uses row1 since only row_1 exists
                self._add_matrix(M, [row_1], default)
                row_1 = row_1.get_down()

            while(row_2 is not None):
                # only uses row2
                self._add_matrix(M, [row_2], self.default)
                row_2 = row_2.get_down()

            return M
        else:
            val = 'This Matrix dimensions: ' + self.get_dimensions()
            val = val + ', adding matrix dimensions: '
            val = val + adder_matrix.get_dimensions()
            raise MatrixDimensionError(val)

    def _add_matrix(self, M, row_nodes, default1, default2=None):
        '''(Matrix, Matrix, list of MatrixNode, float, float)-> NoneType
        helper method to add_matrix, deals with case
        of list having a length of 1 or 2

        REQ: len(row_node) == 1 or  len(row_node) == 2
        REQ: row_nodes[0] is not None'''
        # case where there is more than one row
        if(len(row_nodes) > 1):
            # gets rows
            row1 = row_nodes[0].get_right()
            row2 = row_nodes[1].get_right()
            row_val = row1.get_row()

            # goes through all the columns
            while(row1 is not None and row2 is not None):
                # checks where the rows are in terms of column
                if(row1.get_col() == row2.get_col()):
                    # same place so we add both together
                    val1 = row1.get_contents()
                    val2 = row2.get_contents()

                    M.set_val(row_val, row1.get_col(), (val1 + val2))
                    # iterates
                    row1 = row1.get_right()
                    row2 = row2.get_right()
                elif(row1.get_col() < row2.get_col()):
                    # row1 is smaller so we add it first
                    val1 = row1.get_contents()
                    # add default of second matrix as well
                    M.set_val(row_val, row1.get_col(), (val1 + default2))
                    row1 = row1.get_right()
                else:
                    # row2 is smaller so we add it first
                    val1 = row2.get_contents()
                    M.set_val(row_val, row2.get_col(), (val1 + default1))
                    row2 = row2.get_right()

            while(row1 is not None):
                # only row1 exists
                val1 = row1.get_contents()
                M.set_val(row_val, row1.get_col(), (val1 + default2))
                row1 = row1.get_right()

            while(row2 is not None):
                # only row2 exists
                val1 = row2.get_contents()
                M.set_val(row_val, row2.get_col(), (val1 + default1))
                row2 = row2.get_right()

        else:
            # only one row was passed
            row = row_nodes[0]
            curr = row.get_right()
            while(curr is not None):
                M.set_val(row.get_contents(),
                          curr.get_col(), (curr.get_contents() + default1))
                curr = curr.get_right()

    def dot_product(self, row1, row2):
        '''(Matrix, OneDimensionalMatrix, OneDimensionalMatrix) -> float
        returns the dotproduct of two vectors, returns zero
        in all other situations'''
        ret = 0
        # goes through all the cells and adds them to total
        # only if the lengths are the same
        if(len(row1) == len(row2)):
            for a in range(0, len(row1)):
                ret = ret + (row1.get_item(a)*row2.get_item(a))
        else:
            val = 'given unequal lengths: ' + len(row1) + ' : ' + len(row2)
            raise MatrixDimensionError(val)

        return ret

    def multiply_matrix(self, mult_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the product of this matrix and mult_matrix
        '''
        M = None
        if(mult_matrix is not None):
            # gets row/col of matrix to multiply
            rows = None
            cols = None
            (rows, cols) = mult_matrix.get_dimensions()
            # check whether this is a valid multiplication
            if(self._max_col == rows):
                # creates matrix
                M = Matrix(self._max_row, cols, self.default)

                # goes through all columns and rows
                for x in range(0, self._max_row):
                    vector1 = self.get_row(x)
                    for y in range(0, cols):
                        vector2 = mult_matrix.get_col(y)
                        val = self.dot_product(vector1, vector2)
                        M.set_val(x, y, val)

                return M
            else:
                val = 'col: ' + str(self._max_col) + ', does not equal'
                val = val + ' col: ' + str(rows) + ' to make a valid'
                val = val + ' matrix multiplication'
                raise MatrixDimensionError(val)


class OneDimensionalMatrix(Matrix):
    '''A 1xn or nx1 matrix.
    (For the purposes of multiplication, we assume it's 1xn)'''
    def __init__(self, m, default=0):
        '''(OneDimensionalMatrix, int, boolean, float)
        A representation of a OneDimensionalMatrix that uses Matrix
        to help fill its methods'''
        Matrix.__init__(self, m, m, default)
        self._length = m

    def get_list(self):
        '''(OneDimensionalMatrix) -> list of float
        returns the list representation of the OneDimensionalMatrix'''
        # create array of length with default variables
        ret = []
        for a in range(0, len(self)):
            ret[a] = self.default

        # fills in different variables
        if(self._head.get_down() is not None):
            curr = self._head.get_down().get_right()
            while(curr is not None):
                ret[curr.get_row()] = curr.get_contents()

        return ret

    def __len__(self):
        '''(OneDimensionalMatrix) -> int
        returns the length of the OneDimensionalMatrix'''
        return self._length

    def get_index(self, cell):
        '''(OneDimensionalMatrix) -> int
        returns the spot the value is in'''
        return cell.get_row()

    def get_item(self, i):
        '''(OneDimensionalMatrix, int) -> float
        Return the i'th item in this matrix
        '''
        ret = self.default
        row = self._find_row(i)
        # tries to find row and if it does not then it returns default value
        if(row is not None):
            ret = row.get_right().get_contents()

        return ret

    def get_next_item(self, node=None):
        '''(OneDimensionalMatrix, MatrixNode) -> MatrixNode
        based on this one dimensional array we return the Node
        that appears next
        REQ: type(node) == MatrixNode'''
        ret = None
        # None means that we want first
        if(node is None):
            # checks if there are any nodes
            if(self._head.get_down() is not None):
                ret = self._head.get_down().get_right()
        else:
            # returns the node below
            ret = node.get_down()

        return ret

    def get_val(self, i, j):
        '''(OneDimensionalMatrix(), int, int) -> float
        a method that insures OneDiemnsionalMatrix does not error
        during a call'''
        ret = None
        # checks if i is in domain
        if(i < self.get_max_row):
            # checks if they are trying to access a row
            if(j == 0):
                ret = self.get_item(i)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        # checks for j in domain
        elif(j < self.get_max_row):
            # checks if they are trying acces a row
            if(i == 0):
                ret = self.get_item(j)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        else:
            val = 'got:' + str(i) + ', ' + str(j) + ', max is:'
            val = val + str(self._max_row)
            raise MatrixIndexError(val)

        return ret

    def set_val(self, i, j, new_val):
        '''(OneDimensionalMatrix(), int, int) -> float
        a method that insures OneDimensionalMatrix does not error
        '''
        # checks for i > j case
        if(i < self._max_row):
            # checks if they are trying to access a row
            if(j == 0):
                self.set_item(i, new_val)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        # checks for j > i case
        elif(j < self.get_max_row):
            # checks if they are trying to access a row
            if(i == 0):
                self.set_item(i, new_val)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        else:
            val = 'got:' + str(i) + ', ' + str(j) + ', max is:'
            val = val + str(self._max_row)
            raise MatrixIndexError(val)

    def set_item(self, i, new_val):
        '''(OneDimensionalMatrix, int, float) -> NoneType
        Set the i'th item in this matrix to new_val
        '''
        # checks for bounds
        if(self.in_bounds(i, 0)):
            # tries to find row
            row = self._find_row(i)
            # checks if value is default
            if(new_val == self.default):
                # if it is then we need to worry about case of
                # deletion
                if(row is not None):
                    self._remove(i, 0)
                # we don't need to worry about non-existant since
                # it is already default
            else:
                if(row is not None):
                    # changes value
                    row.get_right().set_contents(new_val)
                else:
                    # creates a new value and adds it
                    cell = MatrixNode(new_val)
                    self._add_to_row(i, 0, cell)
                    self._add_to_col(i, 0, cell)

        else:
            val = 'got:' + str(i) + ', max is:'
            val = val + str(self._max_row)
            raise MatrixIndexError(val)

    def multiply_matrix(self, mult_matrix):
        '''(OneDimensionalMatrix, Matrix) -> Matrix
        since I store my vector as just a column I need
        to create a case when we multiply it'''
        M = None
        col_size = None
        row_size = None
        # checks the dimensions
        (row_size, col_size) = mult_matrix.get_dimensions()
        if(self._max_row == row_size):
            # creates array which will be the result
            M = OneDimensionalMatrix(col_size, self.default)
            # goes through all the columns
            curr = mult_matrix
            for a in range(0, col_size):
                curr = curr.get_col(a)
                # sends itself since it is a OneDimensionalMatrix
                M.set_item(a, self.dot_product(self, curr))

            return M
        else:
            val = 'col: ' + str(self._max_col) + ', does not equal'
            val = val + ' col: ' + str(rows) + ' to make a valid'
            val = val + ' matrix multiplication'
            raise MatrixDimensionError(val)


class SquareMatrix(Matrix):
    '''A matrix where the number of rows and columns are equal'''

    def __init__(self, m, default=0):
        '''(SquareMatrix, int, float) -> NoneType
        creates a SquareMatrix'''
        Matrix.__init__(self, m, m, default)

    def transpose(self):
        '''(SquareMatrix) -> NoneType
        Transpose this matrix
        '''
        # goes through and transposes by turning the pointer right-down into
        # down-right since transpose is just i,j -> j,i
        row = self._head
        # starts with head node as it needs to be switched as well

        while(row is not None):
            curr = row
            while(curr is not None):
                # starts going through the columns and switching rows to
                # columns and columns to rows
                temp = curr.get_down()
                curr.set_down(curr.get_right())
                curr.set_right(temp)
                # changes col/row indicators
                temp = curr.get_col_node()
                curr.set_col(curr.get_row_node())
                curr.set_row(temp)
                # columns are now rows so it goes to next column
                curr = curr.get_down()
            # rows are now columns so it gets from columns
            # in order to progress down the rows
            row = row.get_right()

    def get_diagonal(self):
        '''(Squarematrix) -> OneDimensionalMatrix
        Return a one dimensional matrix with the values of the diagonal
        of this matrix
        '''
        M = OneDimensionalMatrix(self._max_row, self.default)
        # gets first calue and gets the index to find
        row = self._head.get_down()
        val_check = row.get_contents()
        # goes through all rows
        while(row is not None):
            curr = row.get_right()
            # goes through columns until it reaches a number greater or
            # the end of the column nodes
            while(curr is not None and curr.get_col() < val_check):
                curr = curr.get_right()

            # checks for right node before adding
            if(curr is not None and curr.get_col() == val_check):
                M.set_item(val_check, curr.get_contents())

            # iterates rows and sets next index
            row = row.get_down()
            if(row is not None):
                val_check = row.get_contents()

        return M

    def set_diagonal(self, new_diagonal):
        '''(SquareMatrix, OneDimensionalMatrix) -> NoneType
        Set the values of the diagonal of this matrix to those of new_diagonal
        '''
        # check the dimensions
        if(len(new_diagonal) == self._max_row):
            # checks the default values
            if(new_diagonal.get_default() == self.default):
                # default values are the same so we only need to add
                # unique values
                # gets the first item and sets it
                curr = new_diagonal.get_next_item()
                while(curr is not None):
                    # sets value and asks for next unique value
                    index = curr.get_row()
                    self.set_val(index, index, curr.get_contents())
                    curr = new_diagonal.get_next_item(curr)
            else:
                # set the entire diagonal as new since default
                # is not the same
                for a in range(0, len(new_diagonal)):
                    self.set_val(a, a, new_diagonal.get_item(a))

        else:
            val = 'The length of the OneDimensionalMatrices are not equal'
            raise MatrixDimensionError(val)


class SymmetricMatrix(SquareMatrix):
    '''A Symmetric Matrix, where m[i, j] = m[j, i] for all i and j'''

    def __init__(self, m, default=0):
        '''(SymmetricMatrix, int, float) ->NoneType
        create a new symmetric matrix'''
        SquareMatrix.__init__(self, m, default)

    def set_val(self, m, n, val):
        '''(SymmetricMatrix, int, int, float)
        insures all values are symmetric'''
        SquareMatrix.set_val(m, n, val)
        SquareMatrix.set_val(n, m, val)

    def set_row(self, i, new_row):
        '''(SymmetricMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_row()
        '''
        raise MatrixInvalidOperationError('invalid type')

    def set_col(self, i, new_row):
        '''(SymmetricMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_col()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_rows(self, i, j):
        '''(SymmetricMatrix, int, int) -> NoneType
        deals with swap_row()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_cols(self, i, j):
        '''(SymmetricMatrix, int, int) -> NoneType
        deals with swap_cols()'''
        raise MatrixInvalidOperationError('invalid type')

    def add_scalar(self, add_val):
        '''(SymmetricMatrix, int) -> Nonetype
        deals with add_sccalar'''
        raise MatrixInvalidOperationError('invalid type')

    def subtract_scalar(self, sub_val):
        '''(SymmetricMatrix, int) -> Nonetype
        deals with sub_scalar'''
        raise MatrixInvalidOperationError('invalid type')


class DiagonalMatrix(SquareMatrix, OneDimensionalMatrix):
    '''A square matrix with 0 values everywhere but the diagonal'''

    def __init__(self, m, default=0):
        '''(DiagonalMatrix, int) -> NoneType
        Creates a diagonal matrix'''
        OneDimensionalMatrix.__init__(self, m, 0)
        SquareMatrix.__init__(self, m, 0)
        self._max_col = m

    def set_val(self, i, j, new_val):
        '''(DiagonalMatrix, int, int, float) -> NoneType
        adds based on the rules of a Matrix'''
        if(self.in_bounds(i, j)):
            # checks that it's asking for diagonal
            if(i == j):
                # changes matrices
                SquareMatrix.set_val(self, i, j, new_val)
                OneDimensionalMatrix.set_item(self, i, new_val)
            else:
                val = 'This is a diagonal Matrix and its values'
                val = val + ' cannot be adjusted at: ' + str(i)
                val = val + ' : ' + str(j)
                raise MatrixInvalidOperationError(val)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j) + ', max col:'
            val = val + str(self._max_col)
            raise MatrixIndexError(val)

    def set_item(self, i, new_val):
        '''(DiagonalMatrix, int, float) -> NoneType
        adds item based on the rules of a OneDimensional Matrix'''
        if(self.in_bounds(i, i)):
            OneDimensionalMatrix.set_item(self, i, new_val)
            SquareMatrix.set_val(self, i, i, new_val)
        else:
            val = 'got row:' + str(i) + ', max size:' + str(self._max_row)
            raise MatrixIndexError(val)

    def get_val(self, i, j):
        '''(DiagonalMatrix, int, int) -> float
        Return the value of m[i,j] for this matrix m
        '''
        # deals with vertical case since this Matrix
        # stores in both vertical and diagonal
        ret = None
        if(i == j):
            SquareMatrix.get_val(self, i, j)
        else:
            return 0

    def get_row(self, i):
        '''(DiagonalMatrix, int) -> OneDimensionalMatrix
        deals with getting the row of a DiagonalMatrix'''
        ret = SquareMatrix.get_row(self, i)

        # checks for case where we are accessing 0
        # since I have values going down col 0
        if(i != 0):
            ret.set_val(0, 0)

        return ret

    def get_col(self, i):
        '''(Matrix, int) -> OneDimensionalMatrix
        deals with getting a column in DiagonalMatrix
        '''
        ret = None

        # if we're getting col 0 I need to send them just
        # the first value of the column since there are
        # other values in col 0
        if(i == 0):
            ret = OneDimensionalMatrix(len(self))
            ret.set_item(0, self.get_item(0))
        else:
            ret = SquareMatrix.get_col(self, i)

        return ret

    def set_row(self, i, new_row):
        '''(DiagonalMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_row()'''
        raise MatrixInvalidOperationError('invalid type')

    def set_col(self, i, new_row):
        '''(DiagonalMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_col()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_rows(self, i, j):
        '''(DiagonalMatrix, int, int) -> NoneType
        deals with swap_row()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_cols(self, i, j):
        '''(DiagonalMatrix, int, int) -> NoneType
        deals with swap_cols()'''
        raise MatrixInvalidOperationError('invalid type')

    def add_scalar(self, add_val):
        '''(DiagonalMatrix, int) -> Nonetype
        deals with add_sccalar'''
        raise MatrixInvalidOperationError('invalid type')

    def subtract_scalar(self, sub_val):
        '''(DiagonalMatrix, int) -> Nonetype
        deals with sub_scalar'''
        raise MatrixInvalidOperationError('invalid type')

    def add_matrix(self, add_Matrix):
        '''(DiagonalMatrix, Matrix) -> Nonetype
        deals with add_matrix'''
        raise MatrixInvalidOperationError('invalid type')


class IdentityMatrix(DiagonalMatrix):
    '''A matrix with 1s on the diagonal and 0s everywhere else'''

    def __init__(self, m):
        '''(Matrix, int) -> NoneType
        creates an identity matrix'''
        DiagonalMatrix.__init__(self, m)
        # fills the values with 1
        for a in range(0, m):
            DiagonalMatrix.set_val(self, a, a, 1)

    def set_val(self, i, j, val):
        '''(IdentityMatrix, int, int, float)
        deals with set_val'''
        raise MatrixInvalidOperationError('invalid type')
class MatrixIndexError(Exception):
    '''An attempt has been made to access an invalid index in this matrix'''
    def __init__(self, value):
        self.message = 'An attempt has been made to access an invalid index'
        self.message = self.message + 'in this matrix ' + str(value)

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


class MatrixNode():
    '''A general node class for a matrix'''

    def __init__(self, contents, right=None, down=None):
        '''(MatrixNode, obj, MatrixNode, MatrixNode) -> NoneType
        Create a new node holding contents, that is linked to right
        and down in a matrix
        '''
        self._contents = contents
        self._right = right
        self._down = down
        # added col and row nodes that direct where to find the row and col
        self._col = None
        self._row = None

    def __str__(self):
        '''(MatrixNode) -> str
        Return the string representation of this node
        '''
        return str(self._contents)

    def get_col(self):
        '''(MatrixNode) -> int
        returns the col value indicating the col position of the node

        REQ: self._col = MatrixNode'''
        # since col is a MatrixNode I just go and check for contents
        return self._col.get_contents()

    def get_col_node(self):
        '''(MatrixNode) -> MatrixNode
        returns the col node indicating the col position of the node'''
        return self._col

    def set_col(self, val):
        '''(MatrixNode, int) -> int
        sets the column value of the node'''
        self._col = val

    def set_row(self, val):
        '''(MatrixNode, int) -> int
        set the row value of the node'''
        self._row = val

    def get_row(self):
        '''(MatrixNode) -> str
        returns the row value indicating the row position of the node

        REQ: self._row = MatrixNode'''
        # since row is a MatrixNode I need to get the contents
        return self._row.get_contents()

    def get_row_node(self):
        '''(MatrixNode) -> MatrixNode
        returns the row node indicating the row position of the node'''
        return self._row

    def get_contents(self):
        '''(MatrixNode) -> obj
        Return the contents of this node
        '''
        return self._contents

    def set_contents(self, new_contents):
        '''(MatrixNode, obj) -> NoneType
        Set the contents of this node to new_contents
        '''
        self._contents = new_contents

    def get_right(self):
        '''(MatrixNode) -> MatrixNode
        Return the node to the right of this one
        '''
        return self._right

    def set_right(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set the new_node to be to the right of this one in the matrix
        '''
        self._right = new_node

    def add_right(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Adds the new_node to the right of this node if no node exists
        otherwise places new node to right and gives it it's children
        '''
        # grab the value to the right
        curr = self.get_right()
        if(curr is not None):
            # exists so we need to replace it
            new_node.set_right(curr)
            self.set_right(new_node)
        else:
            # doesn't exist
            self.set_right(new_node)

    def remove_right(self):
        '''(MatrixNode) -> NoneType
        removes the node to the right and replaces it with any children
        the right node has'''
        # checks to see if a right Node exists
        if(self._right is not None):
            # checks for children
            if(self._right._right is not None):
                self.set_right(self._right._right)
            else:
                self.set_right(None)

    def get_down(self):
        '''(MatrixNode) -> MatrixNode
        Return the node below this one
        '''
        return self._down

    def set_down(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set new_node to be below this one in the matrix
        '''
        self._down = new_node

    def add_down(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Adds the new_node to the bottom of this node if no node exists
        otherwise places new node to bottom and gives it it's children

        REQ: new_node.get_right() == None
        REQ: new_node.get_down() == None
        '''
        # grab the value to the right
        curr = self.get_down()
        if(curr is not None):
            # exists so we need to replace it
            new_node.set_down(curr)
            self.set_down(new_node)
        else:
            # doesn't exist
            self.set_down(new_node)

    def remove_down(self):
        '''(MatrixNode) -> NoneType
        removes the node to the bottom and replaces it with any children
        the node below has'''
        # checks whether down exists
        if(self._down is not None):
            # checks for children
            if(self._down._down is not None):
                self.set_down(self._down._down)
            else:
                self.set_down(None)


class Matrix():
    '''A class to represent a mathematical matrix'''

    def __init__(self, m, n, default=0):
        '''(Matrix, int, int, float) -> NoneType
        Create a new m x n matrix with all values set to default
        '''
        self._head = MatrixNode(None)
        # _max_row and _max_col are numbers to check and make sure that
        # the program does not go over the Matrix size
        self._max_row = m
        self._max_col = n
        self.default = default

    def _find_row(self, row_num):
        '''(Matrix, int, MatrixNode) -> MatrixNode
        Helper function that isolates the head where the row starts
        and returns it, if it's not found then it returns None'''
        ret = None
        curr = self._head.get_down()
        # loops until row num is greater
        while(curr is not None and curr.get_contents() < row_num):
            curr = curr.get_down()
        # checks for right row and returns appropriate decision
        if(curr is not None and curr.get_contents() == row_num):
            ret = curr
        return ret

    def _find_col(self, col_num):
        '''(Matrix, int, MatrixNode) -> MatrixNode
        Helper function that isolates the head where the row starts
        and returns it, if it's not found then it returns None'''
        ret = None
        curr = self._head.get_right()
        # loops until col num is greater
        while(curr is not None and curr.get_contents() < col_num):
            curr = curr.get_right()
        # checks for right col and returns appropriate decision
        if(curr is not None and curr.get_contents() == col_num):
            ret = curr
        return ret

    def _get_cell(self, i, j):
        '''(Matrix, int, int) -> MatrixNode
        Returns the cell at the position, if it doesn't exist then it
        returns None

        REQ: self.in_bounds(i, j) == True'''
        ret = None

        # sets curr as first row
        curr = self._head.get_down()
        if(curr is not None):
            # gets row
            curr = self._find_row(i)
            # checks to see if it found the row
            if(curr is not None):

                curr = curr.get_right()
                # searching for the value based on the col value in MatrixNode
                while(curr is not None and curr.get_col() < j):
                    curr = curr.get_right()

                # checks to see if it's found
                if(curr is not None and curr.get_col() == j):
                    ret = curr
                # not found
                else:
                    ret = None
            else:
                ret = None

        return ret

    def _remove(self, i, j):
        '''(Matrix, int, int) -> NoneType
        removes the selected node. this method is to increase efficiency
        This method is private as generally the Matrix will just return
        the default value'''
        # tries to get row
        row = self._find_row(i)
        temp_row = MatrixNode(None)

        if(row is not None):
            temp_row = row
            # recurses till it finds the col value to the right of the
            # current node
            while(row.get_right() is not None and
                  row.get_right().get_col() < j):
                row = row.get_right()

            # checks if they found the node
            if(row.get_right() is not None and row.get_right().get_col() == j):
                row.remove_right()

        # tries to get column
        col = self._find_col(j)
        temp_col = MatrixNode(None)

        if(col is not None):
            temp_col = col
            # recurses till it finds the row value under the current node
            while(col.get_down() is not None and
                  col.get_down().get_row() < i):
                col = col.get_down()

            # checks if program found node
            if(col.get_down() is not None and col.get_down().get_row() == i):
                col.remove_down()

        # uses previously saved temp_row/col values to go through and
        # eliminate any empty row/columns
        if(temp_row.get_right() == None):
            self._remove_row(i)
        if(temp_col.get_down() == None):
            self._remove_col(j)

    def _remove_row(self, i):
        '''(Matrix, int) -> NoneType
        Removes the row indicated as a pointer'''
        # loops and tries to find the row in question
        curr = self._head
        while(curr.get_down() is not None and
              curr.get_down().get_contents() < i):
            curr = curr.get_down()
        # checks if the node was found
        if(curr.get_down() is not None and
           curr.get_down().get_contents() == i):
            curr.remove_down()

    def _remove_col(self, j):
        '''(Matrix, int) -> NoneType
        Removes the col indicated as a pointer'''
        # loops and tries to find the column in question
        curr = self._head
        while(curr.get_right() is not None and
              curr.get_right().get_contents() < j):
            curr = curr.get_right()

        # checks if column was found
        if(curr.get_right() is not None and
           curr.get_right().get_contents() == j):
            curr.remove_right()

    def _add_to_row(self, i, j, cell):
        '''(Matrix, int, MatrixNode) -> NoneType
        a helper method that adds a new cell
        to a row if it exists and if it doesn't
        it creates a new one

        REQ: M(i, cell.get_col()) does not previously exist, that is
             _get_cell(i, j) == None
        REQ: in_bounds(i, j) == True'''
        # tries to find row
        row = self._find_row(i)

        # row is not found so we need to add row
        if(row is None):
            # we need to create a new row as it does not exist
            row = MatrixNode(i)
            # tries to order the row by finding the last row < i
            curr = self._head
            while(curr.get_down() is not None and
                  curr.get_down().get_contents() < i):
                curr = curr.get_down()
            # adds row
            curr.add_down(row)

        # tries to order the values by finding the last cell with col < j
        curr = row
        while(curr.get_right() is not None and curr.get_right().get_col() < j):
            curr = curr.get_right()
        curr.add_right(cell)

        # sets the row node of the cell
        cell.set_row(row)

    def _add_to_col(self, i, j, cell):
        '''(Matrix, int, MatrixNode) -> NoneType
        a helper method that adds a new cell
        to a col if it exists and if it doesn't
        it creates a new one

        REQ: M(cell.get_row(), j) does not previously exist, that is
             _get_cell(i, j) == None
        REQ: in_bounds(i, j) == True'''
        # tries to find column
        col = self._find_col(j)

        # column is not found
        if(col is None):
            # we need to create a new row as it does not exist
            col = MatrixNode(j)
            # tries to order the row by finding the last row < i
            curr = self._head
            while(curr.get_right() is not None and
                  curr.get_right().get_contents() < j):
                curr = curr.get_right()
            # adds row
            curr.add_right(col)

        # tries to order the values by finding the last cell with row < i
        curr = col
        while(curr.get_down() is not None and curr.get_down().get_row() < i):
            curr = curr.get_down()
        curr.add_down(cell)

        # sets the row node of the cell
        cell.set_col(col)

    def in_bounds(self, i, j):
        '''(Matrix, int, int) -> boolean
        returns a true if the value exists in the Matrix'''
        ret = False
        if(i < self._max_row and j < self._max_col and i >= 0 and j >= 0):
            ret = True
        return ret

    def set_val(self, i, j, new_val):
        '''(Matrix, int, int, float) -> NoneType
        Set the value of m[i,j] to new_val for this matrix m
        '''
        # checks if the search is in bounds
        if(self.in_bounds(i, j)):
            # attempts to get cell
            cell = self._get_cell(i, j)
            # cell is found we're done
            if(cell is not None):
                if(new_val == self.default):
                    self._remove(i, j)
                else:
                    cell.set_contents(new_val)
            # cell is not found so we need to add it
            else:
                if(new_val != self.default):
                    # creates cell
                    cell = MatrixNode(new_val)
                    # calls methods to add cell
                    self._add_to_row(i, j, cell)
                    self._add_to_col(i, j, cell)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

    def get_val(self, i, j):
        '''(Matrix, int, int) -> float
        Return the value of m[i,j] for this matrix m
        '''
        # checks if value is in matrix
        if(self.in_bounds(i, j)):
            # tries and find cell
            ret = self._get_cell(i, j)

            # checks if cell is different from default
            if(ret is not None):
                # is so it gets non-default value
                ret = ret.get_contents()
            else:
                ret = self.default

            return ret
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

    def get_row(self, row_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the row_num'th row of this matrix
        '''
        ret = None

        # insures that the row asked for is in the index
        if(self.in_bounds(row_num, 0)):
            # calls recursive helper to get the row asked
            row = self._find_row(row_num)

            # creates a default row
            ret = OneDimensionalMatrix(self._max_col, self.default)

            # None tells us that the row does not exist
            # and as such we just return the default OneDimensionalMatrix
            if(row is not None):
                # moves to first data
                curr = row.get_right()
                # fills OneDimensionalMatrix
                while(curr is not None):
                    ret.set_item(curr.get_col(), curr.get_contents())
                    curr = curr.get_right()
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

        return ret

    def set_row(self, row_num, new_row):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the row_num'th row of this matrix to those of new_row
        '''
        # checks that the row to be set is in bounds
        if(new_row is not None):
            if(self.in_bounds(row_num, len(new_row) - 1)):
                if(self.default == new_row.default):
                    # has to delete everything the row first
                    row = self._find_row(row_num)
                    while(row is not None and row.get_right() is not None):
                        curr = row.get_right()
                        self._remove(row_num, curr.get_col())

                    # gets items from row and puts them in matrix
                    curr = new_row.get_next_item()
                    while(curr is not None):
                        self.set_val(row_num, new_row.get_index(curr),
                                     curr.get_contents())
                        curr = new_row.get_next_item(curr)
                else:
                    i = row_num
                    new_row_values = new_row.get_list()
                    for x in range(0, len(new_row)):
                        self.set_val(i, x, new_row.get_item(x))
            else:
                val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
                val = val + ', got col:' + str(j)
                val = val + ', max col:' + str(self._max_col)
                raise MatrixIndexError(val)
        else:
            # erases row
            row = self._find_row(row_num)
            while(row is not None and row.get_right() is not None):
                curr = row.get_right()
                self._remove(row_num, curr.get_col())

    def get_col(self, col_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the col_num'th column of this matrix
        '''
        ret = None

        # insures that the column asked for is in the index
        if(self.in_bounds(0, col_num)):
            # calls recursive helper to get the row asked
            col = self._find_col(col_num)

            # creates a default row
            ret = OneDimensionalMatrix(self._max_row, self.default)

            # None tells us that the row does not exist
            # and as such we just return the default OneDimensionalMatrix
            if(col is not None):
                # moves to first data
                curr = col.get_down()
                # fills OneDimensionalMatrix
                while(curr is not None):
                    ret.set_item(curr.get_row(), curr.get_contents())
                    curr = curr.get_down()
        else:
            val = 'got col:' + str(col_num)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

        return ret

    def set_col(self, col_num, new_col):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the col_num'th column of this matrix to
        those of new_row '''
        # checks that the column to be set is in bounds
        if(new_col is not None):
            if(self.in_bounds(len(new_col) - 1, col_num)):
                if(self.default == new_col.default):
                    # has to delete everything the col first
                    col = self._find_col(col_num)
                    while(col is not None and col.get_down() is not None):
                        curr = col.get_down()
                        self._remove(curr.get_row(), col_num)

                    # gets items from column and puts them in matrix
                    curr = new_col.get_next_item()
                    while(curr is not None):
                        self.set_val(new_col.get_index(curr),
                                     col_num, curr.get_contents())
                        curr = new_col.get_next_item(curr)
                else:
                    i = col_num
                    new_col_values = new_col.get_list()
                    for x in range(0, len(new_col)):
                        self.set_val(x, i, new_col.get_item(x))
            else:
                val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
                val = val + ', got col:' + str(j)
                val = val + ', max col:' + str(self._max_col)
                raise MatrixIndexError(val)
        else:
            # erases column
            col = self._find_col(col_num)
            while(col is not None and col.get_down() is not None):
                curr = col.get_down()
                self._remove(curr.get_row(), col_num)

    def swap_rows(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of rows i and j in this matrix
        '''
        # checks for index error
        if(i < self._max_row and j < self._max_row):
            i_node = self._find_row(i)
            j_node = self._find_row(j)

            if(i_node is not None):
                # can find both i and j
                if(j_node is not None):
                    # replaces i with j and j with i
                    i_vector = self.get_row(i)
                    self.set_row(i, self.get_row(j))
                    self.set_row(j, i_vector)

                # can find only i
                else:
                    # replaces i in j spot and makes i empty
                    self.set_row(j, self.get_row(i))
                    self.set_row(i, None)

            # can only find j
            elif(j is not None):
                # replace j in i and makes j empty
                self.set_row(i, self.get_row(j))
                self.set_row(j, None)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j) + ', max col:'
            val = val + str(self._max_col)
            raise MatrixIndexError(val)

    def swap_cols(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of columns i and j in this matrix
        '''
        # checks for index error
        if(i < self._max_col and j < self._max_col):
            i_node = self._find_col(i)
            j_node = self._find_col(j)

            if(i_node is not None):
                # can find both i and j
                if(j_node is not None):
                    # replaces i with j and j with i
                    i_vector = self.get_col(i)
                    self.set_col(i, self.get_col(j))
                    self.set_col(j, i_vector)

                # can find only i
                else:
                    # replaces i in j spot and makes i empty
                    self.set_col(j, self.get_col(i))
                    self.set_col(i, None)

            # can only find j
            elif(j is not None):
                # replace j in i and makes j empty
                self.set_col(i, self.get_col(j))
                self.set_col(j, None)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j) + ', max col:'
            val = val + str(self._max_col)
            raise MatrixIndexError(val)

    def add_scalar(self, add_value):
        '''(Matrix, float) -> NoneType
        Increase all values in this matrix by add_value
        '''
        # changes default values
        self.default = self.default + add_value

        # gets first row
        curr_row = self._head.get_down()
        while(curr_row is not None):
            # gets first cell
            curr = curr_row.get_right()
            while(curr is not None):
                # gets cell value and changes it
                val = curr.get_contents()
                curr.set_contents(val + add_value)
                # goes to next cell
                curr = curr.get_right()
            # goes to next row
            curr_row = curr_row.get_down()

    def subtract_scalar(self, sub_value):
        '''(Matrix, float) -> NoneType
        Decrease all values in this matrix by sub_value
        '''
        # changes default values
        self.default = self.default - sub_value

        # gets first row
        curr_row = self._head.get_down()
        while(curr_row is not None):
            # gets first cell
            curr = curr_row.get_right()
            while(curr is not None):
                # gets cell value and changes it
                val = curr.get_contents()
                curr.set_contents(val - sub_value)
                # goes to next cell
                curr = curr.get_right()
            # goes to next row
            curr_row = curr_row.get_down()

    def multiply_scalar(self, mult_value):
        '''(Matrix, float) -> NoneType
        Multiply all values in this matrix by mult_value
        '''
        # changes default values
        self.default = self.default * mult_value

        # gets first row
        curr_row = self._head.get_down()
        while(curr_row is not None):
            # gets first cell
            curr = curr_row.get_right()
            while(curr is not None):
                # gets cell value and changes it
                val = curr.get_contents()
                curr.set_contents(val * mult_value)
                # goes to next cell
                curr = curr.get_right()
            # goes to next row
            curr_row = curr_row.get_down()

    def get_default(self):
        '''(Matrix) -> float
        returns the default value'''
        return self.default

    def get_first_row(self):
        '''(Matrix) -> MatrixNode
        returns the first row'''
        return self._head.get_down()

    def get_first_col(self):
        '''(Matrix) -> MatrixNode
        returns the frist col'''
        return self._head.get_right()

    def get_dimensions(self):
        '''(Matrix) -> (int, int)
        returns the max row,col of the matrix'''
        return (self._max_row, self._max_col)

    def add_matrix(self, adder_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the sum of this matrix and adder_matrix
        '''
        # check dimensions
        if(adder_matrix.get_dimensions() == self.get_dimensions()):
            # create a new matrix
            default = self.default + adder_matrix.get_default()
            M = Matrix(self._max_row, self._max_col, default)

            # gets default for use later
            default = adder_matrix.get_default()

            # get the first row of values
            row_1 = self._head.get_down()
            row_2 = adder_matrix.get_first_row()

            # keeps looping while there still exists both rows
            while(row_1 is not None and row_2 is not None):
                # checks the relationship of the rows
                if(row_1.get_contents() == row_2.get_contents()):
                    # they are equal so we need to consider the case
                    # that some numbers are the same
                    self._add_matrix(M, [row_1, row_2], self.default, default)
                    # iterates
                    row_1 = row_1.get_down()
                    row_2 = row_2.get_down()
                elif(row_1.get_contents() < row_2.get_contents()):
                    # only uses row1
                    self._add_matrix(M, [row_1], default)
                    row_1 = row_1.get_down()
                else:
                    # only uses row2
                    self._add_matrix(M, [row_2], self.default)
                    row_2 = row_2.get_down()

            while(row_1 is not None):
                # only uses row1 since only row_1 exists
                self._add_matrix(M, [row_1], default)
                row_1 = row_1.get_down()

            while(row_2 is not None):
                # only uses row2
                self._add_matrix(M, [row_2], self.default)
                row_2 = row_2.get_down()

            return M
        else:
            val = 'This Matrix dimensions: ' + self.get_dimensions()
            val = val + ', adding matrix dimensions: '
            val = val + adder_matrix.get_dimensions()
            raise MatrixDimensionError(val)

    def _add_matrix(self, M, row_nodes, default1, default2=None):
        '''(Matrix, Matrix, list of MatrixNode, float, float)-> NoneType
        helper method to add_matrix, deals with case
        of list having a length of 1 or 2

        REQ: len(row_node) == 1 or  len(row_node) == 2
        REQ: row_nodes[0] is not None'''
        # case where there is more than one row
        if(len(row_nodes) > 1):
            # gets rows
            row1 = row_nodes[0].get_right()
            row2 = row_nodes[1].get_right()
            row_val = row1.get_row()

            # goes through all the columns
            while(row1 is not None and row2 is not None):
                # checks where the rows are in terms of column
                if(row1.get_col() == row2.get_col()):
                    # same place so we add both together
                    val1 = row1.get_contents()
                    val2 = row2.get_contents()

                    M.set_val(row_val, row1.get_col(), (val1 + val2))
                    # iterates
                    row1 = row1.get_right()
                    row2 = row2.get_right()
                elif(row1.get_col() < row2.get_col()):
                    # row1 is smaller so we add it first
                    val1 = row1.get_contents()
                    # add default of second matrix as well
                    M.set_val(row_val, row1.get_col(), (val1 + default2))
                    row1 = row1.get_right()
                else:
                    # row2 is smaller so we add it first
                    val1 = row2.get_contents()
                    M.set_val(row_val, row2.get_col(), (val1 + default1))
                    row2 = row2.get_right()

            while(row1 is not None):
                # only row1 exists
                val1 = row1.get_contents()
                M.set_val(row_val, row1.get_col(), (val1 + default2))
                row1 = row1.get_right()

            while(row2 is not None):
                # only row2 exists
                val1 = row2.get_contents()
                M.set_val(row_val, row2.get_col(), (val1 + default1))
                row2 = row2.get_right()

        else:
            # only one row was passed
            row = row_nodes[0]
            curr = row.get_right()
            while(curr is not None):
                M.set_val(row.get_contents(),
                          curr.get_col(), (curr.get_contents() + default1))
                curr = curr.get_right()

    def dot_product(self, row1, row2):
        '''(Matrix, OneDimensionalMatrix, OneDimensionalMatrix) -> float
        returns the dotproduct of two vectors, returns zero
        in all other situations'''
        ret = 0
        # goes through all the cells and adds them to total
        # only if the lengths are the same
        if(len(row1) == len(row2)):
            for a in range(0, len(row1)):
                ret = ret + (row1.get_item(a)*row2.get_item(a))
        else:
            val = 'given unequal lengths: ' + len(row1) + ' : ' + len(row2)
            raise MatrixDimensionError(val)

        return ret

    def multiply_matrix(self, mult_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the product of this matrix and mult_matrix
        '''
        M = None
        if(mult_matrix is not None):
            # gets row/col of matrix to multiply
            rows = None
            cols = None
            (rows, cols) = mult_matrix.get_dimensions()
            # check whether this is a valid multiplication
            if(self._max_col == rows):
                # creates matrix
                M = Matrix(self._max_row, cols, self.default)

                # goes through all columns and rows
                for x in range(0, self._max_row):
                    vector1 = self.get_row(x)
                    for y in range(0, cols):
                        vector2 = mult_matrix.get_col(y)
                        val = self.dot_product(vector1, vector2)
                        M.set_val(x, y, val)

                return M
            else:
                val = 'col: ' + str(self._max_col) + ', does not equal'
                val = val + ' col: ' + str(rows) + ' to make a valid'
                val = val + ' matrix multiplication'
                raise MatrixDimensionError(val)


class OneDimensionalMatrix(Matrix):
    '''A 1xn or nx1 matrix.
    (For the purposes of multiplication, we assume it's 1xn)'''
    def __init__(self, m, default=0):
        '''(OneDimensionalMatrix, int, boolean, float)
        A representation of a OneDimensionalMatrix that uses Matrix
        to help fill its methods'''
        Matrix.__init__(self, m, m, default)
        self._length = m

    def get_list(self):
        '''(OneDimensionalMatrix) -> list of float
        returns the list representation of the OneDimensionalMatrix'''
        # create array of length with default variables
        ret = []
        for a in range(0, len(self)):
            ret[a] = self.default

        # fills in different variables
        if(self._head.get_down() is not None):
            curr = self._head.get_down().get_right()
            while(curr is not None):
                ret[curr.get_row()] = curr.get_contents()

        return ret

    def __len__(self):
        '''(OneDimensionalMatrix) -> int
        returns the length of the OneDimensionalMatrix'''
        return self._length

    def get_index(self, cell):
        '''(OneDimensionalMatrix) -> int
        returns the spot the value is in'''
        return cell.get_row()

    def get_item(self, i):
        '''(OneDimensionalMatrix, int) -> float
        Return the i'th item in this matrix
        '''
        ret = self.default
        row = self._find_row(i)
        # tries to find row and if it does not then it returns default value
        if(row is not None):
            ret = row.get_right().get_contents()

        return ret

    def get_next_item(self, node=None):
        '''(OneDimensionalMatrix, MatrixNode) -> MatrixNode
        based on this one dimensional array we return the Node
        that appears next
        REQ: type(node) == MatrixNode'''
        ret = None
        # None means that we want first
        if(node is None):
            # checks if there are any nodes
            if(self._head.get_down() is not None):
                ret = self._head.get_down().get_right()
        else:
            # returns the node below
            ret = node.get_down()

        return ret

    def get_val(self, i, j):
        '''(OneDimensionalMatrix(), int, int) -> float
        a method that insures OneDiemnsionalMatrix does not error
        during a call'''
        ret = None
        # checks if i is in domain
        if(i < self.get_max_row):
            # checks if they are trying to access a row
            if(j == 0):
                ret = self.get_item(i)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        # checks for j in domain
        elif(j < self.get_max_row):
            # checks if they are trying acces a row
            if(i == 0):
                ret = self.get_item(j)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        else:
            val = 'got:' + str(i) + ', ' + str(j) + ', max is:'
            val = val + str(self._max_row)
            raise MatrixIndexError(val)

        return ret

    def set_val(self, i, j, new_val):
        '''(OneDimensionalMatrix(), int, int) -> float
        a method that insures OneDimensionalMatrix does not error
        '''
        # checks for i > j case
        if(i < self._max_row):
            # checks if they are trying to access a row
            if(j == 0):
                self.set_item(i, new_val)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        # checks for j > i case
        elif(j < self.get_max_row):
            # checks if they are trying to access a row
            if(i == 0):
                self.set_item(i, new_val)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        else:
            val = 'got:' + str(i) + ', ' + str(j) + ', max is:'
            val = val + str(self._max_row)
            raise MatrixIndexError(val)

    def set_item(self, i, new_val):
        '''(OneDimensionalMatrix, int, float) -> NoneType
        Set the i'th item in this matrix to new_val
        '''
        # checks for bounds
        if(self.in_bounds(i, 0)):
            # tries to find row
            row = self._find_row(i)
            # checks if value is default
            if(new_val == self.default):
                # if it is then we need to worry about case of
                # deletion
                if(row is not None):
                    self._remove(i, 0)
                # we don't need to worry about non-existant since
                # it is already default
            else:
                if(row is not None):
                    # changes value
                    row.get_right().set_contents(new_val)
                else:
                    # creates a new value and adds it
                    cell = MatrixNode(new_val)
                    self._add_to_row(i, 0, cell)
                    self._add_to_col(i, 0, cell)

        else:
            val = 'got:' + str(i) + ', max is:'
            val = val + str(self._max_row)
            raise MatrixIndexError(val)

    def multiply_matrix(self, mult_matrix):
        '''(OneDimensionalMatrix, Matrix) -> Matrix
        since I store my vector as just a column I need
        to create a case when we multiply it'''
        M = None
        col_size = None
        row_size = None
        # checks the dimensions
        (row_size, col_size) = mult_matrix.get_dimensions()
        if(self._max_row == row_size):
            # creates array which will be the result
            M = OneDimensionalMatrix(col_size, self.default)
            # goes through all the columns
            curr = mult_matrix
            for a in range(0, col_size):
                curr = curr.get_col(a)
                # sends itself since it is a OneDimensionalMatrix
                M.set_item(a, self.dot_product(self, curr))

            return M
        else:
            val = 'col: ' + str(self._max_col) + ', does not equal'
            val = val + ' col: ' + str(rows) + ' to make a valid'
            val = val + ' matrix multiplication'
            raise MatrixDimensionError(val)


class SquareMatrix(Matrix):
    '''A matrix where the number of rows and columns are equal'''

    def __init__(self, m, default=0):
        '''(SquareMatrix, int, float) -> NoneType
        creates a SquareMatrix'''
        Matrix.__init__(self, m, m, default)

    def transpose(self):
        '''(SquareMatrix) -> NoneType
        Transpose this matrix
        '''
        # goes through and transposes by turning the pointer right-down into
        # down-right since transpose is just i,j -> j,i
        row = self._head
        # starts with head node as it needs to be switched as well

        while(row is not None):
            curr = row
            while(curr is not None):
                # starts going through the columns and switching rows to
                # columns and columns to rows
                temp = curr.get_down()
                curr.set_down(curr.get_right())
                curr.set_right(temp)
                # changes col/row indicators
                temp = curr.get_col_node()
                curr.set_col(curr.get_row_node())
                curr.set_row(temp)
                # columns are now rows so it goes to next column
                curr = curr.get_down()
            # rows are now columns so it gets from columns
            # in order to progress down the rows
            row = row.get_right()

    def get_diagonal(self):
        '''(Squarematrix) -> OneDimensionalMatrix
        Return a one dimensional matrix with the values of the diagonal
        of this matrix
        '''
        M = OneDimensionalMatrix(self._max_row, self.default)
        # gets first calue and gets the index to find
        row = self._head.get_down()
        val_check = row.get_contents()
        # goes through all rows
        while(row is not None):
            curr = row.get_right()
            # goes through columns until it reaches a number greater or
            # the end of the column nodes
            while(curr is not None and curr.get_col() < val_check):
                curr = curr.get_right()

            # checks for right node before adding
            if(curr is not None and curr.get_col() == val_check):
                M.set_item(val_check, curr.get_contents())

            # iterates rows and sets next index
            row = row.get_down()
            if(row is not None):
                val_check = row.get_contents()

        return M

    def set_diagonal(self, new_diagonal):
        '''(SquareMatrix, OneDimensionalMatrix) -> NoneType
        Set the values of the diagonal of this matrix to those of new_diagonal
        '''
        # check the dimensions
        if(len(new_diagonal) == self._max_row):
            # checks the default values
            if(new_diagonal.get_default() == self.default):
                # default values are the same so we only need to add
                # unique values
                # gets the first item and sets it
                curr = new_diagonal.get_next_item()
                while(curr is not None):
                    # sets value and asks for next unique value
                    index = curr.get_row()
                    self.set_val(index, index, curr.get_contents())
                    curr = new_diagonal.get_next_item(curr)
            else:
                # set the entire diagonal as new since default
                # is not the same
                for a in range(0, len(new_diagonal)):
                    self.set_val(a, a, new_diagonal.get_item(a))

        else:
            val = 'The length of the OneDimensionalMatrices are not equal'
            raise MatrixDimensionError(val)


class SymmetricMatrix(SquareMatrix):
    '''A Symmetric Matrix, where m[i, j] = m[j, i] for all i and j'''

    def __init__(self, m, default=0):
        '''(SymmetricMatrix, int, float) ->NoneType
        create a new symmetric matrix'''
        SquareMatrix.__init__(self, m, default)

    def set_val(self, m, n, val):
        '''(SymmetricMatrix, int, int, float)
        insures all values are symmetric'''
        SquareMatrix.set_val(m, n, val)
        SquareMatrix.set_val(n, m, val)

    def set_row(self, i, new_row):
        '''(SymmetricMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_row()
        '''
        raise MatrixInvalidOperationError('invalid type')

    def set_col(self, i, new_row):
        '''(SymmetricMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_col()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_rows(self, i, j):
        '''(SymmetricMatrix, int, int) -> NoneType
        deals with swap_row()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_cols(self, i, j):
        '''(SymmetricMatrix, int, int) -> NoneType
        deals with swap_cols()'''
        raise MatrixInvalidOperationError('invalid type')

    def add_scalar(self, add_val):
        '''(SymmetricMatrix, int) -> Nonetype
        deals with add_sccalar'''
        raise MatrixInvalidOperationError('invalid type')

    def subtract_scalar(self, sub_val):
        '''(SymmetricMatrix, int) -> Nonetype
        deals with sub_scalar'''
        raise MatrixInvalidOperationError('invalid type')


class DiagonalMatrix(SquareMatrix, OneDimensionalMatrix):
    '''A square matrix with 0 values everywhere but the diagonal'''

    def __init__(self, m, default=0):
        '''(DiagonalMatrix, int) -> NoneType
        Creates a diagonal matrix'''
        OneDimensionalMatrix.__init__(self, m, 0)
        SquareMatrix.__init__(self, m, 0)
        self._max_col = m

    def set_val(self, i, j, new_val):
        '''(DiagonalMatrix, int, int, float) -> NoneType
        adds based on the rules of a Matrix'''
        if(self.in_bounds(i, j)):
            # checks that it's asking for diagonal
            if(i == j):
                # changes matrices
                SquareMatrix.set_val(self, i, j, new_val)
                OneDimensionalMatrix.set_item(self, i, new_val)
            else:
                val = 'This is a diagonal Matrix and its values'
                val = val + ' cannot be adjusted at: ' + str(i)
                val = val + ' : ' + str(j)
                raise MatrixInvalidOperationError(val)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j) + ', max col:'
            val = val + str(self._max_col)
            raise MatrixIndexError(val)

    def set_item(self, i, new_val):
        '''(DiagonalMatrix, int, float) -> NoneType
        adds item based on the rules of a OneDimensional Matrix'''
        if(self.in_bounds(i, i)):
            OneDimensionalMatrix.set_item(self, i, new_val)
            SquareMatrix.set_val(self, i, i, new_val)
        else:
            val = 'got row:' + str(i) + ', max size:' + str(self._max_row)
            raise MatrixIndexError(val)

    def get_val(self, i, j):
        '''(DiagonalMatrix, int, int) -> float
        Return the value of m[i,j] for this matrix m
        '''
        # deals with vertical case since this Matrix
        # stores in both vertical and diagonal
        ret = None
        if(i == j):
            SquareMatrix.get_val(self, i, j)
        else:
            return 0

    def get_row(self, i):
        '''(DiagonalMatrix, int) -> OneDimensionalMatrix
        deals with getting the row of a DiagonalMatrix'''
        ret = SquareMatrix.get_row(self, i)

        # checks for case where we are accessing 0
        # since I have values going down col 0
        if(i != 0):
            ret.set_val(0, 0)

        return ret

    def get_col(self, i):
        '''(Matrix, int) -> OneDimensionalMatrix
        deals with getting a column in DiagonalMatrix
        '''
        ret = None

        # if we're getting col 0 I need to send them just
        # the first value of the column since there are
        # other values in col 0
        if(i == 0):
            ret = OneDimensionalMatrix(len(self))
            ret.set_item(0, self.get_item(0))
        else:
            ret = SquareMatrix.get_col(self, i)

        return ret

    def set_row(self, i, new_row):
        '''(DiagonalMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_row()'''
        raise MatrixInvalidOperationError('invalid type')

    def set_col(self, i, new_row):
        '''(DiagonalMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_col()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_rows(self, i, j):
        '''(DiagonalMatrix, int, int) -> NoneType
        deals with swap_row()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_cols(self, i, j):
        '''(DiagonalMatrix, int, int) -> NoneType
        deals with swap_cols()'''
        raise MatrixInvalidOperationError('invalid type')

    def add_scalar(self, add_val):
        '''(DiagonalMatrix, int) -> Nonetype
        deals with add_sccalar'''
        raise MatrixInvalidOperationError('invalid type')

    def subtract_scalar(self, sub_val):
        '''(DiagonalMatrix, int) -> Nonetype
        deals with sub_scalar'''
        raise MatrixInvalidOperationError('invalid type')

    def add_matrix(self, add_Matrix):
        '''(DiagonalMatrix, Matrix) -> Nonetype
        deals with add_matrix'''
        raise MatrixInvalidOperationError('invalid type')


class IdentityMatrix(DiagonalMatrix):
    '''A matrix with 1s on the diagonal and 0s everywhere else'''

    def __init__(self, m):
        '''(Matrix, int) -> NoneType
        creates an identity matrix'''
        DiagonalMatrix.__init__(self, m)
        # fills the values with 1
        for a in range(0, m):
            DiagonalMatrix.set_val(self, a, a, 1)

    def set_val(self, i, j, val):
        '''(IdentityMatrix, int, int, float)
        deals with set_val'''
        raise MatrixInvalidOperationError('invalid type')


class MatrixIndexError(Exception):
    '''An attempt has been made to access an invalid index in this matrix'''
    def __init__(self, value):
        self.message = 'An attempt has been made to access an invalid index'
        self.message = self.message + 'in this matrix ' + str(value)

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


class MatrixNode():
    '''A general node class for a matrix'''

    def __init__(self, contents, right=None, down=None):
        '''(MatrixNode, obj, MatrixNode, MatrixNode) -> NoneType
        Create a new node holding contents, that is linked to right
        and down in a matrix
        '''
        self._contents = contents
        self._right = right
        self._down = down
        # added col and row nodes that direct where to find the row and col
        self._col = None
        self._row = None

    def __str__(self):
        '''(MatrixNode) -> str
        Return the string representation of this node
        '''
        return str(self._contents)

    def get_col(self):
        '''(MatrixNode) -> int
        returns the col value indicating the col position of the node

        REQ: self._col = MatrixNode'''
        # since col is a MatrixNode I just go and check for contents
        return self._col.get_contents()

    def get_col_node(self):
        '''(MatrixNode) -> MatrixNode
        returns the col node indicating the col position of the node'''
        return self._col

    def set_col(self, val):
        '''(MatrixNode, int) -> int
        sets the column value of the node'''
        self._col = val

    def set_row(self, val):
        '''(MatrixNode, int) -> int
        set the row value of the node'''
        self._row = val

    def get_row(self):
        '''(MatrixNode) -> str
        returns the row value indicating the row position of the node

        REQ: self._row = MatrixNode'''
        # since row is a MatrixNode I need to get the contents
        return self._row.get_contents()

    def get_row_node(self):
        '''(MatrixNode) -> MatrixNode
        returns the row node indicating the row position of the node'''
        return self._row

    def get_contents(self):
        '''(MatrixNode) -> obj
        Return the contents of this node
        '''
        return self._contents

    def set_contents(self, new_contents):
        '''(MatrixNode, obj) -> NoneType
        Set the contents of this node to new_contents
        '''
        self._contents = new_contents

    def get_right(self):
        '''(MatrixNode) -> MatrixNode
        Return the node to the right of this one
        '''
        return self._right

    def set_right(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set the new_node to be to the right of this one in the matrix
        '''
        self._right = new_node

    def add_right(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Adds the new_node to the right of this node if no node exists
        otherwise places new node to right and gives it it's children
        '''
        # grab the value to the right
        curr = self.get_right()
        if(curr is not None):
            # exists so we need to replace it
            new_node.set_right(curr)
            self.set_right(new_node)
        else:
            # doesn't exist
            self.set_right(new_node)

    def remove_right(self):
        '''(MatrixNode) -> NoneType
        removes the node to the right and replaces it with any children
        the right node has'''
        # checks to see if a right Node exists
        if(self._right is not None):
            # checks for children
            if(self._right._right is not None):
                self.set_right(self._right._right)
            else:
                self.set_right(None)

    def get_down(self):
        '''(MatrixNode) -> MatrixNode
        Return the node below this one
        '''
        return self._down

    def set_down(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set new_node to be below this one in the matrix
        '''
        self._down = new_node

    def add_down(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Adds the new_node to the bottom of this node if no node exists
        otherwise places new node to bottom and gives it it's children

        REQ: new_node.get_right() == None
        REQ: new_node.get_down() == None
        '''
        # grab the value to the right
        curr = self.get_down()
        if(curr is not None):
            # exists so we need to replace it
            new_node.set_down(curr)
            self.set_down(new_node)
        else:
            # doesn't exist
            self.set_down(new_node)

    def remove_down(self):
        '''(MatrixNode) -> NoneType
        removes the node to the bottom and replaces it with any children
        the node below has'''
        # checks whether down exists
        if(self._down is not None):
            # checks for children
            if(self._down._down is not None):
                self.set_down(self._down._down)
            else:
                self.set_down(None)


class Matrix():
    '''A class to represent a mathematical matrix'''

    def __init__(self, m, n, default=0):
        '''(Matrix, int, int, float) -> NoneType
        Create a new m x n matrix with all values set to default
        '''
        self._head = MatrixNode(None)
        # _max_row and _max_col are numbers to check and make sure that
        # the program does not go over the Matrix size
        self._max_row = m
        self._max_col = n
        self.default = default

    def _find_row(self, row_num):
        '''(Matrix, int, MatrixNode) -> MatrixNode
        Helper function that isolates the head where the row starts
        and returns it, if it's not found then it returns None'''
        ret = None
        curr = self._head.get_down()
        # loops until row num is greater
        while(curr is not None and curr.get_contents() < row_num):
            curr = curr.get_down()
        # checks for right row and returns appropriate decision
        if(curr is not None and curr.get_contents() == row_num):
            ret = curr
        return ret

    def _find_col(self, col_num):
        '''(Matrix, int, MatrixNode) -> MatrixNode
        Helper function that isolates the head where the row starts
        and returns it, if it's not found then it returns None'''
        ret = None
        curr = self._head.get_right()
        # loops until col num is greater
        while(curr is not None and curr.get_contents() < col_num):
            curr = curr.get_right()
        # checks for right col and returns appropriate decision
        if(curr is not None and curr.get_contents() == col_num):
            ret = curr
        return ret

    def _get_cell(self, i, j):
        '''(Matrix, int, int) -> MatrixNode
        Returns the cell at the position, if it doesn't exist then it
        returns None

        REQ: self.in_bounds(i, j) == True'''
        ret = None

        # sets curr as first row
        curr = self._head.get_down()
        if(curr is not None):
            # gets row
            curr = self._find_row(i)
            # checks to see if it found the row
            if(curr is not None):

                curr = curr.get_right()
                # searching for the value based on the col value in MatrixNode
                while(curr is not None and curr.get_col() < j):
                    curr = curr.get_right()

                # checks to see if it's found
                if(curr is not None and curr.get_col() == j):
                    ret = curr
                # not found
                else:
                    ret = None
            else:
                ret = None

        return ret

    def _remove(self, i, j):
        '''(Matrix, int, int) -> NoneType
        removes the selected node. this method is to increase efficiency
        This method is private as generally the Matrix will just return
        the default value'''
        # tries to get row
        row = self._find_row(i)
        temp_row = MatrixNode(None)

        if(row is not None):
            temp_row = row
            # recurses till it finds the col value to the right of the
            # current node
            while(row.get_right() is not None and
                  row.get_right().get_col() < j):
                row = row.get_right()

            # checks if they found the node
            if(row.get_right() is not None and row.get_right().get_col() == j):
                row.remove_right()

        # tries to get column
        col = self._find_col(j)
        temp_col = MatrixNode(None)

        if(col is not None):
            temp_col = col
            # recurses till it finds the row value under the current node
            while(col.get_down() is not None and
                  col.get_down().get_row() < i):
                col = col.get_down()

            # checks if program found node
            if(col.get_down() is not None and col.get_down().get_row() == i):
                col.remove_down()

        # uses previously saved temp_row/col values to go through and
        # eliminate any empty row/columns
        if(temp_row.get_right() == None):
            self._remove_row(i)
        if(temp_col.get_down() == None):
            self._remove_col(j)

    def _remove_row(self, i):
        '''(Matrix, int) -> NoneType
        Removes the row indicated as a pointer'''
        # loops and tries to find the row in question
        curr = self._head
        while(curr.get_down() is not None and
              curr.get_down().get_contents() < i):
            curr = curr.get_down()
        # checks if the node was found
        if(curr.get_down() is not None and
           curr.get_down().get_contents() == i):
            curr.remove_down()

    def _remove_col(self, j):
        '''(Matrix, int) -> NoneType
        Removes the col indicated as a pointer'''
        # loops and tries to find the column in question
        curr = self._head
        while(curr.get_right() is not None and
              curr.get_right().get_contents() < j):
            curr = curr.get_right()

        # checks if column was found
        if(curr.get_right() is not None and
           curr.get_right().get_contents() == j):
            curr.remove_right()

    def _add_to_row(self, i, j, cell):
        '''(Matrix, int, MatrixNode) -> NoneType
        a helper method that adds a new cell
        to a row if it exists and if it doesn't
        it creates a new one

        REQ: M(i, cell.get_col()) does not previously exist, that is
             _get_cell(i, j) == None
        REQ: in_bounds(i, j) == True'''
        # tries to find row
        row = self._find_row(i)

        # row is not found so we need to add row
        if(row is None):
            # we need to create a new row as it does not exist
            row = MatrixNode(i)
            # tries to order the row by finding the last row < i
            curr = self._head
            while(curr.get_down() is not None and
                  curr.get_down().get_contents() < i):
                curr = curr.get_down()
            # adds row
            curr.add_down(row)

        # tries to order the values by finding the last cell with col < j
        curr = row
        while(curr.get_right() is not None and curr.get_right().get_col() < j):
            curr = curr.get_right()
        curr.add_right(cell)

        # sets the row node of the cell
        cell.set_row(row)

    def _add_to_col(self, i, j, cell):
        '''(Matrix, int, MatrixNode) -> NoneType
        a helper method that adds a new cell
        to a col if it exists and if it doesn't
        it creates a new one

        REQ: M(cell.get_row(), j) does not previously exist, that is
             _get_cell(i, j) == None
        REQ: in_bounds(i, j) == True'''
        # tries to find column
        col = self._find_col(j)

        # column is not found
        if(col is None):
            # we need to create a new row as it does not exist
            col = MatrixNode(j)
            # tries to order the row by finding the last row < i
            curr = self._head
            while(curr.get_right() is not None and
                  curr.get_right().get_contents() < j):
                curr = curr.get_right()
            # adds row
            curr.add_right(col)

        # tries to order the values by finding the last cell with row < i
        curr = col
        while(curr.get_down() is not None and curr.get_down().get_row() < i):
            curr = curr.get_down()
        curr.add_down(cell)

        # sets the row node of the cell
        cell.set_col(col)

    def in_bounds(self, i, j):
        '''(Matrix, int, int) -> boolean
        returns a true if the value exists in the Matrix'''
        ret = False
        if(i < self._max_row and j < self._max_col and i >= 0 and j >= 0):
            ret = True
        return ret

    def set_val(self, i, j, new_val):
        '''(Matrix, int, int, float) -> NoneType
        Set the value of m[i,j] to new_val for this matrix m
        '''
        # checks if the search is in bounds
        if(self.in_bounds(i, j)):
            # attempts to get cell
            cell = self._get_cell(i, j)
            # cell is found we're done
            if(cell is not None):
                if(new_val == self.default):
                    self._remove(i, j)
                else:
                    cell.set_contents(new_val)
            # cell is not found so we need to add it
            else:
                if(new_val != self.default):
                    # creates cell
                    cell = MatrixNode(new_val)
                    # calls methods to add cell
                    self._add_to_row(i, j, cell)
                    self._add_to_col(i, j, cell)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

    def get_val(self, i, j):
        '''(Matrix, int, int) -> float
        Return the value of m[i,j] for this matrix m
        '''
        # checks if value is in matrix
        if(self.in_bounds(i, j)):
            # tries and find cell
            ret = self._get_cell(i, j)

            # checks if cell is different from default
            if(ret is not None):
                # is so it gets non-default value
                ret = ret.get_contents()
            else:
                ret = self.default

            return ret
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

    def get_row(self, row_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the row_num'th row of this matrix
        '''
        ret = None

        # insures that the row asked for is in the index
        if(self.in_bounds(row_num, 0)):
            # calls recursive helper to get the row asked
            row = self._find_row(row_num)

            # creates a default row
            ret = OneDimensionalMatrix(self._max_col, self.default)

            # None tells us that the row does not exist
            # and as such we just return the default OneDimensionalMatrix
            if(row is not None):
                # moves to first data
                curr = row.get_right()
                # fills OneDimensionalMatrix
                while(curr is not None):
                    ret.set_item(curr.get_col(), curr.get_contents())
                    curr = curr.get_right()
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

        return ret

    def set_row(self, row_num, new_row):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the row_num'th row of this matrix to those of new_row
        '''
        # checks that the row to be set is in bounds
        if(new_row is not None):
            if(self.in_bounds(row_num, len(new_row) - 1)):
                if(self.default == new_row.default):
                    # has to delete everything the row first
                    row = self._find_row(row_num)
                    while(row is not None and row.get_right() is not None):
                        curr = row.get_right()
                        self._remove(row_num, curr.get_col())

                    # gets items from row and puts them in matrix
                    curr = new_row.get_next_item()
                    while(curr is not None):
                        self.set_val(row_num, new_row.get_index(curr),
                                     curr.get_contents())
                        curr = new_row.get_next_item(curr)
                else:
                    i = row_num
                    new_row_values = new_row.get_list()
                    for x in range(0, len(new_row)):
                        self.set_val(i, x, new_row.get_item(x))
            else:
                val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
                val = val + ', got col:' + str(j)
                val = val + ', max col:' + str(self._max_col)
                raise MatrixIndexError(val)
        else:
            # erases row
            row = self._find_row(row_num)
            while(row is not None and row.get_right() is not None):
                curr = row.get_right()
                self._remove(row_num, curr.get_col())

    def get_col(self, col_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the col_num'th column of this matrix
        '''
        ret = None

        # insures that the column asked for is in the index
        if(self.in_bounds(0, col_num)):
            # calls recursive helper to get the row asked
            col = self._find_col(col_num)

            # creates a default row
            ret = OneDimensionalMatrix(self._max_row, self.default)

            # None tells us that the row does not exist
            # and as such we just return the default OneDimensionalMatrix
            if(col is not None):
                # moves to first data
                curr = col.get_down()
                # fills OneDimensionalMatrix
                while(curr is not None):
                    ret.set_item(curr.get_row(), curr.get_contents())
                    curr = curr.get_down()
        else:
            val = 'got col:' + str(col_num)
            val = val + ', max col:' + str(self._max_col)
            raise MatrixIndexError(val)

        return ret

    def set_col(self, col_num, new_col):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the col_num'th column of this matrix to
        those of new_row '''
        # checks that the column to be set is in bounds
        if(new_col is not None):
            if(self.in_bounds(len(new_col) - 1, col_num)):
                if(self.default == new_col.default):
                    # has to delete everything the col first
                    col = self._find_col(col_num)
                    while(col is not None and col.get_down() is not None):
                        curr = col.get_down()
                        self._remove(curr.get_row(), col_num)

                    # gets items from column and puts them in matrix
                    curr = new_col.get_next_item()
                    while(curr is not None):
                        self.set_val(new_col.get_index(curr),
                                     col_num, curr.get_contents())
                        curr = new_col.get_next_item(curr)
                else:
                    i = col_num
                    new_col_values = new_col.get_list()
                    for x in range(0, len(new_col)):
                        self.set_val(x, i, new_col.get_item(x))
            else:
                val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
                val = val + ', got col:' + str(j)
                val = val + ', max col:' + str(self._max_col)
                raise MatrixIndexError(val)
        else:
            # erases column
            col = self._find_col(col_num)
            while(col is not None and col.get_down() is not None):
                curr = col.get_down()
                self._remove(curr.get_row(), col_num)

    def swap_rows(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of rows i and j in this matrix
        '''
        # checks for index error
        if(i < self._max_row and j < self._max_row):
            i_node = self._find_row(i)
            j_node = self._find_row(j)

            if(i_node is not None):
                # can find both i and j
                if(j_node is not None):
                    # replaces i with j and j with i
                    i_vector = self.get_row(i)
                    self.set_row(i, self.get_row(j))
                    self.set_row(j, i_vector)

                # can find only i
                else:
                    # replaces i in j spot and makes i empty
                    self.set_row(j, self.get_row(i))
                    self.set_row(i, None)

            # can only find j
            elif(j is not None):
                # replace j in i and makes j empty
                self.set_row(i, self.get_row(j))
                self.set_row(j, None)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j) + ', max col:'
            val = val + str(self._max_col)
            raise MatrixIndexError(val)

    def swap_cols(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of columns i and j in this matrix
        '''
        # checks for index error
        if(i < self._max_col and j < self._max_col):
            i_node = self._find_col(i)
            j_node = self._find_col(j)

            if(i_node is not None):
                # can find both i and j
                if(j_node is not None):
                    # replaces i with j and j with i
                    i_vector = self.get_col(i)
                    self.set_col(i, self.get_col(j))
                    self.set_col(j, i_vector)

                # can find only i
                else:
                    # replaces i in j spot and makes i empty
                    self.set_col(j, self.get_col(i))
                    self.set_col(i, None)

            # can only find j
            elif(j is not None):
                # replace j in i and makes j empty
                self.set_col(i, self.get_col(j))
                self.set_col(j, None)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j) + ', max col:'
            val = val + str(self._max_col)
            raise MatrixIndexError(val)

    def add_scalar(self, add_value):
        '''(Matrix, float) -> NoneType
        Increase all values in this matrix by add_value
        '''
        # changes default values
        self.default = self.default + add_value

        # gets first row
        curr_row = self._head.get_down()
        while(curr_row is not None):
            # gets first cell
            curr = curr_row.get_right()
            while(curr is not None):
                # gets cell value and changes it
                val = curr.get_contents()
                curr.set_contents(val + add_value)
                # goes to next cell
                curr = curr.get_right()
            # goes to next row
            curr_row = curr_row.get_down()

    def subtract_scalar(self, sub_value):
        '''(Matrix, float) -> NoneType
        Decrease all values in this matrix by sub_value
        '''
        # changes default values
        self.default = self.default - sub_value

        # gets first row
        curr_row = self._head.get_down()
        while(curr_row is not None):
            # gets first cell
            curr = curr_row.get_right()
            while(curr is not None):
                # gets cell value and changes it
                val = curr.get_contents()
                curr.set_contents(val - sub_value)
                # goes to next cell
                curr = curr.get_right()
            # goes to next row
            curr_row = curr_row.get_down()

    def multiply_scalar(self, mult_value):
        '''(Matrix, float) -> NoneType
        Multiply all values in this matrix by mult_value
        '''
        # changes default values
        self.default = self.default * mult_value

        # gets first row
        curr_row = self._head.get_down()
        while(curr_row is not None):
            # gets first cell
            curr = curr_row.get_right()
            while(curr is not None):
                # gets cell value and changes it
                val = curr.get_contents()
                curr.set_contents(val * mult_value)
                # goes to next cell
                curr = curr.get_right()
            # goes to next row
            curr_row = curr_row.get_down()

    def get_default(self):
        '''(Matrix) -> float
        returns the default value'''
        return self.default

    def get_first_row(self):
        '''(Matrix) -> MatrixNode
        returns the first row'''
        return self._head.get_down()

    def get_first_col(self):
        '''(Matrix) -> MatrixNode
        returns the frist col'''
        return self._head.get_right()

    def get_dimensions(self):
        '''(Matrix) -> (int, int)
        returns the max row,col of the matrix'''
        return (self._max_row, self._max_col)

    def add_matrix(self, adder_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the sum of this matrix and adder_matrix
        '''
        # check dimensions
        if(adder_matrix.get_dimensions() == self.get_dimensions()):
            # create a new matrix
            default = self.default + adder_matrix.get_default()
            M = Matrix(self._max_row, self._max_col, default)

            # gets default for use later
            default = adder_matrix.get_default()

            # get the first row of values
            row_1 = self._head.get_down()
            row_2 = adder_matrix.get_first_row()

            # keeps looping while there still exists both rows
            while(row_1 is not None and row_2 is not None):
                # checks the relationship of the rows
                if(row_1.get_contents() == row_2.get_contents()):
                    # they are equal so we need to consider the case
                    # that some numbers are the same
                    self._add_matrix(M, [row_1, row_2], self.default, default)
                    # iterates
                    row_1 = row_1.get_down()
                    row_2 = row_2.get_down()
                elif(row_1.get_contents() < row_2.get_contents()):
                    # only uses row1
                    self._add_matrix(M, [row_1], default)
                    row_1 = row_1.get_down()
                else:
                    # only uses row2
                    self._add_matrix(M, [row_2], self.default)
                    row_2 = row_2.get_down()

            while(row_1 is not None):
                # only uses row1 since only row_1 exists
                self._add_matrix(M, [row_1], default)
                row_1 = row_1.get_down()

            while(row_2 is not None):
                # only uses row2
                self._add_matrix(M, [row_2], self.default)
                row_2 = row_2.get_down()

            return M
        else:
            val = 'This Matrix dimensions: ' + self.get_dimensions()
            val = val + ', adding matrix dimensions: '
            val = val + adder_matrix.get_dimensions()
            raise MatrixDimensionError(val)

    def _add_matrix(self, M, row_nodes, default1, default2=None):
        '''(Matrix, Matrix, list of MatrixNode, float, float)-> NoneType
        helper method to add_matrix, deals with case
        of list having a length of 1 or 2

        REQ: len(row_node) == 1 or  len(row_node) == 2
        REQ: row_nodes[0] is not None'''
        # case where there is more than one row
        if(len(row_nodes) > 1):
            # gets rows
            row1 = row_nodes[0].get_right()
            row2 = row_nodes[1].get_right()
            row_val = row1.get_row()

            # goes through all the columns
            while(row1 is not None and row2 is not None):
                # checks where the rows are in terms of column
                if(row1.get_col() == row2.get_col()):
                    # same place so we add both together
                    val1 = row1.get_contents()
                    val2 = row2.get_contents()

                    M.set_val(row_val, row1.get_col(), (val1 + val2))
                    # iterates
                    row1 = row1.get_right()
                    row2 = row2.get_right()
                elif(row1.get_col() < row2.get_col()):
                    # row1 is smaller so we add it first
                    val1 = row1.get_contents()
                    # add default of second matrix as well
                    M.set_val(row_val, row1.get_col(), (val1 + default2))
                    row1 = row1.get_right()
                else:
                    # row2 is smaller so we add it first
                    val1 = row2.get_contents()
                    M.set_val(row_val, row2.get_col(), (val1 + default1))
                    row2 = row2.get_right()

            while(row1 is not None):
                # only row1 exists
                val1 = row1.get_contents()
                M.set_val(row_val, row1.get_col(), (val1 + default2))
                row1 = row1.get_right()

            while(row2 is not None):
                # only row2 exists
                val1 = row2.get_contents()
                M.set_val(row_val, row2.get_col(), (val1 + default1))
                row2 = row2.get_right()

        else:
            # only one row was passed
            row = row_nodes[0]
            curr = row.get_right()
            while(curr is not None):
                M.set_val(row.get_contents(),
                          curr.get_col(), (curr.get_contents() + default1))
                curr = curr.get_right()

    def dot_product(self, row1, row2):
        '''(Matrix, OneDimensionalMatrix, OneDimensionalMatrix) -> float
        returns the dotproduct of two vectors, returns zero
        in all other situations'''
        ret = 0
        # goes through all the cells and adds them to total
        # only if the lengths are the same
        if(len(row1) == len(row2)):
            for a in range(0, len(row1)):
                ret = ret + (row1.get_item(a)*row2.get_item(a))
        else:
            val = 'given unequal lengths: ' + len(row1) + ' : ' + len(row2)
            raise MatrixDimensionError(val)

        return ret

    def multiply_matrix(self, mult_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the product of this matrix and mult_matrix
        '''
        M = None
        if(mult_matrix is not None):
            # gets row/col of matrix to multiply
            rows = None
            cols = None
            (rows, cols) = mult_matrix.get_dimensions()
            # check whether this is a valid multiplication
            if(self._max_col == rows):
                # creates matrix
                M = Matrix(self._max_row, cols, self.default)

                # goes through all columns and rows
                for x in range(0, self._max_row):
                    vector1 = self.get_row(x)
                    for y in range(0, cols):
                        vector2 = mult_matrix.get_col(y)
                        val = self.dot_product(vector1, vector2)
                        M.set_val(x, y, val)

                return M
            else:
                val = 'col: ' + str(self._max_col) + ', does not equal'
                val = val + ' col: ' + str(rows) + ' to make a valid'
                val = val + ' matrix multiplication'
                raise MatrixDimensionError(val)


class OneDimensionalMatrix(Matrix):
    '''A 1xn or nx1 matrix.
    (For the purposes of multiplication, we assume it's 1xn)'''
    def __init__(self, m, default=0):
        '''(OneDimensionalMatrix, int, boolean, float)
        A representation of a OneDimensionalMatrix that uses Matrix
        to help fill its methods'''
        Matrix.__init__(self, m, m, default)
        self._length = m

    def get_list(self):
        '''(OneDimensionalMatrix) -> list of float
        returns the list representation of the OneDimensionalMatrix'''
        # create array of length with default variables
        ret = []
        for a in range(0, len(self)):
            ret[a] = self.default

        # fills in different variables
        if(self._head.get_down() is not None):
            curr = self._head.get_down().get_right()
            while(curr is not None):
                ret[curr.get_row()] = curr.get_contents()

        return ret

    def __len__(self):
        '''(OneDimensionalMatrix) -> int
        returns the length of the OneDimensionalMatrix'''
        return self._length

    def get_index(self, cell):
        '''(OneDimensionalMatrix) -> int
        returns the spot the value is in'''
        return cell.get_row()

    def get_item(self, i):
        '''(OneDimensionalMatrix, int) -> float
        Return the i'th item in this matrix
        '''
        ret = self.default
        row = self._find_row(i)
        # tries to find row and if it does not then it returns default value
        if(row is not None):
            ret = row.get_right().get_contents()

        return ret

    def get_next_item(self, node=None):
        '''(OneDimensionalMatrix, MatrixNode) -> MatrixNode
        based on this one dimensional array we return the Node
        that appears next
        REQ: type(node) == MatrixNode'''
        ret = None
        # None means that we want first
        if(node is None):
            # checks if there are any nodes
            if(self._head.get_down() is not None):
                ret = self._head.get_down().get_right()
        else:
            # returns the node below
            ret = node.get_down()

        return ret

    def get_val(self, i, j):
        '''(OneDimensionalMatrix(), int, int) -> float
        a method that insures OneDiemnsionalMatrix does not error
        during a call'''
        ret = None
        # checks if i is in domain
        if(i < self.get_max_row):
            # checks if they are trying to access a row
            if(j == 0):
                ret = self.get_item(i)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        # checks for j in domain
        elif(j < self.get_max_row):
            # checks if they are trying acces a row
            if(i == 0):
                ret = self.get_item(j)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        else:
            val = 'got:' + str(i) + ', ' + str(j) + ', max is:'
            val = val + str(self._max_row)
            raise MatrixIndexError(val)

        return ret

    def set_val(self, i, j, new_val):
        '''(OneDimensionalMatrix(), int, int) -> float
        a method that insures OneDimensionalMatrix does not error
        '''
        # checks for i > j case
        if(i < self._max_row):
            # checks if they are trying to access a row
            if(j == 0):
                self.set_item(i, new_val)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        # checks for j > i case
        elif(j < self.get_max_row):
            # checks if they are trying to access a row
            if(i == 0):
                self.set_item(i, new_val)
            else:
                val = 'trying to access a non-OneDimensionalMatrix cell'
                raise MatrixInvalidOperationError(val)
        else:
            val = 'got:' + str(i) + ', ' + str(j) + ', max is:'
            val = val + str(self._max_row)
            raise MatrixIndexError(val)

    def set_item(self, i, new_val):
        '''(OneDimensionalMatrix, int, float) -> NoneType
        Set the i'th item in this matrix to new_val
        '''
        # checks for bounds
        if(self.in_bounds(i, 0)):
            # tries to find row
            row = self._find_row(i)
            # checks if value is default
            if(new_val == self.default):
                # if it is then we need to worry about case of
                # deletion
                if(row is not None):
                    self._remove(i, 0)
                # we don't need to worry about non-existant since
                # it is already default
            else:
                if(row is not None):
                    # changes value
                    row.get_right().set_contents(new_val)
                else:
                    # creates a new value and adds it
                    cell = MatrixNode(new_val)
                    self._add_to_row(i, 0, cell)
                    self._add_to_col(i, 0, cell)

        else:
            val = 'got:' + str(i) + ', max is:'
            val = val + str(self._max_row)
            raise MatrixIndexError(val)

    def multiply_matrix(self, mult_matrix):
        '''(OneDimensionalMatrix, Matrix) -> Matrix
        since I store my vector as just a column I need
        to create a case when we multiply it'''
        M = None
        col_size = None
        row_size = None
        # checks the dimensions
        (row_size, col_size) = mult_matrix.get_dimensions()
        if(self._max_row == row_size):
            # creates array which will be the result
            M = OneDimensionalMatrix(col_size, self.default)
            # goes through all the columns
            curr = mult_matrix
            for a in range(0, col_size):
                curr = curr.get_col(a)
                # sends itself since it is a OneDimensionalMatrix
                M.set_item(a, self.dot_product(self, curr))

            return M
        else:
            val = 'col: ' + str(self._max_col) + ', does not equal'
            val = val + ' col: ' + str(rows) + ' to make a valid'
            val = val + ' matrix multiplication'
            raise MatrixDimensionError(val)


class SquareMatrix(Matrix):
    '''A matrix where the number of rows and columns are equal'''

    def __init__(self, m, default=0):
        '''(SquareMatrix, int, float) -> NoneType
        creates a SquareMatrix'''
        Matrix.__init__(self, m, m, default)

    def transpose(self):
        '''(SquareMatrix) -> NoneType
        Transpose this matrix
        '''
        # goes through and transposes by turning the pointer right-down into
        # down-right since transpose is just i,j -> j,i
        row = self._head
        # starts with head node as it needs to be switched as well

        while(row is not None):
            curr = row
            while(curr is not None):
                # starts going through the columns and switching rows to
                # columns and columns to rows
                temp = curr.get_down()
                curr.set_down(curr.get_right())
                curr.set_right(temp)
                # changes col/row indicators
                temp = curr.get_col_node()
                curr.set_col(curr.get_row_node())
                curr.set_row(temp)
                # columns are now rows so it goes to next column
                curr = curr.get_down()
            # rows are now columns so it gets from columns
            # in order to progress down the rows
            row = row.get_right()

    def get_diagonal(self):
        '''(Squarematrix) -> OneDimensionalMatrix
        Return a one dimensional matrix with the values of the diagonal
        of this matrix
        '''
        M = OneDimensionalMatrix(self._max_row, self.default)
        # gets first calue and gets the index to find
        row = self._head.get_down()
        val_check = row.get_contents()
        # goes through all rows
        while(row is not None):
            curr = row.get_right()
            # goes through columns until it reaches a number greater or
            # the end of the column nodes
            while(curr is not None and curr.get_col() < val_check):
                curr = curr.get_right()

            # checks for right node before adding
            if(curr is not None and curr.get_col() == val_check):
                M.set_item(val_check, curr.get_contents())

            # iterates rows and sets next index
            row = row.get_down()
            if(row is not None):
                val_check = row.get_contents()

        return M

    def set_diagonal(self, new_diagonal):
        '''(SquareMatrix, OneDimensionalMatrix) -> NoneType
        Set the values of the diagonal of this matrix to those of new_diagonal
        '''
        # check the dimensions
        if(len(new_diagonal) == self._max_row):
            # checks the default values
            if(new_diagonal.get_default() == self.default):
                # default values are the same so we only need to add
                # unique values
                # gets the first item and sets it
                curr = new_diagonal.get_next_item()
                while(curr is not None):
                    # sets value and asks for next unique value
                    index = curr.get_row()
                    self.set_val(index, index, curr.get_contents())
                    curr = new_diagonal.get_next_item(curr)
            else:
                # set the entire diagonal as new since default
                # is not the same
                for a in range(0, len(new_diagonal)):
                    self.set_val(a, a, new_diagonal.get_item(a))

        else:
            val = 'The length of the OneDimensionalMatrices are not equal'
            raise MatrixDimensionError(val)


class SymmetricMatrix(SquareMatrix):
    '''A Symmetric Matrix, where m[i, j] = m[j, i] for all i and j'''

    def __init__(self, m, default=0):
        '''(SymmetricMatrix, int, float) ->NoneType
        create a new symmetric matrix'''
        SquareMatrix.__init__(self, m, default)

    def set_val(self, m, n, val):
        '''(SymmetricMatrix, int, int, float)
        insures all values are symmetric'''
        SquareMatrix.set_val(m, n, val)
        SquareMatrix.set_val(n, m, val)

    def set_row(self, i, new_row):
        '''(SymmetricMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_row()
        '''
        raise MatrixInvalidOperationError('invalid type')

    def set_col(self, i, new_row):
        '''(SymmetricMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_col()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_rows(self, i, j):
        '''(SymmetricMatrix, int, int) -> NoneType
        deals with swap_row()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_cols(self, i, j):
        '''(SymmetricMatrix, int, int) -> NoneType
        deals with swap_cols()'''
        raise MatrixInvalidOperationError('invalid type')

    def add_scalar(self, add_val):
        '''(SymmetricMatrix, int) -> Nonetype
        deals with add_sccalar'''
        raise MatrixInvalidOperationError('invalid type')

    def subtract_scalar(self, sub_val):
        '''(SymmetricMatrix, int) -> Nonetype
        deals with sub_scalar'''
        raise MatrixInvalidOperationError('invalid type')


class DiagonalMatrix(SquareMatrix, OneDimensionalMatrix):
    '''A square matrix with 0 values everywhere but the diagonal'''

    def __init__(self, m, default=0):
        '''(DiagonalMatrix, int) -> NoneType
        Creates a diagonal matrix'''
        OneDimensionalMatrix.__init__(self, m, 0)
        SquareMatrix.__init__(self, m, 0)
        self._max_col = m

    def set_val(self, i, j, new_val):
        '''(DiagonalMatrix, int, int, float) -> NoneType
        adds based on the rules of a Matrix'''
        if(self.in_bounds(i, j)):
            # checks that it's asking for diagonal
            if(i == j):
                # changes matrices
                SquareMatrix.set_val(self, i, j, new_val)
                OneDimensionalMatrix.set_item(self, i, new_val)
            else:
                val = 'This is a diagonal Matrix and its values'
                val = val + ' cannot be adjusted at: ' + str(i)
                val = val + ' : ' + str(j)
                raise MatrixInvalidOperationError(val)
        else:
            val = 'got row:' + str(i) + ', max row:' + str(self._max_row)
            val = val + ', got col:' + str(j) + ', max col:'
            val = val + str(self._max_col)
            raise MatrixIndexError(val)

    def set_item(self, i, new_val):
        '''(DiagonalMatrix, int, float) -> NoneType
        adds item based on the rules of a OneDimensional Matrix'''
        if(self.in_bounds(i, i)):
            OneDimensionalMatrix.set_item(self, i, new_val)
            SquareMatrix.set_val(self, i, i, new_val)
        else:
            val = 'got row:' + str(i) + ', max size:' + str(self._max_row)
            raise MatrixIndexError(val)

    def get_val(self, i, j):
        '''(DiagonalMatrix, int, int) -> float
        Return the value of m[i,j] for this matrix m
        '''
        # deals with vertical case since this Matrix
        # stores in both vertical and diagonal
        ret = None
        if(i == j):
            SquareMatrix.get_val(self, i, j)
        else:
            return 0

    def get_row(self, i):
        '''(DiagonalMatrix, int) -> OneDimensionalMatrix
        deals with getting the row of a DiagonalMatrix'''
        ret = SquareMatrix.get_row(self, i)

        # checks for case where we are accessing 0
        # since I have values going down col 0
        if(i != 0):
            ret.set_val(0, 0)

        return ret

    def get_col(self, i):
        '''(Matrix, int) -> OneDimensionalMatrix
        deals with getting a column in DiagonalMatrix
        '''
        ret = None

        # if we're getting col 0 I need to send them just
        # the first value of the column since there are
        # other values in col 0
        if(i == 0):
            ret = OneDimensionalMatrix(len(self))
            ret.set_item(0, self.get_item(0))
        else:
            ret = SquareMatrix.get_col(self, i)

        return ret

    def set_row(self, i, new_row):
        '''(DiagonalMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_row()'''
        raise MatrixInvalidOperationError('invalid type')

    def set_col(self, i, new_row):
        '''(DiagonalMatrix, int, OneDimensionalMatrix) -> NoneType
        deals with set_col()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_rows(self, i, j):
        '''(DiagonalMatrix, int, int) -> NoneType
        deals with swap_row()'''
        raise MatrixInvalidOperationError('invalid type')

    def swap_cols(self, i, j):
        '''(DiagonalMatrix, int, int) -> NoneType
        deals with swap_cols()'''
        raise MatrixInvalidOperationError('invalid type')

    def add_scalar(self, add_val):
        '''(DiagonalMatrix, int) -> Nonetype
        deals with add_sccalar'''
        raise MatrixInvalidOperationError('invalid type')

    def subtract_scalar(self, sub_val):
        '''(DiagonalMatrix, int) -> Nonetype
        deals with sub_scalar'''
        raise MatrixInvalidOperationError('invalid type')

    def add_matrix(self, add_Matrix):
        '''(DiagonalMatrix, Matrix) -> Nonetype
        deals with add_matrix'''
        raise MatrixInvalidOperationError('invalid type')


class IdentityMatrix(DiagonalMatrix):
    '''A matrix with 1s on the diagonal and 0s everywhere else'''

    def __init__(self, m):
        '''(Matrix, int) -> NoneType
        creates an identity matrix'''
        DiagonalMatrix.__init__(self, m)
        # fills the values with 1
        for a in range(0, m):
            DiagonalMatrix.set_val(self, a, a, 1)

    def set_val(self, i, j, val):
        '''(IdentityMatrix, int, int, float)
        deals with set_val'''
        raise MatrixInvalidOperationError('invalid type')
