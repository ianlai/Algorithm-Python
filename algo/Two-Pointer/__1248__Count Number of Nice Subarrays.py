class Solution:
    
    # 2022/01/20
    # Sliding window   [O(n): 45%]
    # exact(n) = atMost(n) - atMost(n-1)  (because we can only find atMost)
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        def atMost(nums, k):
            left, right = 0, 0
            niceCount = 0
            res = 0
            while right < len(nums):
                
                if nums[right] % 2 == 1:
                    niceCount += 1
                    
                # move left
                while niceCount > k:
                    if nums[left] % 2 == 1:
                        niceCount -= 1
                    left += 1
                
                assert niceCount <= k 
                res += right - left + 1  #subarray [left:left+1] ~ [left:right] are nice
                right += 1
            return res
        
        #print("at most k:", k, atMost(nums, k))
        #print("at most k-1:", k-1, atMost(nums, k-1))
        
        return atMost(nums, k) - atMost(nums, k-1)