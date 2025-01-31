class Solution:
    
    # Matrix manipulation [O(n): 96%]
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """            
        n = len(matrix)
        for s in range(n//2):
            length = n - (s * 2)
            for d in range(length - 1):
                c1 = matrix[s][s + d]
                c2 = matrix[s + d][n - 1 - s]
                c3 = matrix[n - 1 - s][n - 1 - s - d]
                c4 = matrix[n - 1 - d - s][s]
                
                matrix[s][s + d] = c4
                matrix[s + d][n - 1 - s] = c1
                matrix[n - 1 - s][n - 1 - s - d] = c2
                matrix[n - 1 - d - s][s] = c3
                #print(c1, c2, c3, c4)
