import heapq
class Solution:

    # Greedy [O(n): 34%]
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        print("Code3")
        intervals.sort(key = lambda x: x[1])
        lastEnd = -inf
        count = 0
        for start, end in intervals:
            if start >= lastEnd:
                count += 1
                lastEnd = end
        return len(intervals) - count 
        
    # ============================================
        
    # DP [O(n2): TLE]
    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        print("Code2")
        dp = [0] * len(intervals)
        dp[0] = 1
        intervals.sort(key = lambda x: x[0])
        #print(intervals)
        for i in range(1, len(intervals)):
            for j in range(i):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1) #use i or not 
                else:
                    dp[i] = max(dp[i], 1)
        #print(dp)
        return len(intervals) - dp[-1]
        
    # ============================================
        
    # 2022/01/28
    # Heap [Incorrect ]
    def eraseOverlapIntervals1(self, intervals: List[List[int]]) -> int:
        print("Code1")
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x[0])
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
        print(heaps)
        maxHeapLen = 0
        totalHeapLen = 0
        for heap in heaps:
            totalHeapLen += len(heap)
            maxHeapLen = max(maxHeapLen, len(heap))
        print(totalHeapLen - maxHeapLen)
        return totalHeapLen - maxHeapLen