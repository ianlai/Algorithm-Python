class Solution:
    # 2022/02/07
    # Binary Search [O(logn): 23%]
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        print("Code2")
        def canFinish(speed, h):
            time = 0
            for pile in piles:
                time += math.ceil(pile / speed)
            if time > h:
                return False
            return True
            
        start, end = 1, max(piles)  #搜索範圍[1:max-1] 但結果是區間，所以end有包到O就可以
        while start < end:
            mid = start + (end - start) // 2
            if canFinish(mid, h):  # > t
                end = mid 
            else:  # <= t
                start = mid + 1
        return start 
        
    # ========================================   
    # 2021/12/11 
    # Binary Search [O(logn): 53%]
    def minEatingSpeed1(self, piles: List[int], h: int) -> int:
        print("Code1")
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