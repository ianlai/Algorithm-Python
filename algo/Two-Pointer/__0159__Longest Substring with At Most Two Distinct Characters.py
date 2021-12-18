class Solution:
    
    # Two Pointer, Sliding Window [O(n): 41%]
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
        
        charCount = collections.defaultdict(int)
        charCount[s[0]] += 1
        charCount[s[1]] += 1
        
        maxLength = 2
        left, right = 0, 2
        while right < len(s):
            charCount[s[right]] += 1
            while len(charCount) > 2:
                if s[left] in charCount:    
                    charCount[s[left]] -= 1
                    if charCount[s[left]] == 0:
                        del charCount[s[left]]
                left += 1      
            maxLength = max(maxLength, right - left + 1) 
            right += 1
        return maxLength