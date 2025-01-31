MODULE = 10 ** 9 + 7

class Solution:
    
    # 2022/07/02
    # Sorting then find max w and h to multiply together [O(MlogM + NlogN): 86% / O(M + N): 11%]
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        hIntervals, vIntervals = [], []
        for i, v in enumerate(horizontalCuts):
            if not hIntervals:
                hIntervals.append(v)
            else:
                hIntervals.append(v - horizontalCuts[i-1])
        for i, v in enumerate(verticalCuts):
            if not vIntervals:
                vIntervals.append(v)
            else:
                vIntervals.append(v - verticalCuts[i-1])
        
        return max(hIntervals) * max(vIntervals) % MODULE