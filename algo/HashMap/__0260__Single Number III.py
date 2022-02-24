class Solution:
    
    # Use hashmap [time:O(n):62%, space:O(n):7% ]
    def singleNumber(self, nums: List[int]) -> List[int]:
        res_set = set()
        num_set = set()
        for num in nums:
            if num in num_set:
                res_set.remove(num)
            else:
                num_set.add(num)
                res_set.add(num)
        return list(res_set)
                