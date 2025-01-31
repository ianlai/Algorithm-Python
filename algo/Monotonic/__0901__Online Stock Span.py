# 2022/05/22
# Monotonic Stack (not store the price array)
class StockSpanner:

    def __init__(self):
        print("Code2")
        self.stack = []

    # [O(1): 55% / O(1): 75%]
    def next(self, price: int) -> int:
        res = 1 
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append((price, res))
        return res
    
# 2022/05/22
# Monotonic Stack (store the price array)
class StockSpanner:

    def __init__(self):
        print("Code1")
        self.stock = []
        self.stack = []
        self.idx = 0

    # [O(1): 16% / O(1): 41%]
    def next(self, price: int) -> int:
        self.stock.append(price)
        
        while self.stack and self.stock[self.stack[-1]] <= price:
            self.stack.pop()
        lastIdx = self.stack[-1] if self.stack else -1
        self.stack.append(self.idx)
        self.idx += 1
        return self.idx - 1 - lastIdx


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)