class Solution:
    
    # 2022/01/12
    # Calculate prefix sum and two-sum method
    # Need to do reverse traverse when finding the num - k  [O(n), 24%]
    def subarraySum(self, nums: List[int], k: int) -> int:
        print("Code3: Count")
        if not nums:
            return 0
        prefixSums = [0] * len(nums)
        prefixCounts = collections.defaultdict(int)
        # init 
        prefixSums[0] = nums[0]
        # loop
        for i in range(1, len(nums)):
            prefixSums[i] = prefixSums[i-1] + nums[i]
        # core
        count = 0
        for i in range(len(nums)-1, -1, -1):
            #(1), (2) cannot swap 
            #(1) Find the current number (num) to accumulate the count
            if prefixSums[i] in prefixCounts:
                count += prefixCounts[prefixSums[i]]
            #(2) Add the current number (num-k) into map so that later we can try to find 
            prefixCounts[prefixSums[i] - k] += 1
        count += prefixCounts[0] #sum from index=0 equals to k 
        
        return count 
    
    # ======================================
    # 2021/05/27
    # Hashmap to calculate the number [O(n), 24%]
    def subarraySum2(self, nums: List[int], k: int) -> int:
        print("Code2: Count")
        if not nums:
            return 0
        n = len(nums)
        sums = [0] * n
        for i in range(n):
            sums[i] = sums[i - 1] + nums[i]
        
        sumToCount = {}
        totalCount = 0
        print(sums)
        for i in range(n - 1, -1, -1):
            #check 
            if sums[i] in sumToCount:
                totalCount += sumToCount[sums[i]]
            #add 
            val = sums[i] - k
            if val in sumToCount:
                sumToCount[val] += 1 
            else:
                sumToCount[val] = 1
                
        if 0 in sumToCount:
            totalCount += sumToCount[0]
        print(sumToCount)
        return totalCount 
    
    # ======================================
    
    # Enumerate [O(n2): TLE]
    def subarraySum1(self, nums: List[int], k: int) -> int:
        print("Code1: Enumerate")
        if not nums:
            return 0
        
        n = len(nums)
        sums = [[0 for j in range(n)] for i in range(n)]

        count = 0   
        sums[0][0] = nums[0]
        if sums[0][0] == k:
            count += 1

        for i in range(1, n):
            sums[0][i] = sums[0][i-1] + nums[i] 
            if sums[0][i] == k:
                count += 1
        
        for i in range(1, n):
            for j in range(i, n):
                sums[i][j] = sums[i-1][j] - nums[i-1]
                if sums[i][j] == k:
                    count += 1
                    
        #print(count)
        #for i in range(len(nums)):
        #    print(sums[i])
        return count 