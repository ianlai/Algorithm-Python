class Solution:
# [1,0,0]
# 2
# [1,0]
# 2
# [0,1]
# 2
# [1,2,12]
# 6
# [1,3,0,6]
# 6
    
    # 2022/01/15 
    # Store the remainder; deal with the edge cases [O(n): 30%]
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        print("Code3")
        if not nums:
            return False
        
        accumulativeSum = [0] * len(nums)
        accumulativeSum[0] = nums[0]
        for i in range(1, len(nums)):
            accumulativeSum[i] = accumulativeSum[i-1] + nums[i] 
        
        #print(nums)
        #print(accumulativeSum)
        
        remainderMap = {}
        for i, v in enumerate(accumulativeSum):
            remainder = v % k
            if remainder in remainderMap:
                if i - remainderMap[remainder] > 1:
                    return True
            else:
                remainderMap[remainder] = i
            
            #Edge cases 
            if i != 0 and remainder == 0:
                return True
            
            #print(i, remainder, remainderMap)
        return False
    
    # ========================================
    # 2022/01/15 
    # Store the remainder [Too many edge cases]
    def checkSubarraySum2(self, nums: List[int], k: int) -> bool:
        print("Code2")
        if not nums:
            return False
        
        accumulativeSum = [0] * len(nums)
        accumulativeSum[0] = nums[0]
        for i in range(1, len(nums)):
            accumulativeSum[i] = accumulativeSum[i-1] + nums[i] 
        print(nums)
        print(accumulativeSum)
        
        remainderMap = {}
        for i, v in enumerate(accumulativeSum):
            remainder = v % k
            quotient = v // k
            if remainder in remainderMap and remainderMap[remainder][0] != quotient and remainderMap[remainder][1] != i - 1:
                return True
            if i != 0 and nums[i] == 0 and nums[i-1] == 0:
                return True
            if i != 0 and remainder == 0:
                return True
            remainderMap[remainder] = (quotient, i)
            #print(v, remainderMap)
        return False
        
    # ========================================
    # 2022/01/15 
    # Accumulative sum [O(n2): TLE]
    def checkSubarraySum1(self, nums: List[int], k: int) -> bool:
        print("Code1")
        accumulativeSum = [0] * len(nums)
        accumulativeSum[0] = nums[0]
        for i in range(1, len(nums)):
            accumulativeSum[i] = accumulativeSum[i-1] + nums[i] 
            
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i == 0:
                    curSum = accumulativeSum[j]
                else:
                    curSum = accumulativeSum[j] - accumulativeSum[i-1]
                if curSum % k == 0:
                    return True
        return False
        