MODULE = 10 ** 9 + 7
class Solution:
    
    # 2022/05/22
    # Monotonic Stack (PLE and NLE) [O(N): 52% / O(N): 67%]
    def sumSubarrayMins(self, arr: List[int]) -> int:
        print("Code2")
        leftLess  = [-1] * len(arr) #left less than
        rightLess = [len(arr)] * len(arr) #right less than  (increasing)
        
        #Left less than 
        stack = []
        for i, v in enumerate(arr):
            while stack and arr[stack[-1]] >= v:
                idx = stack.pop()
                #if leftLess[i] == -1:
            leftLess[i] = stack[-1] if stack else -1
            stack.append(i)
        #print(leftLess)
        
        #Right less than 
        stack = []
        for i, v in enumerate(arr):
            while stack and arr[stack[-1]] >= v:
                idx = stack.pop()
                rightLess[idx] = i
            stack.append(i)
        #print(rightLess)
    
        res = 0
        for i in range(len(arr)):
            leftDistance  = i - leftLess[i] 
            rightDistance = rightLess[i] - i 
            #print(i, ":", arr[i] , leftDistance , rightDistance)
            res += arr[i] * leftDistance * rightDistance % MODULE
        return res % MODULE
    
    # ======================================
    # 2022/05/22
    # Two loops [O(N2): TLE / O(1)]
    def sumSubarrayMins1(self, arr: List[int]) -> int:
        print("Code1")
        totalSum = 0
        for i in range(len(arr)):
            curSum = 0
            minVal = arr[i]
            for j in range(i, len(arr)):
                minVal = min(minVal, arr[j])
                curSum += minVal 
            totalSum += curSum % MODULE
        return totalSum % MODULE