class Solution:
    
    # 2022/05/28 
    # Counter Hashmap [O(C): 58% / O(C): 65%]
    def longestPalindrome(self, s: str) -> int:
        
        charToCount = collections.defaultdict(int)
        
        # count chars
        for ch in s:
            charToCount[ch] += 1
        
        # accumulate counts 
        oddCount, totalCount = 0, 0
        for count in charToCount.values():
            totalCount += count 
            if count & 1 == 0: #odd
                oddCount += count
            else:
                oddCount += count - 1
                
        return oddCount + 1 if oddCount != totalCount else oddCount