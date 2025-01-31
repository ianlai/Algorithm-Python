class Solution:

    # 2022/04/03 
    # Binary Search 值域 [O(log(max candy) * candy length): 40%]
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        def check(allocate):
            total = 0 
            for c in candies:
                total += c // allocate 
                if total >= k:
                    return True
            return False
            
        start, end = 1, max(candies) + 1
        while start < end:
            mid = start + (end - start) // 2
            if check(mid):
                start = mid + 1
            else:
                end = mid
        return start - 1
        
        
##### Insert to sorted array
#       if len(candies) >= k:
#           candies.sort(reverse=True)
#          return candies[k-1]
        
#         candies.sort(reverse=True)
#         while True:
#             while len(candies) > k:
#                 candies.pop()
#             pop = candies[0]
#             candies.pop(0)
#             if pop % 2 == 0:
#                 idx = bisect.bisect_right(candies, pop)
#                 candies.insert(idx, pop // 2)
#                 candies.insert(idx, pop // 2)
#             else:
#                 idx = bisect.bisect_right(candies, pop)
#                 left = pop - pop//2
#                 candies.insert(idx, pop//2)
#                 candies.insert(idx, left)
#             print(candies)
        

##### Use heap  
#         hp = [-v for v in candies]
#         heapq.heapify(hp)
#         maxVal = 0
#         while True:
#             pop = heapq.heappop(hp)
#             while len(hp) > k:
#                 #heapq.heappop(hp)
#             if pop % 2 == 0:
#                 heapq.heappush(hp, pop // 2)
#                 heapq.heappush(hp, pop // 2)
#             else:
#                 left = pop - (pop // 2)
#                 heapq.heappush(hp, pop // 2)
#                 heapq.heappush(hp, left)
#             curVal = -max(hp)
#             print(pop, hp, curVal, maxVal)
#             if curVal > maxVal:
#                 maxVal = curVal
#             else:
#                 return maxVal