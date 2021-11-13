class Solution:
    
    # DP [11%]
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
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
    
    # =======================================
    
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