class Solution:
    
    # 2022/05/14
    # Iterate substrings [O(N): 100% / O(1): 75%] 
    def divisorSubstrings(self, num: int, k: int) -> int:
        strNum = str(num)
        count = 0
        for i in range(k, len(strNum)+1):
            sub = int(strNum[i-k:i])
            if sub == 0:
                continue
            if num % sub == 0:
                count += 1
        return count
        