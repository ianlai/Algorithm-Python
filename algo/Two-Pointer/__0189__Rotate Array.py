class Solution:
    
    # 3-step rotation [O(n), 38%]
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 
        
        n = len(nums) 
        while k > n:
            k -= n
        
        print(id(nums))
        self.swap(nums, 0, len(nums) - 1) 
        self.swap(nums, 0, k - 1)
        self.swap(nums, k, len(nums) - 1)
        print(id(nums))
        
        #=== This is incorrect because this will create new nums (id changed)
        #print(id(nums))
        #nums = nums[::-1]
        #nums = nums[:k][::-1] + nums[k:][::-1]
        #print(id(nums))
        
    def swap(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1