class Solution:
    
    # Two-pointer [O(n), 78%]
    def maxArea(self, height: List[int]) -> int:
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