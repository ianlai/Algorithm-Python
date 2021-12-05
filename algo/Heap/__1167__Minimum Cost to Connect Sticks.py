class Solution:
    
    # 2021/12/05
    # Heap [O(n + nlogn)] : 66%
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) <= 1:
            return 0
        
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            s1 = heapq.heappop(sticks)
            s2 = heapq.heappop(sticks)
            newStick = s1 + s2
            heapq.heappush(sticks, newStick)
            cost += newStick
        return cost