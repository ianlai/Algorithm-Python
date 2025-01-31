class Solution:
    
    #Sliding-window [O(n): 77%]
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0
        
        res = 0
        left = 0
        brackets = collections.defaultdict(int)
        for right, r in enumerate(fruits):
            brackets[r] += 1
            while len(brackets) > 2 :
                l = fruits[left]
                brackets[l] -= 1
                if brackets[l] == 0:
                    del brackets[l]
                left += 1
            res = max(res, right - left + 1)
        return res