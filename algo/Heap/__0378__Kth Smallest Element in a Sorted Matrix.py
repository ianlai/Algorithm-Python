class Solution:
    
    # Sorting [O(nlogn): 26%]
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        print("Sorting")
        if not matrix:
            return None 
        arr = []
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                arr.append(matrix[i][j])
        arr.sort()
        return arr[k-1]
    
    # N-Heap [O(n + klogn), 53%]   
    # Note: n is one-dimension size; node number is n^2
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        print("Heap")
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
    
        
    # Incorrect
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return None 
        
        n = len(matrix)
        groups = [[] for _ in range(n * 2 - 1)]
        
        for i in range(n):
            for j in range(n):
                idx = i + j
                groups[idx].append(matrix[i][j])
        
        print(groups)
        k -= 1
        for group in groups:
            if len(group) <= k:
                k -= len(group)
                print("skip", group)
                continue
            else:
                group.sort()
                print("use", group)
                print("k=", k)
                return group[k]
        
                