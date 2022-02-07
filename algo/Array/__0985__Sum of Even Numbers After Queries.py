class Solution:
    
    # Main even sum [O(n): 56%]
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        for v in nums:
            if v % 2 == 0:
                evenSum += v
                
        res = []
        for v, i in queries:
            oldValue = nums[i]
            newValue = nums[i] + v
            nums[i] += v
            if oldValue % 2 != 0:
                if newValue % 2 == 0:
                    evenSum += newValue
                    res.append(evenSum)
                else:
                    res.append(evenSum)
            else:
                evenSum -= oldValue
                if newValue % 2 == 0:
                    evenSum += newValue
                    res.append(evenSum)
                else:
                    res.append(evenSum)
        return res