# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    
    # 2022/04/25
    # Save in a buffer variable 
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator 
        self.buffer = self.iter.next()
        self.end = False
    
    # TC: O(1)
    # SC: O(1)
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.buffer

    # TC: O(1)
    # SC: O(1)
    def next(self):
        """
        :rtype: int
        """
        if self.iter.hasNext():
            res = self.iter.next()
            pop = self.buffer
            self.buffer = res
            return pop
        else:
            self.end = True
            return self.buffer

    # TC: O(1)
    # SC: O(1)     
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.iter.hasNext():
            return True
        else:
            if self.end:
                return False
            return True

        
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].