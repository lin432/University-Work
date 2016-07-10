class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.depth = 0  # the depth of this node in a tree

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, depth):
        '''(BTNode, int) ->  NoneType
        sets the binary tree nodes depth'''
        self.depth = depth
        if(self.right is not None):
            self.right.set_depth((depth + 1))
        if(self.left is not None):
            self.left.set_depth((depth + 1))

    def leaves_and_internals(self):
        '''(BTNode) -> (set of int, set of int)
        returns a tuple with a set of all leaves in the tree
        and a set of values in the internals of the tree, that is
        bounded by the root and the leaves'''
        leaf = set()
        internal = set()
        if(self.left is not None):
            self.left._internals(leaf, internal)
        if(self.right is not None):
            self.right._internals(leaf, internal)

        return (leaf, internal)

    def _internals(self, leaf, internal):
        '''(BTNode) -> (set of int, set of int)
        helper method for leaves_and_internals'''
        if(self.left is None and self.right is None):
            leaf.add(self.value)
        else:
            internal.add(self.value)
            if(self.left is not None):
                self.left._internals(leaf, internal)
            if(self.right is not None):
                self.right._internals(leaf, internal)

    def sum_to_deepest(self):
        '''(BTNode) -> float
        returns the sum of the deepest path'''
        suml = None
        depthl = None
        sumr = None
        depthr = None
        ret = None

        if(self.left is not None):
            (suml, depthl) = self.left._deep()
        if(self.right is not None):
            (sumr, depthr) = self.right._deep()

        if(depthl > depthr):
            ret = suml
        elif(depthr > depthl):
            ret = sumr
        else:
            if(sum1 > sum2):
                ret = sum1
            else:
                ret = sum2

        return (ret + self.value)

    def _deep(self):
        '''(BTNode) -> (float, int)
        helper method that returns a tuple
        of the sums, and the depth'''
        ret = None
        if(self.left is None and self.right is None):
            ret = (self.value, 0)
        else:
            suml = None
            depthl = None
            sumr = None
            depthr = None

            if(self.left is not None):
                (suml, depthl) = self.left._deep()
            if(self.right is not None):
                (sumr, depthr) = self.right._deep()

            if(suml is not None and sumr is not None):
                if(depthl > depthr):
                    ret = (suml + self.value, depthl + 1)
                elif(depthr > depthl):
                    ret = (sumr + self.value, depthr + 1)
                else:
                    if(suml > sumr):
                        ret = (suml + self.value, depthl + 1)
                    else:
                        ret = (sumr + self.value, depthr + 1)
            elif(suml is not None):
                ret = (suml + self.value, depthl + 1)
            elif(sumr is not None):
                ret = (sumr + self.value, depthr + 1)

        return ret
