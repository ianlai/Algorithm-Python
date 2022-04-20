'''
Problem-1 是否有空餘時間

先確定，是否有排序排好，是否有區段有overlap (本來就不成立）
https://leetcode.com/problems/meeting-rooms/  LC252
Leetcode是全部判斷，Karat是給新增一個來判斷

第一题：类似meeting rooms，输入是一个int[][] meetings, int start, int end, 每个数都是时间，13：00 =》 1300， 9：30 =》 18930， 看新的meeting 能不能安排到meetings

ex: {[1300, 1500], [930, 1200],[830, 845]}, 
新的meeting[820, 830], return true; 
[1450, 1500] return false;
'''

def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True

'''
Problem-2 返回空閒時間段
類似 ​​https://leetcode.com/problems/merge-intervals/  LC56
类似merge interval，唯一的区别是输出，输出空闲的时间段，merge完后，再把两两个之间的空的输出就好，注意要加上0 - 第一个的start time
'''

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