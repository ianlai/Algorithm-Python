class Solution:
    
    # Prefix Sum (from front and tail) [O(n): 15%]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        frontProducts = []
        tailProducts = []
        
        product = 1
        for num in nums:
            product *= num
            frontProducts.append(product)
        product = 1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i] 
            tailProducts.append(product)
        
        res = []
        for i in range(len(nums)):
            product = 1
            if i > 0:
                product *= frontProducts[i-1]
            if i < len(nums)-1:
                product *= tailProducts[len(nums) - i - 1 - 1]
            res.append(product)
        return res 