import heapq
class Solution:
    
    # 2022/04/07
    # Heap [O(n + nlogn): 57%]
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [-v for v in stones] 
        heapq.heapify(hp)
        while len(hp) > 1:
            stone1 = -heapq.heappop(hp)
            stone2 = -heapq.heappop(hp)
            if stone1 != stone2:
                heapq.heappush(hp, stone2 - stone1)  #negative value
        return -hp[0] if len(hp) > 0 else 0