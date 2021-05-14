class Solution:
    

    def maxSubArray(self, nums: List[int]) -> int:
        print("Two pointer O(n); no extra array")
        if not nums:
            return 0
        maxVal = 0 
        max
        left, right = 0, 0
        while left < right and right < len(nums): 
            if nums[right] > 0:
                right += 1
                maxVal += e
            else:
                left += 1 
                
    
    # Enumerate; create preSum array first [O(n), 9%] 
    def maxSubArray(self, nums: List[int]) -> int:
        print("Enumerate O(n); create preSum")
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
