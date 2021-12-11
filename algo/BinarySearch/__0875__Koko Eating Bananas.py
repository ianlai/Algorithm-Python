class Solution:
    
    # Binary Search [O(logn): 53%]
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBanana = max(piles)
        start, end = 1, maxBanana
        while start < end:
            speed = start + (end - start) // 2 
            if self.isValidSpeed(speed, piles, h):
                end = speed 
            else:
                start = speed + 1
        return start

    def isValidSpeed(self, speed, piles, h):
        time = 0
        for pile in piles:
            time += math.ceil(pile / speed)
        ans = time <= h
        return ans