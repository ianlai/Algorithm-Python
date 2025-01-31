class Solution:
    
    # Binary Search (值域) [O(nlogn): 26%]
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def checkFeasible(weights, days, maxWeight):
            leftWeight = maxWeight
            for w in weights:
                if w > maxWeight:
                    return False
                    
                leftWeight -= w
                if leftWeight < 0:
                    days -= 1
                    if days <= 0:
                        return False
                    leftWeight = maxWeight
                    leftWeight -= w
            return True
        
        sumWeight = 0
        for v in weights:
            sumWeight += v
        
        start, end = 0, sumWeight + 1
        while start < end:
            mid = start + (end - start) // 2
            if checkFeasible(weights, days, mid):
                end = mid
            else:
                start = mid + 1
        return start 
                
            
        
                    
                    