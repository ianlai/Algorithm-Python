class Solution:
    def minimizeResult(self, expression: str) -> str:
        v1, v2 = expression.split('+')

        maxValue = inf
        maxTuple = None
        for i in range(len(v1)):
            isAdded1 = False
            isAdded2 = False
            v1L = 0
            if len(v1[:i]) == 0:
                v1L = 1
                isAdded1 = True
            else:
                v1L = int(v1[:i])
                
            v1R = int(v1[i:])
            for j in range(len(v2)):
                v2L = int(v2[:j+1])
                v2R = 0
                if len(v2[j+1:]) == 0:
                    v2R = 1
                    isAdded2 = True
                else: 
                    v2R = int(v2[j+1:])
                
                cur = v1L * (v1R + v2L) * v2R
                if cur < maxValue:
                    maxValue = cur
                    maxTuple = (v1L, v1R, v2L, v2R, isAdded1, isAdded2)
                    
        res = "" 
        if not maxTuple[4]:
            res += str(maxTuple[0]) 
        
        res += "(" + str(maxTuple[1]) + "+" + str(maxTuple[2]) + ")" 
        
        if not maxTuple[5]:
            res += str(maxTuple[3])
        return res
                