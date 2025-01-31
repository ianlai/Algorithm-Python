class Solution:
    
    # 2022/01/22
    # Sliding Window [O(n): 48%]
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        print("Code2")
        if len(s) <= k:
            return len(s)
        
        #charCount = collections.Counter() #slower
        charCount = collections.defaultdict(int) #faster

        maxLength = 0
        left = 0
        for right in range(len(s)):
            charCount[s[right]] += 1
            while len(charCount) > k:
                charCount[s[left]] -= 1
                if charCount[s[left]] == 0:
                    del charCount[s[left]]
                left += 1      
            maxLength = max(maxLength, right - left + 1) 

        return maxLength

    # =======================================
    
    # 2021/12/19
    # Two-Pointer, Sliding Window [O(n): 48%]
    def lengthOfLongestSubstringKDistinct1(self, s: str, k: int) -> int:
        print("Code1")
        if len(s) <= k:
            return len(s)
        
        charCount = collections.defaultdict(int)
        charCount[s[0]] += 1 
        
        maxLength = 0
        left, right = 0, 1
        while right < len(s):
            charCount[s[right]] += 1
            while len(charCount) > k:
                if s[left] in charCount:    
                    charCount[s[left]] -= 1
                    if charCount[s[left]] == 0:
                        del charCount[s[left]]
                left += 1      
            maxLength = max(maxLength, right - left + 1) 
            right += 1
        return maxLength