class Solution:
    
    # A bit like two pointer [O(n), 78%]
    def maximumSwap(self, num: int) -> int:
        if num <= 0:
            return num 
        numStr = [int(x) for x in str(num)]
        
        if len(numStr) == 1:
            return num
        
        smallIdx = 0
        smallNum = numStr[0]
        for i in range(len(numStr)):
            smallIdx = i
            smallNum = numStr[i]
            largeIdx = i
            largeNum = numStr[i]
            print(i, numStr[i])
            if len(numStr[i+1:]) != 0:
                largeNum = max(numStr[i+1:])
#                 fromSmall = numStr[i+1:]
#                 tmpIdx = fromSmall[::-1].index(largeNum) 
#                 largeIdx = len(fromSmall) - 1 - tmpIdx + i + 1
                for j in range(len(numStr) - 1, i, -1):
                    if numStr[j] > numStr[i] and numStr[j] == largeNum:
                        largeNum = numStr[j]
                        largeIdx = j 
                        numStr[smallIdx], numStr[largeIdx] = numStr[largeIdx], numStr[smallIdx] 
                        print("small idx:", smallIdx, smallNum)
                        print("large idx:", largeIdx, largeNum)
                        resultNum = int("".join([str(x) for x in numStr]))
                        return resultNum
        return num
            