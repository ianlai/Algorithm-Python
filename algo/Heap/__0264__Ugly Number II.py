class Solution:
    
    # Heap + Hashset [O(nlogn), 55%]
    def nthUglyNumber(self, n: int) -> int:
        print("now")
        if n == 1:
            return 1
        
        nums = [1]
        visited = set([1])
        
        for i in range(n):
            val = nums[0]       #get min
            for n in [val * 2, val * 3, val * 5]:
                if n in visited:
                    continue
                heapq.heappush(nums, n)
                visited.add(n)
            #print(sorted(nums))
            heapq.heappop(nums) #remove min
        return val
    
    def nthUglyNumber1(self, n: int) -> int:
        print("1")
        if n == 1: 
            return 1
        
        hp = [1]
        visited = set([1])
        
        round = 0
        while round < n:  #logic can handle n=1 but we can return earlier if it's special case
            round += 1 
            
            minVal = heapq.heappop(hp) 
                
            #print(round, minVal, visited, hp)
            
            next2 = minVal * 2
            next3 = minVal * 3
            next5 = minVal * 5
            
            if next2 not in visited:
                heapq.heappush(hp, next2)
                visited.add(next2)

            if next3 not in visited:
                heapq.heappush(hp, next3)
                visited.add(next3)
            
            if next5 not in visited:
                heapq.heappush(hp, next5)
                visited.add(next5)
            
        return minVal