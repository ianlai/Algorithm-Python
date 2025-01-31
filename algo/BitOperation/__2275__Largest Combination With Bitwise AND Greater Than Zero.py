class Solution:
    
    # 2022/05/15
    # Bit count [O(maxbit * N): 83% / O(maxbit * N): 66%]
    def largestCombination(self, candidates: List[int]) -> int:
        
        bc = []  #binary combination 
        length = 0
        for c in candidates:
            bc.append(bin(c)[2:][::-1])
            length = max(length, len(bc[-1]))
                         
        total = 0
        for i in range(length+1):
            count = 0
            for b in bc:
                if i >= len(b):
                    continue
                if b[i] == '1':
                    count += 1
            total = max(count, total)
        return total