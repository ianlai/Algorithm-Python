class Solution:
    
    # 2022/05/26 
    # Bit Manipulation [O(N): 74% / O(1): 49%]
    def hammingWeight(self, n: int) -> int:
        print("Code2")
        count = 0
        while n:
            count += 1 & n
            n = n >> 1
        return count 
        
    # 2022/05/26 
    # String [O(N): 91% / O(N): 7%]
    def hammingWeight1(self, n: int) -> int:
        print("Code1")
        return bin(n)[2:].count('1')
    