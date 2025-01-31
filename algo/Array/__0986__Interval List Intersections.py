class Solution:
    
    # Two-Pointer [O(A+B): 90%]
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a, b = 0, 0        
        res = []
        while a < len(A) and b < len(B):
            newLeft = max(A[a][0], B[b][0])
            newRight = min(A[a][1], B[b][1])
            if newLeft <= newRight:
                res.append([newLeft, newRight])
                #print(res)
            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1 
        return res