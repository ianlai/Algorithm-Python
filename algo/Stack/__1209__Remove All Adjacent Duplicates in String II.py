class Solution:
    
    # 2022/05/06
    # Stack [O(n): 28% / O(n): 69%]
    def removeDuplicates(self, s: str, k: int) -> str:
        print("Code2")
        stack = []
        for c in s:
            if not stack or (stack and stack[-1][0] != c):
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        res = ""
        for e, count in stack:            
            res += e * count
        return res
    
    # Brute Force [TLE]
    def removeDuplicates1(self, s: str, k: int) -> str:
        print("Code1")
        while True:
            i = 0
            newS = ""
            isFound = False
            while i <= len(s) - k:
                isRemovable = True
                first = s[i]
                for j in range(k-1):
                    if first != s[i+j+1]:
                        isRemovable = False
                        break
                if isRemovable:
                    isFound = True
                    i += k
                else:
                    newS += s[i]
                    i += 1
            newS += s[i:]
            if not isFound:
                return newS 
            s = newS