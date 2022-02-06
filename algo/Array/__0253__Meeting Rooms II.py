import heapq
class Solution:
    
    # 2022/02/06
    # Sweep line [O(nlogn): 21%]
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        print("Code3")
        times = collections.defaultdict(int)
        for start, end in intervals:
            times[start] += 1
            times[end] -= 1
        res = cur = 0 
        for time in sorted(times.keys()):
            cur += times[time] 
            res = max(cur, res)
        return res
    
    # ========================================
    
    # 2022/01/28
    # Multiple heaps [O(nlogn): 31%]
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        print("Code2")
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[0]) #sort by start
        heaps = []
        for start, end in intervals:
            isInserted = False
            for heap in heaps:
                if start >= -heap[0]:
                    heapq.heappush(heap, -end)
                    isInserted = True
                    break
            if not isInserted:
                heaps.append([-end])
        return len(heaps)
    
    # ========================================
    
    # 2021/07/19
    # Sorting [55%]
    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        print("Code1")
        if not intervals:
            return 0
        
        count = 1
        intervals.sort()
        ends = [intervals[0][1]]
        for i in range(1, len(intervals)):
            print(ends)
            start = intervals[i][0]
            ends.sort()
            newRoom = True
            for end in ends:
                if start >= end:
                    ends.remove(end)
                    ends.append(intervals[i][1])
                    newRoom = False
                    break
            if newRoom:
                ends.append(intervals[i][1])
                count += 1
        return count