class Solution:
    
    # 2022/06/23
    # Heap [O(nlogn + nlogn): 20% / O(n): 51%]
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        h = []
        cur = 0
        courses.sort(key = lambda x: x[1])
        for duration, lastDay in courses:
            heapq.heappush(h, -duration)
            cur += duration 
            while cur > lastDay:
                pop = heapq.heappop(h)
                cur += pop
        return len(h)
            
    
    # Greedy [Incorrect]
    def scheduleCourse1(self, courses: List[List[int]]) -> int:
        carr = []
        for duration, last in courses:
            heapq.heappush(carr, (last - duration, duration, last))
        cur = 0
        count = 0
        while carr:
            pop = heapq.heappop(carr)
            if cur + pop[1] > pop[2]:
                continue
            cur += pop[1]
            count += 1
        return count