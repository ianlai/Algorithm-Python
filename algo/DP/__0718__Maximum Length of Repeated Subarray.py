class Solution:
    
    # 2022/04/14
    # DP reversed [O(MN): 69%, O(MN): 30%]
    def findLength(self, A, B):
        print("Code4")
        m, n = len(A), len(B)
        dp = [[0] * (n+1) for _ in range(m+1)]
        maxLength = 0 
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    maxLength = max(maxLength, dp[i][j])
        return maxLength
        
    #======================================= 
    # 2021/11/14
    # DP (2D array) [O(n2): 82%]
    def findLength3(self, A, B):
        print("Method3: 2D array 正著走; 全部的點都走過")
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        count = 0
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                count += 1 
                print(count)
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
        return max(max(row) for row in memo)
    
    #=======================================
    
    # DP (2D array) [O(n2): 8%]
    def findLength2(self, nums1: List[int], nums2: List[int]) -> int:
        print("Method2: 2D array 倒著走; 只走有相同的點")
        
        # Preprocess to record the same values in two arrays
        v1ToI2 = collections.defaultdict(list)
        for i1, v1 in enumerate(nums1):
            if v1 in v1ToI2:
                continue
            for i2, v2 in enumerate(nums2):
                if v1 == v2:
                    v1ToI2[v2].append(i2)
        #print(v1ToI2)
        
        res = 0
        maxLength = [[0 for _ in range(len(nums2))] for _ in range(len(nums1))]
        for i1, v1 in enumerate(nums1):
            if v1 in v1ToI2:
                for i2 in v1ToI2[v1]:  #Only check the pair who matches in two arrays
                    maxLength[i1][i2] = 1
                    if i1 == 0: 
                        res = max(res, maxLength[i1][i2])
                        continue 
                    if 0 <= i2 - 1 < len(nums2) and nums2[i2 - 1] == nums1[i1 - 1]:
                        maxLength[i1][i2] = max(maxLength[i1][i2], maxLength[i1-1][i2-1] + 1)
                    res = max(res, maxLength[i1][i2])
        return res
    
    #=======================================

    # DP (2D map) [8%]
    def findLength1(self, nums1: List[int], nums2: List[int]) -> int:
        print("Method1: 2D map")
        
        v1ToI2 = collections.defaultdict(list)
        for i1, v1 in enumerate(nums1):
            if v1 in v1ToI2:
                continue
            for i2, v2 in enumerate(nums2):
                if v1 == v2:
                    v1ToI2[v2].append(i2)
        #print(v1ToI2)
        
        maxLength = defaultdict(lambda: defaultdict(int))
        for i1, v1 in enumerate(nums1):
            #print("i1:", i1)
            if i1 == 0:
                if v1 in v1ToI2:
                    for i2 in v1ToI2[v1]:
                        maxLength[i1][i2] = 1
            else:
                if v1 in v1ToI2:                
                    for i2 in v1ToI2[v1]:
                        #print("  i2:", i2)
                        maxLength[i1][i2] = 1
                        if 0 <= i2 - 1 < len(nums2) and nums2[i2 - 1] == nums1[i1 - 1]:
                            maxLength[i1][i2] = max(maxLength[i1][i2], maxLength[i1-1][i2-1] + 1)
                            
        res = 0
        for k, v in maxLength.items():
            for key, val in v.items():
                res = max(val, res)
            #print(k, ":", v)
        return res
    
    #=======================================
    
    #Incorrect, element might be more than 1 digit
    def findLength1(self, nums1: List[int], nums2: List[int]) -> int:
        string1 = "".join([str(x) for x in nums1])
        string2 = "".join([str(x) for x in nums2])
        
        for d in range(len(nums1), 0, -1):
            for s in range(len(nums1)):
                if s + d > len(nums1):
                    continue
                substring1 = string1[s:s+d]
                print(substring1)
                if substring1 in string2:
                    return d
        return 0 