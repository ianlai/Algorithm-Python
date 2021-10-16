class Solution:
    
    # Two-pointer [O(n): 73%]
    def maxArea(self, height: List[int]) -> int:
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