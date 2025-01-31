class Solution:
    
    # 2022/01/26
    # DP [O(n): 36%]
    def maxProduct(self, nums: List[int]) -> int:
        print("Code3")
        if not nums:
            return 0
        dp = [[0] * 2 for _ in range(len(nums))]
        
        if nums[0] >= 0:
            dp[0][0] = nums[0]
        if nums[0] < 0:
            dp[0][1] = nums[0]
            
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp[i][0] = max(nums[i], nums[i] * dp[i-1][0])
                dp[i][1] = nums[i] * dp[i-1][1]    
            elif nums[i] < 0: 
                dp[i][0] = nums[i] * dp[i-1][1]
                dp[i][1] = min(nums[i], nums[i] * dp[i-1][0])
            else:
                dp[i][0] = 0
                dp[i][1] = 0
                
            res = max(res, dp[i][0], dp[i][1])
        #print(dp)
        return res
    
    # ======================================

    # 2022/01/26
    # DP [O(n): 36%]
    def maxProduct2(self, nums: List[int]) -> int:
        print("Code2")
        if not nums:
            return 0
        dp = [[0] * 2 for _ in range(len(nums))]
        
        if nums[0] >= 0:
            dp[0][0] = nums[0]
        if nums[0] < 0:
            dp[0][1] = nums[0]
            
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                if dp[i-1][0] != 0:
                    dp[i][0] = max(nums[i], nums[i] * dp[i-1][0])
                else:
                    dp[i][0] = nums[i]
                    
                if dp[i-1][1] != 0:
                    dp[i][1] = nums[i] * dp[i-1][1]
                else:
                    dp[i][1] = 0       
                    
            elif nums[i] < 0: 
                if dp[i-1][1] != 0:
                    dp[i][0] = nums[i] * dp[i-1][1]
                else:
                    dp[i][0] = 0
                    
                if dp[i-1][0] != 0:
                    dp[i][1] = min(nums[i], nums[i] * dp[i-1][0])
                else:
                    dp[i][1] = nums[i]
            else:
                dp[i][0] = 0
                dp[i][1] = 0
                
            res = max(res, dp[i][0], dp[i][1])
        #print(dp)
        return res
        
    # ======================================
        
    # 2021/06/07
    # Two-pointer 同向雙指針 [O(n), 29%]
    def maxProduct1(self, nums: List[int]) -> int:
        print("Code1")
        if not nums:
            return 0
        
        left, right = 0, 0
        maxProduct, product = nums[0], 1 
        isProductGen = False
        #print(nums)
        while right < len(nums) and left <= right:
            #print(left, right, end = " ")
            if nums[right] == 0:
                #print(">>", left, right, end = " ")
                while left < right:
                    product /= nums[left]
                    if left + 1 < right:
                        maxProduct = max(maxProduct, product)
                    maxProduct = max(maxProduct, nums[right])
                    left += 1 
                    
                #reset
                product = 1
                right += 1
                left  = right
                isProductGen = False
            else:
                product *= nums[right] 
                isProductGen = True
                
                #if left + 1 < right:
                maxProduct = max(maxProduct, product)
                maxProduct = max(maxProduct, nums[right])
                #maxProduct = max(maxProduct, 0)
                right += 1 
            #print(product, end = "\n")
        
        # -----------------------
        # Last left scan 
        right -= 1
        #print("end:", left, right)
        while left < right:
            #print(left, right, end = " ")
            product /= nums[left]
            if left + 1 < right:
                maxProduct = max(maxProduct, product)
            maxProduct = max(maxProduct, nums[right])
            left += 1 
            #print(product, end = "\n")
            
        return int(maxProduct)
        
            
