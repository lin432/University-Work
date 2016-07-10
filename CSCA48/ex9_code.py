import random

#not implemented
class HeapEmptyError(Exception):
    pass

class Heap(object):
    '''A class representing a heap.'''
    
    def __init__(self, insert_list = []):
        '''(Heap [,list]) -> NoneType
        Create a new Heap containing the elements in insert_list.
        '''
        # test case would be just regualar case
        self._heap = []
        for element in range(len(self._heap)):
            self.insert(element)

    def is_empty(self):
        '''(Heap) -> bool
        Return True iff there are no nodes in this Heap.
        '''
        # no return
        # statement isn't a statement
        ret = False
        if(self._heap == []):
            ret = True
        return ret

    def insert(self, insert_value):
        '''(Heap, object) -> NoneType
        Insert insert_value into this Heap.
        REQ: insert_value is not already in this Heap.
        '''
        # adding a value to a list crashes python
        self._heap += [insert_value]
        self._bubble_up(len(self._heap) - 1)

    def _bubble_up(self, c_index):
        '''(Heap) -> NoneType
        
        Re-arrange the values in this Heap to maintain the heap
        property after a new element has been inserted into the
        heap. The offending child node is located at c_index.
        '''

        p_index = (c_index - 1) / 2
        #Base Case: We're at the beginning of the list, do nothing
        if (c_index > 0):
            # not bracketed
            if (self._heap[c_index] > self._heap[p_index]):
                #swap the parent and child
                self._swap(c_index, p_index)
                #RD: bubble up again from our new position
                # would just do it at c_index and return
                self._bubble_up(p_index)

    def _swap(self, i, j):
        '''(Heap, int, int) -> NoneType
        Swap the values at indices i and j.
        '''
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def remove_top(self):
        '''(Heap) -> object
        Remove and return the largest element in this Heap.
        RAISES: HeapEmptyException if this Heap is empty.
        '''
        # not a working decision and heap is a list
        # so we need to change to len() == 0
        if (len(self._heap) == 0):
            raise HeapEmptyException("Attempt to remove top of empty heap")
        else:
            #save the top element
            ret = self._heap[0]
            #remove the last element from the heap, and 
            #replace the head's value with it
            last = self._heap.pop()
            # brackets
            if (len(self._heap) > 0):
                self._heap[0] = last
                self._bubble_down(0)
            return ret

    def _bubble_down(self, p_index):
        '''(Heap) -> NoneType

        Re-arrange the values in this Heap to maintain the heap
        property after the top element of the heap has been removed.
        The parent node which potentially violates the heap property
        is located at p_index.
        '''

        lt_index = (p_index * 2) + 1
        rt_index = (p_index * 2) + 2
        # Base Case: If we don't violate, then do nothing
        if self._violates(p_index):
            # one of our children violates the heap property
            # if we only have a left child, it must be that one
            # brackets
            if (rt_index >= len(self._heap)):
                self._swap(p_index, lt_index)
                p_index = lt_index
               
            # if we have two children, we need to swap with the larger child
            # brackets
            elif (self._heap[lt_index] > self._heap[rt_index]):
                self._swap(p_index, lt_index)
                p_index = lt_index
            else:
                self._swap(p_index, rt_index)
                p_index = rt_index
            # RD: Bubble down from our new position
            # would infin as even if violation it would bubble down
            # to same node
            self._bubble_down(p_index)


    def _violates(self, index):
        '''(Heap, int) -> bool
        
        Return whether the node at index and one of its children
        violate the heap property.
        '''

        lt_index = (index * 2) + 1
        rt_index = (index * 2) + 2
        #if we have no children, we're fine
        # not the right condition should be if lt_index>=len(self._heap)
        if (lt_index >= len(self._heap)):
            return True
        #if we have one child, return True iff it violates
        # brackets
        elif (rt_index >= len(self._heap)):
            return self._heap[lt_index] > self._heap[index]
        #if we have two children, return True if either child violates
        else:
            return (self._heap[lt_index] > self._heap[index] or
                    self._heap[rt_index] > self._heap[index])


if __name__ == "__main__":
    my_unordered_list = []
    random_number = random.random() * 100
    for i in range(100):
        my_unordered_list.append(random_number)
    my_heap = Heap(my_unordered_list)
    my_ordered_list = []
    while not my_heap.is_empty():
        my_ordered_list.append(my_heap.remove_top())
        print(my_heap)
    print(my_ordered_list)
