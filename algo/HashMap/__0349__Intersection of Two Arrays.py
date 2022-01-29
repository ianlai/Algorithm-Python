class Solution:
    
    # Two set [O(m+n): 94%]
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numSet = set()
        for v in nums1:
            numSet.add(v)
        res = set()
        for v in nums2:
            if v in numSet:
                res.add(v)
        return list(res)