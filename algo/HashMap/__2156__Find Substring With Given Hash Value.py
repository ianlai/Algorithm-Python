class Solution:
    
    # 2022/02/02
    # Rolling hash from tail (using module number) [O(n): 79%]
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        print("Code2")
        powerList = [1]
        for i in range(1, k):
            powerVal = (powerList[i-1] * power) % modulo
            powerList.append(powerVal)
            
        res = None
        hashVal = 0
        for i in range(k):
            idx = len(s) - k + i
            hashVal += (ord(s[idx]) - ord('a') + 1) * (powerList[i]) 
            hashVal %= modulo
        if hashVal == hashValue:
            res = s[len(s)-k:]

        for i in range(len(s)-1, k-1, -1):
            hashVal -= (ord(s[i]) - ord('a') + 1) * powerList[k-1]
            hashVal = hashVal * power
            hashVal += (ord(s[i-k]) - ord('a') + 1) 
            hashVal %= modulo
            
            if hashVal == hashValue:
                res = s[i-k:i]
        return res
    
    
    # ============================================
    # 2022/01/30
    # Rolling hash from head (using no module number) [TLE]
    def subStrHash1(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        print("Code1")
        powerList = [1]
        for i in range(1, k):
            powerVal = (powerList[i-1] * power) % modulo
            powerList.append(powerVal)
            
        for i in range(len(s)-k+1):
            originalHash, countedHash = 0, 0
            if i == 0:          
                for j in range(k):
                    originalHash += (ord(s[i+j]) - ord('a') + 1) * (powerList[j]) 
                countedHash = originalHash % modulo
            else:
                originalHash = lastCountedHash 
                originalHash -= (ord(s[i-1]) - ord('a') + 1)
                originalHash = originalHash // power
                originalHash += (ord(s[i+k-1]) - ord('a') + 1) * (powerList[k-1])
                countedHash = originalHash % modulo
            if countedHash == hashValue:
                return s[i:i+k]
            lastCountedHash = originalHash
        return -1