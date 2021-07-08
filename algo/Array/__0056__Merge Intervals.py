class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        i, j = 0, 1
        while j < len(intervals):
            if intervals[j][0] <= intervals[i][1]:  #merge
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                intervals.pop(j)
            else:
                i += 1
                j += 1
                
        results = []
        return intervals
                