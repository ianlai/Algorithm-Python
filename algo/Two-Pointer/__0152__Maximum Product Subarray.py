class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        left, right = 0, 0
        maxProduct, product = nums[0], 1
        print(nums)
        while right < len(nums) and left <= right:
            print(left, right, end = " ")
            if nums[right] == 0:
                while product < 0 and left < right:
                    product /= nums[left]
                    if product > 1:
                        maxProduct = max(maxProduct, product)
                    maxProduct = max(maxProduct, nums[right])
                    left += 1 
                #reset
                product = 1
                right += 1
                left  = right
            else:
                product *= nums[right] 
                if product > 1:
                    maxProduct = max(maxProduct, product)
                maxProduct = max(maxProduct, nums[right])
                #maxProduct = max(maxProduct, 0)
                right += 1 
            print(product, end = "\n")
        return maxProduct 
        
            
