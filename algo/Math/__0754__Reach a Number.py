class Solution:
    
    # 2022/03/01
    # Math [O(target): 38%]
    # 不好想，總之一直往前跳，所以是等差級數，直到超越。
    # 超越之後的差如果是偶數，代表前面在i步可以利用往左邊跳達到-2i的效果，可以做出任意偶數，因此答案就是目前步。
    # 超越之後的差如果是奇數，代表需要再繼續往前直到變成偶數，再利用上述方法回到目標，因此答案就是抵達第一個偶數步。
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        for i in range(1, target+3):
            target -= i 
            if target == 0:
                return i
            if target < 0:
                if target % 2 == 0:
                    return i

s = Solution()
print("5 -> ", s.reachNumber(5))