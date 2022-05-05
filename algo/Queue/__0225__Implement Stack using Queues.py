# 2022/05/05 
# Single queue 
class MyStack:

    def __init__(self):
        print("Code2")
        self.deq1 = collections.deque()

    def push(self, x: int) -> None:
        self.deq1.append(x)

    def pop(self) -> int:
        for _ in range(len(self.deq1)-1):
            self.deq1.append(self.deq1.popleft())
        res = self.deq1.popleft()
        return res
        
    def top(self) -> int:
        res = 0
        for _ in range(len(self.deq1)):
            res = self.deq1.popleft()
            self.deq1.append(res)
        return res

    def empty(self) -> bool:
        return len(self.deq1) == 0
    
    
# 2022/05/05 
# Two queues 
class MyStack1:

    def __init__(self):
        self.deq1 = collections.deque()
        self.deq2 = collections.deque()

    def push(self, x: int) -> None:
        self.deq1.append(x)

    def pop(self) -> int:
        while len(self.deq1) > 1:
            self.deq2.append(self.deq1.popleft())
        res = self.deq1.popleft()
        
        self.deq1 = self.deq2
        self.deq2 = collections.deque()
        return res
        
    def top(self) -> int:
        while len(self.deq1) > 1:
            self.deq2.append(self.deq1.popleft())
        res = self.deq1.popleft()
        self.deq2.append(res)
        
        self.deq1 = self.deq2
        self.deq2 = collections.deque()
        return res

    def empty(self) -> bool:
        return len(self.deq1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()