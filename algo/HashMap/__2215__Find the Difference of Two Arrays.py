class Solution:
    
    # 2022/03/27
    # HashSet [O(m+n):83%]
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans1, ans2 = set(), set()
        for v in nums1:
            if v not in set2:
                ans1.add(v)
        for v in nums2:
            if v not in set1:
                ans2.add(v)
        return [ans1, ans2]