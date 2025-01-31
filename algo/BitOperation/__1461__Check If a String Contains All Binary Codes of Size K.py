class Solution:
    
    # 2022/05/31
    # Rolling calculate [O(N): 16% / O(2^K): 86%]
    def hasAllCodes(self, s: str, k: int) -> bool:
        print("Code2")
        power = 2 ** k
        arr = [0] * (2 ** k)
        for i in range(k-1, len(s)):
            if i == k-1:
                b = int(s[i-k+1:i+1], 2)
            else:
                b = (b << 1 & power - 1) | int(s[i])   
            arr[b] = 1
        return all(arr)    
    
    # 2022/05/31
    # Linear scan [O(NK): 16% / O(2^K): 86%]
    def hasAllCodes1(self, s: str, k: int) -> bool:
        print("Code1")
        arr = [0] * (2 ** k)
        for i in range(k-1, len(s)):
            b = int(s[i-k+1:i+1], 2)
            arr[b] = 1
        return all(arr)