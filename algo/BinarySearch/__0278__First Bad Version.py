# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 
        count = 0
        start, end = 1, n 
        while start + 1 < end: 
            count += 1 
            mid = start + (end - start) // 2 
            testResult = isBadVersion(mid)
            if testResult:
                end = mid
            else: 
                start = mid
        #print(count)
        if isBadVersion(start):
            return start
        if isBadVersion(start + 1):
            return start + 1
        if isBadVersion(end):
            return end
        return -1