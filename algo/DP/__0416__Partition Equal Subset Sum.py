class Solution:
    
    # Buttom-Up DP [O(n * num of reachable sum) : 85%]  //大神
    def canPartition(self, nums: List[int]) -> bool:
        print("Buttom-Up, iterate the map")
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total / 2

        reachable_sum = {0}
        for num in nums:
            if target - num in reachable_sum:
                return True
            next_sum = {n + num for n in reachable_sum if n + num < target}
            reachable_sum.update(next_sum)
        return False
    
    # ==============================================
    # Buttom-Up DP [O(n * sum/2) : 36%]
    # Find a True in the last column then return True -> 48%
    # 使用Array來標記可以達到的sum，但如果nums內的元素很大代表一次可以跳一大步(sparse)，
    # 如此卻還每次都一格一格走就會浪費時間，反而比Top-Down的作法更花時間。
    # 因此可以使用Set來做Buttom-Up
    
    def canPartition2(self, nums: List[int]) -> bool:
        print("Buttom-Up DP")
        if not nums:
            return True
        target = sum(nums) 
        if target % 2 != 0:
            return False
        target = int(target / 2)
        print("target=", target)
        
        # Initialize
        dp = [[0 for _ in range(target+1)] for _ in range(len(nums))]
        dp[0][0] = 1
        if nums[0] < len(dp):
            dp[0][nums[0]] = 1
        
        # DP
        for i in range(1, len(nums)):
            for j in range(target):
                if dp[i-1][j]:
                    if j + nums[i] <= target:
                        dp[i][j+nums[i]] = 1
                    dp[i][j] = 1
                    
                    if dp[i][target] == 1: #Find solution
                        return True
                    
        # for i in range(len(dp)):
        #     print(dp[i])
        
        return False
    
    # ==============================================
    # Memoization DP [O(sum/2) : 74%]
    def canPartition1(self, nums: List[int]) -> bool:
        print("Memoization")
        if not nums:
            return True
        target = sum(nums) 
        if target % 2 != 0:
            return False
        target = target // 2 
        memo = set()
        return self.targetSum(nums, 0, target, memo)
        
    def targetSum(self, nums, idx, target, memo):
        if target == 0:
            return True
        if target in memo:
            return False
        if idx >= len(nums):
            return False
        
        if self.targetSum(nums, idx + 1, target - nums[idx], memo):
            return True
        if self.targetSum(nums, idx + 1, target, memo):
            return True
        memo.add(target) 
        return False