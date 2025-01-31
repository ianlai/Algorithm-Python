class Solution:
    
    # Monotonic stack (store index) [O(n): 50%]
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i, v in enumerate(heights):
            while stack and heights[stack[-1]] <= v:
                stack.pop()
            stack.append(i)
        return stack