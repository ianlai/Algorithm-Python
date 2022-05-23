class Solution:
    
    # 2022/05/23
    # Prefix Sum (反向，只記錄變化值) [O(N+U): 30% / O(N): 53%]
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        print("Code2")
        changingArr = [0] * (length + 1)
        for s, e, d in updates:
            changingArr[s] += d
            changingArr[e+1] -= d
        
        res = [0] * (length + 1)
        for idx, d in enumerate(changingArr):
            if idx == 0:
                res[idx] = d
            else:
                res[idx] = res[idx-1] + d
        return res[:len(res)-1]
    
    # 2022/05/23
    # Native [O(NU): TLE / O(1)]
    def getModifiedArray1(self, length: int, updates: List[List[int]]) -> List[int]:
        print("Code1")
        arr = [0] * length
        for s, e, d in updates:
            for j in range(s, e+1):
                arr[j] += d
        return arr