class Solution:
    
    # Two-pointer [O(m+n): 45%]
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return 
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return 
        
        for i in range(m-1, -1, -1):
            nums1[i+n] = nums1[i]
        
        p0, p1, p2 = 0, n, 0 
        while p1 < m + n or p2 < n:
            if p2 >= n:
                nums1[p0] = nums1[p1]
                p1 += 1
            elif p1 >= m + n: 
                nums1[p0] = nums2[p2]
                p2 += 1
            else:
                if nums1[p1] < nums2[p2]:
                    nums1[p0] = nums1[p1]
                    p1 += 1
                else:
                    nums1[p0] = nums2[p2]
                    p2 += 1
            p0 += 1 
        return 
                