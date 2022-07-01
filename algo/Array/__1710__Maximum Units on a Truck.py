class Solution:
    # 2022/07/01
    # Sort and traverse array [O(NlogN): 55% / O(1): 32%]
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        
        totalNum = 0
        for boxNum, oneNum in boxTypes:
            if truckSize >= boxNum:
                totalNum += boxNum * oneNum
                truckSize -= boxNum
            else:
                totalNum += truckSize * oneNum
                truckSize = 0 
            if truckSize == 0:
                break
        return totalNum
                
            