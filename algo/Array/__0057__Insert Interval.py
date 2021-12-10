class Solution:
    
    # Keep forming bigger newInterval [O(n): 52%]
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
            
        isNewIntervalInserted = False
        for s, e in intervals:
            if newInterval[0] > e:
                res.append([s, e])
            elif newInterval[1] < s:
                if not isNewIntervalInserted:
                    res.append(newInterval)
                    isNewIntervalInserted = True
                res.append([s, e])
            else:
                newInterval[0] = min(newInterval[0], s)
                newInterval[1] = max(newInterval[1], e)
                
        if not isNewIntervalInserted:
            res.append(newInterval)
            
        return res
                