'''
You are given a list of jobs, each job has an ID number(type is long).
Implement two functions,
1.expire(long jobid) to set a job as "expired"
2.isexpired(long jobid) to check if a job is "expired"
'''


'''
T.C. = O(1)
S.C. = O(N)
'''
from bisect import bisect_left


class HashMapApproach:
    def __init__(self):
        self.expiredSet = set()

    def expire(self, id):
        self.expiredSet(id)

    def isexpired(self, id):
        if id in self.expiredSet:
            return True
        return False





class IntervalApproach:
    def __init__(self):
        self.intervals = []

    def expire(self, id):
        if not self.intervals:
            self.intervals.append([id, id])
        else:
            idx = bisect_left(self.intervals, [id, id])
            if id - 1 == self.intervals[idx-1][1] and id + 1 == self.intervals[idx][0]:
                self.intervals[idx-1][1] = self.intervals[idx][1] 
                self.intervals.pop(idx)
            elif
                


    def isexpired(self, id):