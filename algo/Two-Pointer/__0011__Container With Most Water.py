class Solution:
    
    # 2022/04/05
    # Two-Pointer 
    def maxArea(self, height: List[int]) -> int:
        print("Code-4")
        maxArea = 0 
        p1, p2 = 0, len(height) - 1
        while p1 < p2:
            area = (p2 - p1) * min(height[p1], height[p2])
            maxArea = max(maxArea, area)
            if height[p1] < height[p2]:
                p1 += 1
            elif height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
                p2 -= 1
        return maxArea
        
    # ===========================================

    # 2022/01/25 
    # Two-Pointer 
    def maxArea3(self, height: List[int]) -> int:
        print("Code-3")
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            res = max(res, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res
    
    # ===========================================

    # 2021/10/15
    # Two-pointer [O(n): 73%]
    def maxArea2(self, height: List[int]) -> int:
        print("Code-2")
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            if height[l] < height[r]:
                area = max(area, height[l] * (r - l))
                l += 1
            elif height[l] > height[r]:
                area = max(area, height[r] * (r - l))  
                r -= 1
            else: 
                area = max(area, height[r] * (r - l)) 
                l += 1
                r -= 1
        return area

    # ===========================================
    
    # 2021/05/21
    # Two-pointer [O(n), 78%]
    def maxArea1(self, height: List[int]) -> int:
        print("Code-1")
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        maxArea = 0
        while left < right:
            #print(left, right)
            if height[left] == height[right]:
                area = (right - left) * height[left]
                maxArea = max(maxArea, area)
                left += 1
                right -= 1
                #break #stop searching because no larger area with a smaller interval
            elif height[left] < height[right]:
                area = (right - left) * height[left]
                maxArea = max(maxArea, area)
                left += 1
            else:
                area = (right - left) * height[right]
                maxArea = max(maxArea, area)
                right -= 1
        return maxArea