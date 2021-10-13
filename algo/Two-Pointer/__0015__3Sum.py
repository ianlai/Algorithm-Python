# https://leetcode.com/problems/3sum/

class Solution:
    
    # Two-Sum, manaully remove the redundancies of each item BEFORE adding to result [O(n2): 80%]
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        print("Code-2")
        nums.sort()
        res = []
        for idx, val in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:        #remove redundancy - 1 
                continue 
            l, r = idx + 1, len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r] 
                if threeSum == 0:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:   #remove redundancy - 2
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:   #remove redundancy - 3 (this line is redundancy)
                        r -= 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
        return res   
    
    # =======================================

    # Two-Sum, use set to remove the redundancies AFTER adding to result [O(n2): 19%]
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        print("Code-1")
        nums.sort()
        res = set()
        for idx, val in enumerate(nums):
            l, r = idx + 1, len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r] 
                if threeSum == 0:
                    res.add(tuple([val, nums[l], nums[r]]))
                    l += 1
                    r -= 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
        return res
                
    # =======================================
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        print("Code-0")
        if not nums:
            return []
        
        nums.sort()
        print(nums)
        result = []
        # -a = b + c 
        for i in range(len(nums)):  #loop a 
            if i > 0 and nums[i-1] == nums[i]: #get first a only (remove duplicated a later)
                continue
            n1 = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                twosum = nums[left] + nums[right]
                if twosum > n1:
                    right -= 1
                elif twosum < n1:
                    left += 1
                else:
                    result.append([-n1, nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return result