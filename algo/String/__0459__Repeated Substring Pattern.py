class Solution:
    
    #2021/12/25 
    #[O(n/1+n/2+n/3+....+n/n) = O(n2): 51%]
    def repeatedSubstringPattern(self, s: str) -> bool:
        print("Code2")
        for length in range(1, len(s)//2+1):
            if len(s) % length != 0:
                continue
            firstSubstring = s[:length]
            isRepeatedPattern = True
            for i in range(1, len(s)//length):
                if firstSubstring != s[i*length:(i+1)*length]:
                    isRepeatedPattern = False
                    break
            if isRepeatedPattern:
                return True
            
    # =============================================
    
    # 2021/06/28 
    #[O(n2): 6%]
    def repeatedSubstringPattern1(self, s: str) -> bool:
        print("Code1")
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
        