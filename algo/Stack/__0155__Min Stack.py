class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack and val <= self.minstack[-1]:
            self.minstack.append(val)
        if not self.minstack: 
            self.minstack.append(val)
    
    def pop(self) -> None:
        if self.stack:
            if self.getMin() == self.top():
                self.minstack.pop()
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        return None
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()