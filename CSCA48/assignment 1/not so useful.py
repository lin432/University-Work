    def _set_col_row_values(self):
        '''(Matrix) -> NoneType
        Goes through head and labels all nodes col and row values in an
        un initialized MatrixNode head (a.k.a one you pass us)
        This is very resource inefficient meant to speed up all other
        functions and makes it easy to check the col/row of a spot in
        the matrix'''
        _change_all_col_values(self._head.get_right())
        _change_all_row_values(self._head.get_down())

    def _change_all_col_values(self, col): # update with col being a node
        '''(Matrix, Matrix Node) -> NoneType
        recursive helper method that goes through all the connected
        column values and gives them self._col value based on current
        node'''
        # checks if there is any columns left
        if(col is not None):
            # get current column number
            col_val = col.get_contents()
            # gets first value below
            curr = col.get_down()

            # uses method to change all the values in column
            self._set_col_values(curr, col_val)

            # recurses to next column
            next_col = col.get_right()
            if(next_col is not None):
                self._change_all_col_values(next_col)

    def _set_col_values(self, head, val): # deprecated see above
        '''(Matrix, MatrixNode, int) -> NoneType
        changes all the col values of the column to the value given'''
        # goes through all values
        while(head is not None):
            # updates the value
            head.set_col(val)
            # get next node
            head = head.get_down()

    def _change_all_row_values(self, row): # deprecated see above
        '''(Matrix, Matrix Node) -> NoneType
        recursive helper method that goes through all the connected
        row values and gives them self._row value based on current
        node'''
        # checks that there is more rows
        if(row is not None):
            # get current row number
            row_val = row.get_contents()
            # gets first value to the right
            curr = row.get_right()

            # uses method to change all values in the row
            self._set_row_values(curr, row_val)

            # recurses to next row
            next_row = row.get_down()
            if(next_row is not None):
                self._change_all_row_values(next_row)

    def _set_row_values(self, head, val): # deprecated see above
        '''(Matrix, MatrixNode, int) -> NoneType
        changes all the row values of the column to the value given'''
        # goes through all values
        while(head is not None):
            # updates the value
            head.set_row(val)
            # get next node
            head = head.get_right()

    def set_head(self, newHead):
        '''(Matrix, MatrixNode) -> None
        Sets the head of the Matrix'''
        self._head = newHead

    '''
    def set_row(self, row_num, new_row):
        (Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the row_num'th row of this matrix to those of new_row
        
        
        # checks to make sure that the row to be set exists in the matrix
        if(row_num <= self._max_row):
            # tries to find the row in the Matrix
            head = _find_row(row_num)

            # if found it just changes the rows
            if(head is not None):
                # ***************************************** redo to fit OneD
                head.set_right(new_row)
            # it hasn't been found so we create a new node and add it
            # to the matrix
            else:
                temp_head = MatrixNode(row_num)
                temp_head.set_right(new_row)
                self._head.add_down(temp_head)
        else:
            pass
        # throw MatrixIndexError()

    def set_row_default(self, row_num, curr = self._head):
        (Matrix, int) -> Nonetype
        Changes a row so that all of its values return to default
       
        # gets the current node below it
        x = curr.get_down()

        # makes sure it isn't the end of the rows
        if(x is not None):
            # checks whether it has found the right row
            if(x.get_contents() == row_num):
                # checks whether a child exists and then moves the child up
                # disconnecting the other row
                if(x.get_down() is not None):
                    curr.set_down(x.get_down())
                # gets rid of reference to that row
                else:

                    curr.set_down(None)
            else:
                set_row_default(row_num, x)'''


        i = row.get_contents()
        curr = self._head
        print(self._head.get_down().get_contents())
        print(i, j)
        while(curr.get_down() is not None and curr.get_down().get_contents() < i):
            curr = curr.get_down()

        print(curr.get_down().get_contents(), i, 'a')

        if(curr.get_down() is not None and curr.get_down().get_contents() == i):
            curr.add_down(row)
            if(j == None):
                pass
                # error
            else:
                old_row = row.get_down()
                old_row.set_contents(j)
                self._move_row(old_row)
        else:
            curr.add_down(row)


        # checks for index error
        if(self.in_bounds(i, j)):
            curr = self._head
            i_prev = None
            j_prev = None
            # goes through and tries to find the nodes previous to i and j
            while(curr.get_down() is not None and (i_prev == None or j_prev == None)):
                if(curr.get_down().get_contents() == i):
                    i_prev = curr
                if(curr.get_down().get_contents() == j):
                    j_prev = curr
                curr = curr.get_down()

            # checks for what exists
            
            if(i_prev is not None):
                if(j_prev is not None):
                    # both i and j exist so we get j
                    # we are removing_row_impact at the same time when
                    # both cases exist to prevent pointer loss
                    i_node = i_prev.get_down()
                    j_node = j_prev.get_down()
                    i_node.set_contents(j)
                    j_node.set_contents(i)

                    i_prev.remove_down()
                    j_prev.remove_down()

                    i_node.set_down(None)
                    j_node.set_down(None)

                    # add rows i and j back to the Matrix
                    i_prev.add_down(j_node)
                    j_prev.add_down(i_node)
                else:
                    # gets i since it exists
                    i_node = self._remove_row_impact(i_prev)
                    i_node.set_contents(j)
                
                    # searches for the position to replace i
                    curr = self._head
                    while(curr.get_down() is not None and
                          curr.get_down().get_contents() < j):
                        curr = curr.get_down()

                    curr.add_down(i_node)
            else:
                j_node = self._remove_row_impact(j_prev)
                j_node.set_contents(i)
                
                # searches for the position to replace i
                curr = self._head
                while(curr.get_down() is not None and
                      curr.get_down().get_contents() < i):
                    curr = curr.get_down()

                curr.add_down(j_node)

    def _remove_row_impact(self, i_prev):
        '''(Matrix, int) -> MatrixNode
        removes the impact of a node and returns that node'''
        # this is a process to isolate a matrixnode
        # we first get i
        i = i_prev.get_down()
        # we then remove i's location and replace
        # it with the children of i
        i_prev.remove_down()
        # and then we change i to have no children
        i.set_down(None)
        return i

