class Solution:
    #2022/01/01 (mock interview)
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2ToIdx = collections.defaultdict(list)
        for i, v in enumerate(nums2):
            nums2ToIdx[v].append(i)
        
        res = []
        for v in nums1:
            idx = nums2ToIdx[v].pop()
            res.append(idx)
        return res
            