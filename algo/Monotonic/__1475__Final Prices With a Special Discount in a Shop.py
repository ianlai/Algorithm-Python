class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = list(prices)
        for i, v in enumerate(prices):
            while stack and prices[stack[-1]] >= v:
                res[stack[-1]] -= v
                stack.pop()
            stack.append(i)
        return res