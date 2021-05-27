class Solution:
    # Hashmap to calculate the number [O(n), 24%]
    def subarraySum(self, nums: List[int], k: int) -> int:
        print("Hashmap")
        if not nums:
            return 0
        n = len(nums)
        sums = [0] * n
        for i in range(n):
            sums[i] = sums[i - 1] + nums[i]
        
        sumToCount = {}
        totalCount = 0
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
        return totalCount 
    
    # ======================================
    
    # Enumerate [O(n2), TLE]
    def subarraySum1(self, nums: List[int], k: int) -> int:
        print("Enumerate")
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