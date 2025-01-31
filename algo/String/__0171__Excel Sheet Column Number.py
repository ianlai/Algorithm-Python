class Solution:
    
    # 2022/03/19
    # Calculate from LSB [O(s): 74%]
    def titleToNumber(self, columnTitle: str) -> int:
        column = 0
        bitNum = 0
        for i in range(len(columnTitle)-1, -1, -1):
            num = ord(columnTitle[i]) - ord("A") + 1 
            column += num * 26 ** bitNum
            bitNum += 1
        return column