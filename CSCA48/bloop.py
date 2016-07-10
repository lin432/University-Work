class BTNode():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.siblings = False

    def get_height(self):
        l = None
        r = None
        if(self.left is None and sel.right is None):
            return 1
        if(self.left is not None):
            l = self.left.get_height()
        if(self.right is not None):
            r = self.right.get_height()

        if(l is not None and r is not None):
            if(l > r):
                return l + 1
            else:
                return r + 1
        elif(l is not None):
            return l + 1
        elif(r is not None):
            return r + 1

    def siblings(self):
        if(self.left in not None and self.right is not None):
            self.left.siblings = True
            self.right.siblings = True
            self.left.siblings()
            self.right.siblings()
        else:
            if(self.left is not None):
                self.left.siblings()
            if(self.right is not None):
                self.right.siblings()
        
