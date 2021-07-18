import heapq
class Solution:
    
    # Sorting [55%]
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        count = 1
        intervals.sort()
        ends = [intervals[0][1]]
        for i in range(1, len(intervals)):
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