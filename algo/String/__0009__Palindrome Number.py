class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        string = str(x)
        s, e = 0, len(string) - 1
        
        while s < e:
            if string[s] != string[e]:
                return False
            s += 1
            e -= 1
        
        return True