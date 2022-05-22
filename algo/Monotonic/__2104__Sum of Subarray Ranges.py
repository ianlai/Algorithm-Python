class Solution:
    
    # 2022/05/22
    # Monotonic Stack (PLE, NLE, PGE, NGE) [O(N): 68% / O(N): 12%]
    def subArrayRanges(self, arr: List[int]) -> int:
        print("Code2")
        PLE = [-1] * len(arr)       #left less than
        NLE = [len(arr)] * len(arr) #right less than  
        
        PGE = [-1] * len(arr)       #left greater than
        NGE = [len(arr)] * len(arr) #right greater than  
        
        #PLE and NLE 
        stack = []
        for i, v in enumerate(arr):
            while stack and arr[stack[-1]] >= v:
                idx = stack.pop()
                NLE[idx] = i
            PLE[i] = stack[-1] if stack else -1
            stack.append(i)
        
        #PGE and NGE
        stack = []
        for i, v in enumerate(arr):
            while stack and arr[stack[-1]] <= v:
                idx = stack.pop()
                NGE[idx] = i
            PGE[i] = stack[-1] if stack else -1
            stack.append(i)
    
        res = 0
        for i in range(len(arr)):
            res += arr[i] * (i - PGE[i]) * (NGE[i] - i) 
            res -= arr[i] * (i - PLE[i]) * (NLE[i] - i) 
        return res
    
        
    # 2022/05/21
    # Two layer loops [O(n2): 17% / O(1): 95%]
    def subArrayRanges1(self, nums: List[int]) -> int:
        print("Code1")
        rsumAll = 0
        for i in range(len(nums)):
            rmin, rmax = nums[i], nums[i]
            rsum = 0
            for j in range(i, len(nums)):
                rmin = min(rmin, nums[j])
                rmax = max(rmax, nums[j])
                rsum += rmax - rmin
            rsumAll += rsum
        return rsumAll
            