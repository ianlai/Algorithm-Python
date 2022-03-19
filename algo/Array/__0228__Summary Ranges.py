class Solution:
    
    # 2022/03/19
    # Traverse the array [O(n): 87%]
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ranges = [[nums[0], nums[0]]]
        for i, v in enumerate(nums):
            if i == 0:
                continue
            if v == ranges[-1][1] + 1:
                ranges[-1][1] = v
            else:
                ranges.append([v, v])
        res = []
        for start, end in ranges:
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(end))
        return res
    
    # Follow-up:
    # (1) Duplicated 
    # (2) Unsorted 