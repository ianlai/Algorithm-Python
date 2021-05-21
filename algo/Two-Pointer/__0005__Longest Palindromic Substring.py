class Solution:
    
    # 背向雙指針 [O(n2), 43%]
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        (_, _, resultMax) = self.longestPalindromeStartAt(s, 0, 0)
        resultStr = s[0]
        
        for i in range(1, len(s)):
            (l1, r1, max1) = self.longestPalindromeStartAt(s, i, i)
            (l2, r2, max2) = self.longestPalindromeStartAt(s, i - 1, i) 
            if max1 > resultMax:
                resultStr = s[l1:r1 + 1]
                resultMax = max1 
                #print("max1", resultStr)
            if max2 > resultMax:
                resultStr = s[l2:r2 + 1] 
                resultMax = max2
                #print("max2", resultStr)
        return resultStr 
            
    def longestPalindromeStartAt(self, s, lStart, rStart):
        l, r = lStart, rStart
        while 0 <= l < len(s) and 0 <= r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1 
            else:
                break
        return (l + 1, r - 1, r - l - 1) # (r-l-1) = (r-1) - (l+1) + 1
