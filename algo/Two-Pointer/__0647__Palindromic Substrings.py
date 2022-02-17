class Solution:
    
    # Two-Pointer 背向雙指針 [O(n2): 64%]
    def countSubstrings(self, s: str) -> int:
        def countPalindrome(start, end):
            count = 0
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    count += 1
                    start -= 1
                    end += 1
                else:
                    break
            return count 
                    
        count = 1
        for i, ch in enumerate(s):
            if i == 0:
                continue
            for j in range(2):
                if j == 0:
                    count += countPalindrome(i, i)
                if j == 1 and s[i] == s[i-1]:
                    count += countPalindrome(i-1, i)
        return count
    
            