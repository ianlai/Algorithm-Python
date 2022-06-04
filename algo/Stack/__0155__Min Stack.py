class MinStack:
    
    # 2022/06/04
    # One diff stack [O(1) / O(1)]
    # 使用diffstack可以把額外的空間複雜度降為O(1)，當然一個stack來存資料是必然需要O(N)的
    # 當新的min進來的時候，就把diffstack存入負值，在取出的時候也可以用是否有負值來判斷要不要更新min
    '''
    input [3, 5, 2, 2, 8, -3, 1]
    diff  [0, 2,-1, 0, 6, -5, 4] 
    min    3     2        -3 
    '''
    def __init__(self):
        print("Code2")
        self.diffstack = []
        self.min = None 
        
    def push(self, val: int) -> None:
        if not self.diffstack:
            self.diffstack.append(0)  #val - min
            self.min = val
        else:
            diff = val - self.min
            if diff < 0:  #update
                self.diffstack.append(diff) #negative
                self.min = val
            else:
                self.diffstack.append(diff) #0 or positive
    
    def pop(self) -> None:
        pop = self.diffstack.pop()
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        if not self.diffstack: #error 
            return None 
        top = self.diffstack[-1]
        if top > 0:
            return self.diffstack[-1] + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
        
        
        
class MinStack1:
    
    # 2021/05/19 
    # Two Stacks [O(1) / O(N)]
    def __init__(self):
        """
        initialize your data structure here.
        """
        print("Code1")
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

    #Slow O(N): 22%
    def getMin1(self) -> int:
        if self.minstack:
            return min(self.stack)
        return None
    
    #Fast O(1): 87%
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