class Solution:

    # Monotonic stack [O(n): 12%]
    def find132pattern(self, nums: List[int]) -> bool:
        print("Code2")
        if len(nums) < 3:
            return False
        mstack = []
        right = -inf
        for i in range(len(nums)-1, -1, -1):
            if mstack and nums[i] < mstack[-1]:
                if nums[i] < right:
                    return True
            else:    
                while mstack and nums[i] > mstack[-1]:
                    right = mstack.pop()
            mstack.append(nums[i])
        return False
    
    #========================================
    #Brute force [O(n2): TLE]
    def find132pattern1(self, nums: List[int]) -> bool:
        print("Code1")
        min_i = inf
        for j in range(len(nums) - 1):
            min_i = min(min_i, nums[j])
            for k in range(j + 1, len(nums)):
                if min_i < nums[k] < nums[j]:
                    return True
        return False