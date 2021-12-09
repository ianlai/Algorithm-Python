class Solution:
        
    # 2021/12/09 
    # Timestamp [O(nlogn + n): 92%]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        print("Code-3: timestamp")
        timeToIntervalCount = collections.defaultdict(int)
        for s, e in intervals:
            timeToIntervalCount[s] += 1
            timeToIntervalCount[e] -= 1     
        
        res = []
        curIntervalCount = 0
        start, end = None, None
        for t, intervalCount in sorted(timeToIntervalCount.items()): 
            curIntervalCount += intervalCount
            if curIntervalCount != 0:
                if start == None: #first
                    start = t 
            else:
                end = t
                if start == None:  #special case: [end, end]
                    res.append([end, end])    
                else:
                    res.append([start, end])
                start, end = None, None
        return res
    
    # =====================================================

    # 2021/12/09
    # Compare the adjacent two intervals (no pop) [O(nlogn): 79%]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        print("Code-2: Compare the adjacent two intervals and put into new list (no pop)")
        if not intervals:
            return []
        
        intervals.sort(key = lambda x: x[0])
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
    
    # =====================================================
        
    # 2021/07/09 
    # Compare the adjacent two intervals (pop one) [O(n^2): 39%]
    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        print("Code-1: ")
        if not intervals:
            return []
        
        intervals.sort()
        i, j = 0, 1
        while j < len(intervals):
            if intervals[j][0] <= intervals[i][1]:  #merge
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                intervals.pop(j) #O(n) operation
            else:
                i += 1
                j += 1
        return intervals