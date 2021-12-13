class Solution:
    
    # Binary Search: row -> coin to test [O(logn): 71%]
    def arrangeCoins(self, n: int) -> int:
        print("Code2: Binary Search")
        start, end = 1, n   #row 
        while start < end: 
            mid = start + (end - start) // 2
            midCoin = (mid * (mid + 1)) / 2
            if midCoin == n:
                return mid
            elif midCoin < n:
                start = mid + 1 
            else:
                end = mid
        return start - 1 if start != 1 else 1
         
    # =============================================
    
    # Math: coin->row [O(1): 86%]
    def arrangeCoins1(self, n: int) -> int:
        print("Code1: Math")
        ans = (int)((8*n + 1) ** 0.5 - 1) // 2
        return ans