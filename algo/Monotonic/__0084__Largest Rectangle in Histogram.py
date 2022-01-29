class Solution:
    
    # Monotonic stack [O(n: 73%)]
    # =============================
    def largestRectangleArea(self, heights: List[int]) -> int:
        print("Code2 - Monotonic Stack")
        mstack = [-1]
        maxArea = 0
        
        #ascending monotonic stack
        #calculate the area when poping out
        #right wall is the new number 
        for i, v in enumerate(heights):
            popIdx = 0
            while mstack[-1] != -1  and heights[mstack[-1]] >= v:
                popIdx = mstack.pop()
                area = (i - mstack[-1] - 1) * heights[popIdx]
                maxArea = max(maxArea, area)
                #print("(1) ", i, heights[popIdx], "->", area)
            mstack.append(i)
        
        print(mstack)
        #remaining indices
        #they haven't been popped out because no smaller number came in 
        #right wall is the len(arr)
        while mstack[-1] != -1:
            popIdx = mstack.pop()
            popHeight = heights[popIdx]
            leftIdx = mstack[-1]
            area = (len(heights) - leftIdx - 1) * popHeight
            maxArea = max(maxArea, area)    
            #print("(2) ", rightIdx, "->", area)
        return maxArea
    
    # =============================
    # Divide and conquer [O(nlogn: TLE)]
    def largestRectangleArea1(self, heights: List[int]) -> int:
        print("Code1 - D&C")
        if len(heights) == 0:
            return 0
        minVal = min(heights)
        minIdx = heights.index(minVal)
        left  = self.largestRectangleArea(heights[:minIdx])
        right = self.largestRectangleArea(heights[minIdx+1:])
        cross = minVal * len(heights)
        return max(left, right, cross)