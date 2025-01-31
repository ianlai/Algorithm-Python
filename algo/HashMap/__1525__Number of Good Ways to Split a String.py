class Solution:
    
    # Count in two set [O(n): 80%]
    def numSplits(self, s: str) -> int:
        if not s:
            return 0
        leftCount = collections.defaultdict(int)
        rightCount = collections.defaultdict(int)
        for ch in s:
            rightCount[ch] += 1
            
        count = 0
        for ch in s:
            leftCount[ch] += 1
            rightCount[ch] -= 1
            if rightCount[ch] == 0:
                del rightCount[ch]
            if len(leftCount) == len(rightCount):
                count += 1
        return count