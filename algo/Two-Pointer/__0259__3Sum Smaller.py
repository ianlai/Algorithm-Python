class Solution:
    
    # Two Sum variation [O(n2): 22%]
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if nums is None:
            return 0
        nums.sort()
        count = 0
        for i in range(len(nums)):
            curTarget = target - nums[i]
            count += self.twoSumSmaller(nums, i + 1, len(nums) - 1, curTarget)
        return count 
    
    def twoSumSmaller(self, nums, l, r, target):
        count = 0
        while l < r:
            twoSum = nums[l] + nums[r]
            if twoSum < target:
                count += r - l
                l += 1
            elif twoSum >= target:
                r -= 1
        return count
            
    # ==========================================    
    # Brute force [O(n3)]
    def threeSumSmaller1(self, nums: List[int], target: int) -> int:
        print("Method-1")
        if nums is None:
            return 0
        nums.sort()
        #print(nums)
        count = 0
        for i in range(len(nums)):
            #if i > 0 and nums[i] == nums[i-1]:
            #    continue
            curTarget = target - nums[i] 
            #print(i, curTarget, ":")
            count += self.twoSumSmaller1(nums, i + 1, len(nums), curTarget)
        return count 
    
    def twoSumSmaller1(self, nums, start, end, target):
        count = 0
        for i in range(start, end, 1):
            for j in range(end-1, i, -1):
                twoSum = nums[i] + nums[j]
                if twoSum < target:
                    #print(" ", i, j, "->", j-i)
                    count += j - i
                    break
        return count
            