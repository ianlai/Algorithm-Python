class Solution:
    
    # 2022/02/10
    # Greedy [O(n): 22%]
    def canReorderDoubled(self, arr: List[int]) -> bool:
        countPos = collections.defaultdict(int)
        countNeg = collections.defaultdict(int)
        countZero = 0
        
        for v in arr:
            if v == 0:
                countZero += 1
            elif v > 0:
                countPos[v] += 1
            else:
                countNeg[-v] += 1
                
        if countZero % 2 != 0:
            return False
        
        def verifyCountArr(arr):
            for v, count in sorted(arr.items()):
                if arr[v] > arr[v*2]:
                    return False
                arr[v*2] -= arr[v]
                arr[v] = 0
            return True
        
        return verifyCountArr(countPos) and verifyCountArr(countNeg)
            
        