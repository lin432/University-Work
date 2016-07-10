class container():

    def __init__(self):
        self._c = []
    
    def put(self,item):
        self._c.append(item)

    def get(self):
        return self._c.pop()

    def is_empty(self):
        if (len(self._c) < 1):
            return True
        else:
            return False
            
