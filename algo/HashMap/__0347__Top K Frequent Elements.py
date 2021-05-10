class Solution:
    
    #Hashmap + Heap [O(klogn), 67%]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print("Heap")
        if not nums:
            return []
        
        #Count 
        numTocount = {}
        for e in nums:
            if e in numTocount:
                numTocount[e] += 1
            else:
                numTocount[e] = 1     
                
        #Store to tuples into heap (maxheap)
        countToNum = []
        #heapq.heapify(countToNum)
        for key in numTocount.keys():
            heapq.heappush(countToNum, (-numTocount[key], key))
        
        #Heappop k items 
        ans = []
        for _ in range(k):
            cur = heapq.heappop(countToNum)[1]
            ans.append(cur)
        return ans
    
    #Hashmap + Sorting [O(nlogn), 67%]
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        print("Sorting")
        if not nums:
            return []
        
        #Count 
        numTocount = {}
        for e in nums:
            if e in numTocount:
                numTocount[e] += 1
            else:
                numTocount[e] = 1     
                
        #Store to tuples into list to sort
        countToNum = []
        for key in numTocount.keys():
            countToNum.append((numTocount[key], key))

        #Sort the list in descending 
        countToNum.sort(reverse=True)
        return [x[1] for x in countToNum[:k]] 