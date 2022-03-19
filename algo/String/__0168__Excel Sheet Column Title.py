class Solution:
    
    # Not easy to think 
    # Excel column is not a 26-ary counting system because it starts from 1 [O(n): 94%]
    def convertToTitle(self, columnNumber: int) -> str:        
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        columnTitle = ""
        while columnNumber != 0:
            columnNumber -= 1  #the key step
            columnTitle += alphabets[columnNumber % 26] 
            columnNumber //= 26
        return columnTitle[::-1]