class Solution:
    
    # Binary Search; Transform matrix to list [O(n), 57%]
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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