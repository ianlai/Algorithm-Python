#https://leetcode.com/problems/trapping-rain-water/
 
class Solution:
    
    # Accumulated array from left and right [O(n): 49%]
    def trap(self, height: List[int]) -> int:
        print("Method-2: Accumulated array")
        res = 0 
        left, right = [0] * len(height), [0] * len(height) 
        leftMax, rightMax = 0, 0
        for i, h in enumerate(height):
            leftMax = max(leftMax, h)
            left[i] = leftMax
            
        for i, h in enumerate(height[::-1]):
            rightMax = max(rightMax, h)
            right[i] = rightMax
        right = right[::-1]
        
        for i, h in enumerate(height):
            minH = min(left[i], right[i]) 
            res += minH - h if minH > h else 0
        return res
    
    # =====================================================
    
    # Brute force: Find two walls of each point [O(n2): 5%]
    def trap1(self, height: List[int]) -> int:
        print("Method-1: Brute force")
        res = 0
        for i, h in enumerate(height):
            if i == 0 or i == len(height) - 1:
                continue
            minH = min(max(height[:i]), max(height[i+1:]))
            res += minH - h if minH > h else 0
        return res
