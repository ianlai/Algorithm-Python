class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return True
        for i in range(len(s) - 1):
            subStr = s[:i+1]
            leftStr = s[i+1:]
            #print(leftStr, subStr)
            if len(leftStr) % len(subStr) != 0:
                continue
            if self.checkBySubStr(leftStr, subStr):
                return True
        return False
    def checkBySubStr(self, string, sub):
        if not string:
            return True
        if not string.startswith(sub):
            return False
        return self.checkBySubStr(string[len(sub):], sub)
        