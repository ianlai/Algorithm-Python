from typing import List

'''
======================================
[Problem-1] 是否有空餘時間

先確定是否有排序排好, 是否有區段有overlap (本來就不成立）
https://leetcode.com/problems/meeting-rooms/  LC252
Leetcode是全部判斷, Karat是給新增一個來判斷

第一题: 类似meeting rooms, 输入是一个int[][] meetings, int start, int end, 
每个数都是时间, 13: 00 => 1300, 9:30 => 930  看新的meeting 能不能安排到meetings

ex: {[1300, 1500], [930, 1200],[830, 845]}, 
新的meeting[820, 830], return true; 
[1450, 1500] return false;
'''

def canAttendMeetings(intervals: List[List[int]], newMeeting) -> bool:
    print("new meeting:", newMeeting)

    intervals.sort()
    if newMeeting[1] <= intervals[0][0]:
        print("before meetings")
        return True
    if newMeeting[0] >= intervals[-1][1]:
        print("after meetings")
        return True

    for i in range(1, len(intervals)):
        if intervals[i-1][1] <= newMeeting[0] and newMeeting[1] <= intervals[i][0]:
            print("in meetings")
            return True
    return False

meetings = [[1300, 1500], [930, 1200],[830, 845]]
print(canAttendMeetings(meetings, [820, 830]))    #True
print(canAttendMeetings(meetings, [820, 840]))    #False
print(canAttendMeetings(meetings, [1200, 1310]))  #False
print(canAttendMeetings(meetings, [900, 930]))    #True
print(canAttendMeetings(meetings, [1500, 1600]))  #True

'''
======================================
[Problem-2] 返回空閒時間段
類似 https://leetcode.com/problems/merge-intervals/  LC56
类似merge interval, 唯一的区别是输出, 输出空闲的时间段, merge完后, 再把两两个之间的空的输出就好, 注意要加上0 - 第一个的start time
(假設區間是有重複的)

'''

def merge(intervals: List[List[int]]) -> List[List[int]]:
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

# Define:
#   if no intervals at all -> [[0000, 2400]]
def findSpareTime(intervals):
    if len(intervals) == 0:
        return [[0, 2400]]
    mergedIntervals = merge(intervals)

    res = [[0, mergedIntervals[0][0]]]
    for i in range(1, len(mergedIntervals)):
        res.append([mergedIntervals[i-1][1], mergedIntervals[i][0]])
    res.append([mergedIntervals[-1][1], 2400])
    return res

meetings = [
    [1300, 1500], 
    [930, 1200],
    [830, 845],
    ]
print(findSpareTime(meetings))