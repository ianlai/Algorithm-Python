class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        count1 = collections.defaultdict(int)
        count2 = collections.defaultdict(int)
        for i in range(len(nums1)):
            count1[nums1[i]] += 1
        
        for i in range(len(nums2)):
            count2[nums2[i]] += 1
        
        results = []
        for num, count1 in count1.items():
            count = min(count1, count2[num])
            for j in range(count):
                results.append(num)
        return results