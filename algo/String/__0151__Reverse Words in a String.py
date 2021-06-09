class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        
        arr = s.split()
        return ' '.join(arr[::-1])