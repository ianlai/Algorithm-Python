class Solution:
    # 2022/05/03
    # Sorting [TC:O(nlogn):28% / SC:O(n):54%]
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        left, right = 0, 0
        for i in range(len(nums)):
            if nums[i] != sortedNums[i]:
                left = i
                break
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != sortedNums[i]:
                right = i
                break
        return right - left + 1 if left != right else 0
                
    #Find droping points [Wrong]
    def findUnsortedSubarray1(self, nums: List[int]) -> int:
        print("Code1")
        drop = []
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                drop.append(i-1)
        if len(drop) == 0:
            return 0
        else:
            left = 0 
            for i in range(drop[-1]+1):
                if nums[i] > nums[drop[-1]+1]:
                    left = i
                    break
            left = min(left, drop[0])
            
            right = 0
            for i in range(len(nums) - 1, drop[0], -1):
                if nums[i] < nums[drop[0]]:
                    right = i
                    break
            right = max(right, drop[-1]+1)
            #print(left, right, drop)
            return right - left + 1
        
            
            
            
#         left = right = 0
        
#         for i in range(1, len(nums)):
#             if nums[i - 1] >= nums[i]:
#                 left = i - 1
#                 break
        
#         for i in range(len(nums)-2, -1, -1):
#             if nums[i] >= nums[i + 1]:
#                 right = i + 1
#                 break
        
#         if nums[left] == nums[right]:
#             for i in range(left, right + 1):
#                 if nums[i] != nums[left]:
#                     return right - left + 1
#             return 0
#         else:
#             return right - left + 1 if left != right else 0
    
        
                
        