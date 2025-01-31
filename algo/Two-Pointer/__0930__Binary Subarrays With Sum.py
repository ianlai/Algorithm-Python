class Solution:
    
    # 2022/01/22
    # Sliding-Window [O(n): 37%]
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        print("Code3")
        if not nums:
            return 0
        
        #calculate num of method of "<= k" 
        def atMost(nums, k):
            left, curSum, res = 0, 0, 0
            for right in range(len(nums)):
                curSum += nums[right]
                # move left
                while curSum > k:
                    curSum -= nums[left]
                    left += 1
                # move right
                assert curSum <= k
                res += right - left + 1
            return res
        
        if k != 0:
            return atMost(nums, k) - atMost(nums, k-1)
        else:
            return atMost(nums, 0)
    
    # ============================================
    # 2022/01/21
    # Sliding-Window [O(n): 37%]
    def numSubarraysWithSum2(self, nums: List[int], k: int) -> int:
        print("Code2")
        if not nums:
            return 0
        
        def atMost(nums, k):
            left, right = 0, 0
            curSum = 0
            res = 0
            while right < len(nums):
                curSum += nums[right]
                # move left
                while left <= right and curSum > k:
                    curSum -= nums[left]
                    left += 1
                
                assert curSum <= k
                res += right - left + 1
                right += 1
            return res
        
        if k != 0:
            #print("at most k:", k, atMost(nums, k))
            #print("at most k-1:", k-1, atMost(nums, k-1))
            return atMost(nums, k) - atMost(nums, k-1)
        else:
            return atMost(nums, 0)
    
    # ============================================
    # 2022/01/21
    # Prefix Sum [O(n): 20%]
    def numSubarraysWithSum1(self, nums: List[int], goal: int) -> int:
        print("Code1")
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
                