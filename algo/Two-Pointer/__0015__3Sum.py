# https://leetcode.com/problems/3sum/

class Solution:
    
    # 2022/01/26 
    # Two sum function + Redanduncy removal [O(n): 44%]
    # 放入時就去重
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        print("Code-3: Two sum function + Redanduncy removal")
        if not nums or len(nums) <= 2:
            return []
    
        def twoSum(nums, start, end, target):
            if start >= end:
                return []
            left, right = start, end 
            res = []
            while left < right:
                
                # Redanduncy removal 
                if left > start and nums[left-1] == nums[left]:
                    left += 1
                    continue
                if right < end and nums[right] == nums[right+1]:
                    right -= 1
                    continue
                    
                twoSum = nums[left] + nums[right]
                
                if twoSum == target:
                    res.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif twoSum > target:
                    right -= 1
                else:
                    left += 1
            return res 
        
        nums.sort()
        res = []
        for i in range(len(nums)):
            # Redanduncy removal 
            if i > 0 and nums[i-1] == nums[i]:
                continue
            twoSumList = twoSum(nums, i + 1, len(nums) - 1, -nums[i]) #nums, start, end, target
            for twoSumPair in twoSumList:
                twoSumPair.append(nums[i])
                res.append(twoSumPair)
        return res
            
    # =======================================

    # 2021/10/13
    # Two-Sum, manaully remove the redundancies of each item BEFORE adding to result [O(n2): 80%]
    # 結束後才去重
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
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
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
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