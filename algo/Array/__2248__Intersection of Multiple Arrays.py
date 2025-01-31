class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        main = set(nums[0])
        
        for i in range(1, len(nums)):
            s = set(nums[i])
            
            for m in list(main):
                if m not in s:
                    main.remove(m)
        return sorted(list(main))