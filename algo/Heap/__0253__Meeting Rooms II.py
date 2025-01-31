import heapq
class Solution:
    
    # 2022/04/17
    # One heap to store each room's ending time [O(nlogn): 31%]
    # 在heap中我們存入的是每個房間的end time，找出最早的end time看看下一個會議放不放的進去
    # 因此我們排序必須要按照會議的開始時間，而不是結束時間。
    # 否則可能造成我放入一個最早結束的會議室，但我後面的會議其實更早開始，更適合這間會議室。
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        print("*** Code4")
        intervals.sort(key=lambda x: x[0])  #sort by start (not by end!)
        rooms = [intervals[0][1]] #smallest end
        for s, e in intervals[1:]:
            if s >= rooms[0]:  #good, we can use earliest room
                heapq.heappop(rooms)
            heapq.heappush(rooms, e)
        return len(rooms)
        
    # ========================================

    # 2022/02/06
    # Sweep line [O(nlogn): 21%]
    def minMeetingRooms3(self, intervals: List[List[int]]) -> int:
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
    # 不必要使用多個heap，只要存最後的時間就好(Code4)
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