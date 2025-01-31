class NumArray:

    #Prefix Sum [43%]
    # O(n) 
    def __init__(self, nums: List[int]):
        self.prefixSum = []
        for num in nums:
            if not self.prefixSum:
                self.prefixSum.append(num)
            else:
                self.prefixSum.append(self.prefixSum[-1] + num)

    # O(1) 
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        else:
            return self.prefixSum[right] - self.prefixSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)