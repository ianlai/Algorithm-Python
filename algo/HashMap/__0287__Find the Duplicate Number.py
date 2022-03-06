class Solution:
    
    # 2022/03/06 
    # Cycle detection [Time: O(n) 89% / Space: O(1) 52%]
    def findDuplicate(self, nums: List[int]) -> int:
        print("Code4")
        
        #Start at different points otherwise not getting to loop
        slow, fast = nums[0], nums[nums[0]] 
        
        #Phase1: find intersectioin
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        #Phase2: find entry 
        slow = 0 
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow 
        
    # ===========================================
        
    # 2022/03/06 
    # Binary Search - Range [Time: O(nlogn) 32% / Space: O(1) 52%]
    def findDuplicate3(self, nums: List[int]) -> int:
        print("Code3")
        def isNumOfEqualAndLessThanItself(v):
            count = 0
            for num in nums:
                if num <= v:
                    count += 1
                if count > v:
                    return True
            return False
                
        start, end = 0, len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if isNumOfEqualAndLessThanItself(mid):
                end = mid
            else:
                start = mid + 1
        return start 
        
    # ===========================================

    # 2022/03/06 
    # Sort [Time: O(nlogn) 41% / Space: O(n) 29%]
    # Merge sort -> time: O(nlogn) space: O(n)
    # Quick sort -> time: O(nlogn) O(n2) space: O(logn) O(n)
    def findDuplicate2(self, nums: List[int]) -> int:
        print("Code2")
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return nums[i]
    
    # ===========================================
    # 2021/05/15
    # Hashset [Time: O(n) 60% / Space: O(n) 17%]
    def findDuplicate1(self, nums: List[int]) -> int:
        print("Code1")
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