class Solution:
    
    # Two-Pointer, Sliding Window [O(n): 48%]
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
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