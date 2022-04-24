class Solution:

    # 2022/04/24
    # Sweep line + Map [O(F + FlogF + F + PlogF) = O(FlogF + PlogF): 66% / O(F): 16%]
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        print("Code2")
        
        timeline = collections.defaultdict(int)
        
        for start, end in flowers:
            timeline[start] += 1
            timeline[end + 1] -= 1
        
        timesorted = sorted([[k, v] for k, v in timeline.items()])
        for i in range(1, len(timesorted)):
            timesorted[i][1] += timesorted[i-1][1]

        timelist = [time for time, flower in timesorted]
        res = []
        for p in persons:
            idx = bisect.bisect_right(timelist, p)  #Not bisect_left
            if idx == 0:
                res.append(0)
            else:
                res.append(timesorted[idx-1][1])
        return res 
    
    
    # 2022/04/24 
    # Sweep line + Matrix [TLE]
    def fullBloomFlowers1(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        print("Code1")
        timeline = [0] * (max(persons) + 1) 
        timeprefix = [0] * (max(persons) + 1)
        
        for start, end in flowers:
            if start < len(timeline):
                timeline[start] += 1
            if end + 1 < len(timeline):
                timeline[end + 1] -= 1
        
        timeprefix[0] = timeline[0]
        for i in range(1, len(timeprefix)):
            timeprefix[i] = timeprefix[i-1] + timeline[i]
        
        res = []
        for p in persons:
            res.append(timeprefix[p])
        return res 