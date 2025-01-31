class Solution:
    
    # 2022/05/22
    # Two-Pointer [O(N2): 82% / O(1): 75%]
    def countSubstrings(self, s: str) -> int:
        print("Code2")
        def countPalindromes(left, right):
            count = 0 
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count += 1
                else:
                    break
                left -= 1
                right += 1
            return count
            
        res = 0
        for i in range(len(s)):
            res += countPalindromes(i, i)
            if i > 0:
                res += countPalindromes(i - 1, i)
        return res 
        

    # 2022/02/17
    # Two-Pointer 背向雙指針 [O(n2): 64%]
    def countSubstrings1(self, s: str) -> int:
        print("Code1")
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
    
            