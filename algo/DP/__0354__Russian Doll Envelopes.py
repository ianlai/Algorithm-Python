class Solution:
    
#     def maxEnvelopes(self, arr: List[List[int]]) -> int:
#         # sort increasing in first dimension and decreasing on second
#         arr.sort(key=lambda x: (x[0], -x[1]))

#         def lis(nums):
#             dp = []
#             for i in range(len(nums)):
#                 idx = bisect_left(dp, nums[i])
#                 if idx == len(dp):
#                     dp.append(nums[i])
#                 else:
#                     dp[idx] = nums[i]
#             return len(dp)
#         # extract the second dimension and run the LIS
#         return lis([i[1] for i in arr])
    
    # 2022/05/25
    # LIS Binary Search O(nlogn) / O(n)
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        print("LIS")
        e.sort(key = lambda x: (x[0], -x[1]))
        def lis(arr):
            seq = []
            for i in range(len(arr)):
                idx = bisect.bisect_left(seq, arr[i])
                if idx == len(seq):
                    seq.append(arr[i])
                else:
                    seq[idx] = arr[i]
            return len(seq)
        
        return lis([v[1] for v in e]) 
    
    
    # Sorting + DP [TLE]
    def maxEnvelopes2(self, e: List[List[int]]) -> int:
        e.sort(key = lambda x: (x[0], x[1]))
        #dp = [[0] * len(e) for _ in range(len(e))]
        dp = [1] * len(e)
        for i in range(len(e)):
            for j in range(i):
                if e[j][0] < e[i][0] and e[j][1] < e[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) 
            
        
    # Sorting + Greedy [Incorrect]
    # [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
    def maxEnvelopes1(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], x[1]))
        totalCount = 0
        for i in range(len(envelopes)):
            count = 1
            lastW, lastH = envelopes[i][0], envelopes[i][1]
            for j in range(i+1, len(envelopes)):
                if envelopes[j][0] > lastW and envelopes[j][1] > lastH:
                    lastW = envelopes[j][0]
                    lastH = envelopes[j][1]
                    count += 1
            totalCount = max(count, totalCount)
        return totalCount 
            