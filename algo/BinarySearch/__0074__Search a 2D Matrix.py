class Solution:
    # 2022/03/30 
    # Binary Search with matrix [Time: O(logmn): 87% / Space: O(1): 8%]
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print("Code2")
        def convert(idx):
            i, j = idx // n, idx % n
            return i, j
        
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n 
        while start < end:
            mid = start + (end - start) // 2
            midi, midj = convert(mid)
            if matrix[midi][midj] == target:
                return True
            elif matrix[midi][midj] < target:
                start = mid + 1
            else:
                end = mid 
        return False
         
        
    # 2021/05/11
    # Convert to array then binary Search [Time: O(logmn): 59% / Space: O(mn): 8%]
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print("Code1")
        if not matrix or not matrix[0]:
            return False
        
        arr = []
        for row in matrix:
            arr.extend(row)
            
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] == target:
                return True
            if arr[mid] < target:
                start = mid
            if arr[mid] > target:
                end = mid 
        if arr[start] == target or arr[end] == target:
            return True
        return False