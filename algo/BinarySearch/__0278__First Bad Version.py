# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    # 2022/03/03 
    # 找值域的基本題，直接把求值域的函數給我們了
    # 找值域的題目只要找到xxxxoooo的最後一個x或是第一個o，反而不用在意重複的元素或找不到元素的狀況
    def firstBadVersion(self, n):
        print("Code2")
        start, end = 1, n
        while start < end:
            mid = start + (end - start) // 2 
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1 
        return start
            
    # ========================================
    # 2021/06/03 
    def firstBadVersion1(self, n):
        print("Code1")
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