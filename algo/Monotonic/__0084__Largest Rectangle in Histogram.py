class Solution:
    
    # Monotonic stack [O(n: 5%)]
    # =============================
    def largestRectangleArea(self, heights: List[int]) -> int:
        print("Code2 - Monotonic Stack")
        mstack = [-1]
        maxArea = 0
        for i, v in enumerate(heights):
            curIdx = 0
            while mstack[-1] != -1  and heights[mstack[-1]] >= v:
                curIdx = mstack.pop()
                area = (i - mstack[-1] - 1) * heights[curIdx]
                maxArea = max(maxArea, area)
                print("(1) ", curIdx - 1, i, heights[curIdx], "->", maxArea)
            mstack.append(i)
        
        #print(mstack)
        while mstack[-1] != -1:
            rightIdx = mstack.pop()
            rightHeight = heights[rightIdx]
            leftIdx = mstack[-1]
            area = (len(heights) - leftIdx - 1) * rightHeight
            maxArea = max(maxArea, area)    
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