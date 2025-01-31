class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def reset(self) -> List[int]:
        return self.arr 
    
    # Brute Force [40%]
    def shuffle(self) -> List[int]:
        print("Code2")
        arr = list(self.arr)
        res = []
        while arr:
            idx = random.randint(0, len(arr)-1)
            res.append(arr[idx])
            arr.pop(idx)
        return res
    
    # Brute Force [5%]
    def shuffle1(self) -> List[int]:
        print("Code1")
        randSet = set() 
        randArr = []
        for i in range(len(self.arr)):
            r = random.randint(0, len(self.arr)-1)
            while r in randSet:
                r = random.randint(0, len(self.arr)-1)
            randSet.add(r)
            randArr.append(r)
        res = []
        for v in randArr:
            res.append(self.arr[v])
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()