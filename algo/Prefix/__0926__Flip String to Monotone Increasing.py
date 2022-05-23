class Solution:
    
    # 2022/05/23
    # Prefix Sum [O(N): 15% / O(N): 24%]
    def minFlipsMonoIncr(self, s: str) -> int:
        print("Code1")
        presum = [int(s[0])]
        for i in range(1, len(s)):
            presum.append(presum[-1] + int(s[i]))
        totalsum = presum[-1]
        
        minDiff = min(len(s) - totalsum, totalsum)
        for i in range(1, len(s)):
            diff = presum[i-1] + (len(s) - i) - (totalsum - presum[i-1])
            minDiff = min(minDiff, diff)        
        return minDiff 