class Solution:
    
    # Customized sorting [O(nlogn):54%]
    def largestNumber(self, nums: List[int]) -> str:
        numsString = [str(x) for x in nums]
        def comp(x, y):
            if x + y < y + x:
                return 1
            return -1
        numsString.sort(key = cmp_to_key(comp))
        
        res = ""
        for num in numsString:
            if res == "0" and num == "0":
                return res
            res += num
        return res