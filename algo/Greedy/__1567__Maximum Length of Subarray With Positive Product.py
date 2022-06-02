class Solution:
    
    # 2022/06/02 
    # Greedy; Linear scan; store the wall points [O(N): 95% / O(N): 21%]
    def getMaxLen(self, nums: List[int]) -> int:
        print("Code1")
        walls = [-1]
        for i, v in enumerate(nums):
            if v == 0:
                walls.append(i)
        walls.append(len(nums))
        
        res = 0
        for i in range(1, len(walls)):
            w1, w2 = walls[i-1], walls[i]
            countNegative = 0
            firstNegative = -1
            lastNegative = -1
            for j in range(w1+1, w2): # No j is either 0 or out of boundaries 
                if nums[j] < 0:
                    if firstNegative == -1:
                        firstNegative = j 
                    countNegative += 1
                    lastNegative = j
                    
            if countNegative % 2 == 0: 
                res = max(res, w2 - w1 - 1)
            else:
                res = max(res, w2 - firstNegative - 1)
                res = max(res, lastNegative - w1 - 1)
        return res
