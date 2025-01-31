class Solution:
    
    # Sorting 
    def isAnagram(self, s: str, t: str) -> bool:
        if s is None or t is None:
            return False 
        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False