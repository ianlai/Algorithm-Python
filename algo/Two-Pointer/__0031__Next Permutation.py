class Solution:
    
    # Pointer approach [O(n): 92%]
    # (1) Find the 1st decreasing one from tail as target1
    # (2) Find the smallest element which larger than target1 in arr[target1Idx+1:] as target2
    # (3) Swap target1 and target2
    # (4) Reverse arr[target1Idx+1:]
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseFromIdx(nums, idx):
            for i in range(idx, len(nums)):
                j = len(nums) - 1 - i + idx
                if i >= j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
        
        invert = nums[::-1]
        target, targetIdx = -1, -1
        n = len(nums)
        
        # Find target1 
        for i in range(1, len(invert)):
            if invert[i-1] > invert[i]:
                target, targetIdx = invert[i], i
                break
                
        # special case
        if target == -1:
            reverseFromIdx(nums, 0)
            return 
        
        # Find target2 
        for i in range(len(invert[:targetIdx])):
            if invert[i] > target:
                target2 = invert[i] 
                target2Idx = i
                break
        
        t1, t2 = n-1-targetIdx, n-1-target2Idx 
        print("r1:", targetIdx," r2:", target2Idx)  #reverse index 
        print("t1:", t1, " t2:", t2)                #index
        nums[t1], nums[t2] =  nums[t2], nums[t1] 
        reverseFromIdx(nums, t1+1)