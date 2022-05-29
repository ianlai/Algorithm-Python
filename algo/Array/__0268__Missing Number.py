class Solution:
    
    # 2022/05/28
    # N-size Array (like hashset) [O(N): 98% / O(N): 77%]
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        arr = [0] * n
        for v in nums:
            arr[v] = 1
            
        for i in range(len(arr)):
            if arr[i] == 0 :
                return i        