class Solution(object):
    
    
    # 2021/12/13
    # Binary Search [O(nlogn): 93%]
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        def find(arr, target): 
            start, end = 0, len(arr)
            while start < end:
                mid = start + (end - start) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    end = mid
                else:
                    start = mid + 1 
            return False 
        
        for v in mat[0]:
            isFound = True 
            for searchRow in mat[1:]:
                if not find(searchRow, v):
                    isFound = False
                    break
            if isFound:
                return v
        return -1 