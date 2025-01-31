class Solution:
    
    # 2022/05/11
    # Sliding window [O(n) : 86 / O(1) : 25%]
    def maxFrequency(self, nums: List[int], k: int) -> int:
        print("Code2")
        
        nums.sort()
        left = 0
        sumup = 0
        maxlen = 0
        for right in range(len(nums)):
            sumup += nums[right]
            while nums[right] * (right - left + 1) > k + sumup:
                sumup -= nums[left]
                left += 1
            maxlen = max(maxlen, right - left + 1)
        return maxlen 
            
        
    # Use count map  [TLE] <--- 不要自找麻煩
    def maxFrequency1(self, nums: List[int], k: int) -> int:
        print("Code1")
        
        numToCount = collections.Counter(nums)
        sortedNums = sorted(numToCount.keys(), key = lambda x: -x)
        
        full = len(nums) * sortedNums[0] 
        prevSum = 0
        curSum = sum(nums)
        curCount = len(nums)
        
        for i, num in enumerate(sortedNums):
            if i > 0:
                prevSum = sortedNums[i-1] * numToCount[sortedNums[i-1]]
                curSum -= prevSum
                curCount -= numToCount[sortedNums[i-1]]
                full = curCount * num
            
            diff = full - curSum
            if diff <= k: #good
                return curCount
        return -1
            