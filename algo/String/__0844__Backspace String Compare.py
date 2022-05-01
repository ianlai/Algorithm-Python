class Solution:
    
    # 2022/05/01
    # Reverse traverse [O(n): 63% / O(n): 25%]
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def process(s):
            sharpCount = 0
            sarr = []
            for i in reversed(range(len(s))):
                if s[i] == "#":
                    sharpCount += 1
                else:
                    if sharpCount > 0:
                        sharpCount -= 1
                        continue 
                    sarr.append(s[i])
                    
            return sarr
    
        sarr = process(s)
        tarr = process(t)
        return sarr == tarr
        
        