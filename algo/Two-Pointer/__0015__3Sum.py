class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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