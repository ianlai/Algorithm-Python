class Solution:
    
    # 2021/12/05
    # Quick Select [Avg case O(n) -- Worst case O(n2): 99% / 15%]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print("Code7: Quick Select")
        if not nums:
            return []
        
        #Count the numbers (num -> count)
        numToCount = collections.defaultdict(int)
        for num in nums:
            numToCount[num] += 1
        countList = list(numToCount.values())
    
        # Find (len-k)-th from small; k-th from largest
        print(numToCount, countList)
        targetCount = self.findKth(countList, len(countList) - k)
        print(k, "-th max val:", targetCount)
        
        # Generate the results
        results = []
        for num, count in numToCount.items():
            if count >= targetCount:
                results.append(num)
        return results
            
    def findKth(self, arr, k):
        return self.partition(arr, k, 0, len(arr) - 1)
        
    def partition(self, arr, k, start, end):
        #print("S-E:", start, end)
        left, right = start, end
        mid = (start + end) // 2
        pivot = arr[mid]
        while left <= right:
            while left <= right and arr[left] < pivot: 
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        print("start, end:", start, end, arr, "  L-R:", left, right)     
        if k <= right:
            return self.partition(arr, k, start, right)
        if k >= left:
            return self.partition(arr, k, left, end)

        #print("  arr[k]:", k)
        return arr[k] # ..., right, k, left, ...
    
    # ============================================
    
    # 2021/12/05
    # Min-Heap [O(k + (n-k)logk): 76%]
    def topKFrequent6(self, nums: List[int], k: int) -> List[int]:
        print("Code6: K-size Min Heap")
        if not nums:
            return []
        
        #Count 
        numToCount = collections.defaultdict(int)
        for e in nums:
            numToCount[e] += 1 
        
        minhp = []      
        numToCountArr = list(numToCount.items())
        #Iterate 0 ~ k-1
        for i in range(k):
            num, count = numToCountArr[i][0], numToCountArr[i][1]
            heapq.heappush(minhp, (count, num))
        #Iterate from k
        for i, v in enumerate(numToCountArr[k:]):
            num, count = v[0], v[1]
            minVal = minhp[0][0]
            if count > minVal:
                heapq.heappop(minhp)
                heapq.heappush(minhp, (count, num))

        return [e[1] for e in minhp]
            
    # ============================================
    
    # 2021/12/05
    # Max-Heap [O(n + klogn): 89%]
    def topKFrequent5(self, nums: List[int], k: int) -> List[int]:
        print("Code5: N-size Max Heap")
        if not nums:
            return []
        
        #Count 
        numToCount = collections.defaultdict(int)
        for e in nums:
            numToCount[e] += 1 
                
        #Store to tuples into heap (maxheap)
        heapCountToNum = []
        #heapq.heapify(countToNum)
        for num, count in numToCount.items():
            heapq.heappush(heapCountToNum, (-count, num))
        
        #Heappop k items 
        res = []
        for _ in range(k):
            cur = heapq.heappop(heapCountToNum)[1]
            res.append(cur)
        return res
    
    # ============================================
    
    # 2021/12/05 
    # Sorting [O(nlogn): 76%]
    def topKFrequent4(self, nums: List[int], k: int) -> List[int]:
        print("Code4: Sorting")
        if not nums:
            return []
        
        #Count 
        numToCount = collections.defaultdict(int)
        for e in nums:
            numToCount[e] += 1
        
        ### Clear
        #Store to tuples into list to sort
        countToNum = [(v, k) for k, v in numToCount.items()]

        #Sort the list in descending 
        countToNum.sort(reverse=True)    
        return [n[1] for n in countToNum[:k]]
    
        ### Shorter 
        return [t[0] for t in sorted(numToCount.items(), key = lambda x: -x[1])][:k]
    
    # ============================================
    # 2021/06/25 
    # Quick Select [72% / 53%]
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        print("Code3: Quick Select")
        if not nums:
            return []
        
        #Count the numbers (num -> count)
        numToCount = collections.defaultdict(int)
        for num in nums:
            numToCount[num] += 1
        countList = list(numToCount.values())
        #print(numToCount)
        #print(countList)
    
        # Find kth from small 
        targetCount = self.findKth1(countList, len(countList) - k)
        #print("targetCount:", targetCount)
        
        # Generate the results
        results = []
        for num, count in numToCount.items():
            if count >= targetCount:
                results.append(num)
        return results
            
    def findKth1(self, arr, k):
        return self.partition1(arr, k, 0, len(arr) - 1)
        
    def partition1(self, arr, k, start, end):
        #print(start, end)
        left, right = start, end
        mid = (start + end) // 2
        pivot = arr[mid]
        while left <= right:
            while left <= right and arr[left] < pivot: 
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        if k <= right:
            return self.partition1(arr, k, start, right)
        if k >= left:
            return self.partition1(arr, k, left, end)
        return arr[k]
    
        # print("OUT:", k)
        # print(right, left)
        
        # if left == k:
        #     return arr[left] 
        # elif left < k :
        #     return self.partition(arr, k, left, end)
        # else:
        #     return self.partition(arr, k, start, left)
        
    # ============================================
    # 2021/05/10
    # Hashmap + Heap [O(klogn), 67%]
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        print("Code2: Heap")
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
    
    # ============================================
    
    # 2021/05/07 
    # Hashmap + Sorting [O(nlogn), 67%]
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        print("Code1: Sorting")
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