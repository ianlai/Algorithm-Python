class Solution:

    # ==========================================
    # 2021/02/01
    # Kadane algorithm [O(n): 14%]
    # 如果新的v加進來之後反而變小，那就直接從該點開始 
    def maxSubArray(self, nums: List[int]) -> int: 
        print("Code5: Kadane algorithm")
        curSum = 0
        maxSum = -inf
        for v in nums:
            curSum = max(v, curSum + v)
            maxSum = max(maxSum, curSum)
        return maxSum
    
    # ==========================================
    # 2021/02/01
    # Kadane algorithm [O(n): 12%]
    # subarray變成0就不要了 
    def maxSubArray4(self, nums: List[int]) -> int: 
        print("Code4: Kadane algorithm")
        curSum = 0
        maxSum = -inf
        for v in nums:
            curSum += v
            maxSum = max(maxSum, curSum)
            if curSum <= 0:
                curSum = 0
        return maxSum
    
    # ==========================================
    # 2021/02/01
    # Optimized brute force [O(n2): TLE]
    def maxSubArray3(self, nums: List[int]) -> int: 
        print("Code3: Optimized brute force")
        maxSum = -inf
        for i in range(len(nums)):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                maxSum = max(maxSum, curSum)
        return maxSum
                
    # ==========================================
    # Enumerate; create preSum array first [O(n), 9%] 
    def maxSubArray2(self, nums: List[int]) -> int:
        print("Code2: Enumerate O(n); create preSum")
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        preSum = [0]
        for i in range(len(nums)):
            preSum.append(preSum[-1] + nums[i])
        
        maxSum = -float('inf')
        minSum = float('inf')
        for i in range(2, len(preSum)):
            minSum = min(preSum[i-1], minSum)
            if minSum > 0:
                maxSum = max(preSum[i], maxSum)  
            else:
                maxSum = max(preSum[i]-minSum, maxSum)
            #print(i, minSum, maxSum)
        return max(maxSum, preSum[1])
    
    # ==========================================
    def maxSubArray1(self, nums: List[int]) -> int:
        print("Divide and Conquer")
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)
        
        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)
