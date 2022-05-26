class Solution:
    
    # 2022/05/26 
    # Increasing Sub + Binary search [O(nlogn): 83% / O(n): 14%] 
    def lengthOfLIS(self, nums: List[int]) -> int:    
        print("Code3")
        def binarySearchLeft(arr, v):
            start, end = 0, len(arr)
            while start < end:
                mid = start + (end - start) // 2
                if arr[mid] < v:
                    start = mid + 1
                else:
                    end = mid 
            return start
        
        seq = []
        for v in nums:
            idx = binarySearchLeft(seq, v)
            if idx == len(seq):
                seq.append(v)
            else:
                seq[idx] = v
        return len(seq)
            
        
    # 2022/03/06
    # Build smallest-val subsequence with Binary Search  [O(nlogn): 98%]
    # Patience Sorting 
    # https://leetcode.com/problems/longest-increasing-subsequence/discuss/74848/9-lines-C++-code-with-O(NlogN)-complexity/337602
    # https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
    def lengthOfLIS2(self, nums: List[int]) -> int:    
        print("Code2")
        if not nums:
            return 0
        subsequence = [nums[0]]
        for i in range(1, len(nums)):
            #print(i, "  ", subsequence)
            v = nums[i]
            if v > subsequence[-1]:
                subsequence.append(v)
            else:
                idx = bisect.bisect_left(subsequence, v)
                subsequence[idx] = v
            #print(i, "__", subsequence)
        return len(subsequence)
                       
    # ==========================================================
    # 2021/07/08 
    # DP [O(n2): 46%]
    def lengthOfLIS1(self, nums: List[int]) -> int:
        print("Code1")
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        #print(dp)
        return max(dp)