class Solution:
    
    # Hashset [O(n), 34%]
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        numsSet = set()
        
        for e in nums:
            if e in numsSet:
                return e
            else:
                numsSet.add(e)
        return -1

#     def findDuplicate(self, nums: List[int]) -> int:
#         if not nums:
#             return -1
        
#         ans = 0 
#         for i in range(len(nums)):
#             ans ^= nums[i]
#         for i in range(1, len(nums)):
#             ans ^= i
#         print(ans)