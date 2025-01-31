class TwoSum:

    # 2022/06/09 
    # HashMap [O(N): 13% / O(N): 96%]
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.arr.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        mset = set()
        for v in self.arr:
            if value - v in mset:
                return True
            mset.add(v)
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)