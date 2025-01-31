class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.sum = 0
        self.deq = collections.deque()

    def next(self, val: int) -> float:
        self.deq.append(val)
        self.sum += val 
        if len(self.deq) > self.size:
            popleft = self.deq.popleft()
            self.sum -= popleft
        return self.sum / len(self.deq)
            
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)