class Solution:
    # 2021/12/25
    # O(n2): 43%
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        maxPalindrome = ""
        for i in range(len(s)):
            for j in range(2):
                left, right = i, i + j
                length = 0
                while left >= 0 and right < len(s):
                    if s[left] != s[right]:
                        break
                    else:
                        length = right - left + 1 
                        if length > maxLength:
                            maxLength = length
                            maxPalindrome = s[left:right+1]
                    left -= 1
                    right += 1
        return maxPalindrome
    # ==========================================
    # 2021/12/25
    # O(n3): TLE
    def longestPalindrome2(self, s: str) -> str:
        print("Code2")
        for length in range(len(s), 0, -1):
            for i in range(0, len(s) -length + 1, 1):
                left = i
                right = i + length - 1
                isPalindrome = True
                while left <= right:
                    if s[left] != s[right]:
                        isPalindrome = False
                        break
                    left += 1
                    right -= 1
                if not isPalindrome:
                    continue
                return s[i:i+length]

    # ==========================================
    # 2021/05/21
    # 背向雙指針 [O(n2), 89%]
    def longestPalindrome1(self, s: str) -> str:
        print("Code1")
        if not s:
            return ""
        
        (_, _, resultMax) = self.longestPalindromeStartAt(s, 0, 0)
        resultStr = s[0]
        
        for i in range(1, len(s)):
            
            ### (1) Prune the impossible 
            if (i - 0) * 2 < resultMax:
                continue
            if (len(s) - i) * 2 < resultMax:
                continue
                
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
