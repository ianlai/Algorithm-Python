class Solution:
    
    # N-Heap [O(n + klogn), 53%]   
    # Note: n is one-dimension size; node number is n^2
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return -1
        
        heap = []
        n = len(matrix)
        
        heapq.heapify(heap)
        for i in range(n): 
            heapq.heappush(heap, (matrix[i][0], i, 0)) #base is first col
        
        indexList = [0] * n
        
        round = 0
        while heap and round < k:
            #print(heap)
            val, row, col = heapq.heappop(heap)
            round += 1 
            #print(val, row, col)
            col += 1 
            if col >= n:
                continue
            heapq.heappush(heap, (matrix[row][col], row, col))
        return val 