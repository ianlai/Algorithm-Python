class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        
        count = {}
        for i in range(len(s)):  #traversal-1
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
        
        for i in range(len(s)):  #traversal-2
            if count[s[i]] == 1:
                return i
        return -1