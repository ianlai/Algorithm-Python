class Solution:
    
    # Time:  O(R + 100 RlogR + P* 100*logR) 
    # Space: O(R)
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        
        maxH = 101 
        hToL = [[] for _ in range(maxH)]
        
        
        for l, h in rectangles:
            hToL[h].append(l)
        
        for h in range(1, maxH):
            hToL[h].sort()
        
        res = []
        for px, py in points:
            count = 0
            
            # Only search the height (y) which equals to or greater than give py 
            for h in range(py, maxH):
                if len(hToL[h]) == 0:
                    continue
                    
                # Find the first index of length (x) which equals to or greater than give px in a sorted array, thus we can use binary search
                idx = bisect.bisect_left(hToL[h], px) 
                count += len(hToL[h]) - idx
            res.append(count)
        return res