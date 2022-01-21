class Solution:
    
    # Prefix Sum [O(n): 20%]
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        print("Code2")
        # prefixSum = [0] * len(nums)
        # prefixSum[0] = nums[0]
        # for i, v in enumerate(nums):
        #     if i > 0:
        #         prefixSum[i] = prefixSum[i-1] + v
        
        #Add a dummy "0" in the beginning to calculate the prefixSum 
        prefixSum = [0]
        for v in nums:
            prefixSum.append(prefixSum[-1] + v)
        
        #Update the count and res together 
        countMap = collections.defaultdict(int)
        res = 0
        for v in prefixSum:
            res += countMap[v]      # Update res 
            countMap[v + goal] += 1 # "v + goal" over prefixSum will not be counted
            
        print("Original:", nums)
        print("Prefix  :", prefixSum)
        print("CountMap:", countMap)
        
        return res
        
        # res = 0
        # if goal != 0:
        #     for v, count in countMap.items():
        #         if v == goal:
        #             res += count
        #         else:
        #             if v - goal in countMap:
        #                 res += count * countMap[v - goal]
        #     return res
        # else:
        #     for v, count in countMap.items():
        #         if v == 0:
        #             res += (count + 1) * count // 2
        #         else:
        #             res += (count - 1) * count // 2
        #     return res
            
    
    # Sliding window [Incorrect]
    def numSubarraysWithSum1(self, nums: List[int], goal: int) -> int:
        print("Code1")
        if not nums:
            return 0

        def atMost(nums, goal):
            i = 0
            totalSum = 0
            res = 0
            for j in range(len(nums)):
                totalSum += nums[j]
                print(i, j, "->", totalSum)
                
                if totalSum <= goal:
                    continue
                firstI = i    
                while i <= j and totalSum >= goal:
                    print(i, j, totalSum)
                    totalSum -= nums[i]
                    i += 1
                print("i, fi:", i, firstI)
                res += i - firstI - 1
            return res
        k1 = atMost(nums, goal) 
        #k2 = atMost(nums, goal-1)
        print("goal:", goal, k1)
        #print("goal-1:", goal-1, k2)
        return k1 

                