# https://leetcode.com/problems/decode-string/
# 
# Test: 
# "a3[b2[cd]e2[f]]g12[h]ijk"
# "100[leetcode]"

class Solution:
    
    # Recursion [9%]
    def decodeString(self, s: str) -> str:
        #print("----- Recursive -----")
        #print("  s:", s)
        
        numList = []
        numIdxList = []
        quoteList = []
        
        left, right = 0, 0
        leftIdx, rightIdx, numIdx = -1, -1, -1 #left quote, right quote, first digit
        
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                if leftIdx == -1 and numIdx == -1:
                    numIdx = i
            elif c == "[":
                left += 1
                if leftIdx == -1:
                    leftIdx = i
            elif c == "]":
                right += 1                    
                if left == right:
                    rightIdx = i
                    numList.append(int("".join(s[numIdx:leftIdx])))
                    numIdxList.append(numIdx)
                    quoteList.append((leftIdx, rightIdx))
                    
                    #reset 
                    left, right = 0, 0
                    leftIdx, rightIdx = -1, -1
                    numIdx = -1
                    
        res = []
        start, end = -1, 0 
        
        # First part 
        if len(numList) == 0:
            res.append(s)
        
        # Middle parts
        for i in range(len(numList)): 
            end = quoteList[i][0]                
            res.append(s[start+1:numIdxList[i]])
            res.append(numList[i] * self.decodeString(s[end+1:quoteList[i][1]]))
            start = quoteList[i][1]
        
        # Last part 
        if quoteList and quoteList[-1][1] != len(s) - 1:
            res.append(s[quoteList[-1][1]+1:])
        
        return "".join(res)
    
    # =========================================
    
    # [Correct]
    # Two stacks, accumulated to curString all the time [18%]
    def decodeString1(self, s: str) -> str:
        print("2 stacks")
        stack1 = [] #number
        stack2 = [] #alphabet
        
        num = []
        alpha = ""
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num.append(c)
            elif c.isalpha():
                alpha += c
            elif c == "[":
                stack1.append(int("".join(num)))
                stack2.append(alpha)
                alpha = ""
                num = [] 
            elif c == "]":
                curNum = stack1.pop()
                last = stack2.pop()
                alpha = last + curNum * alpha
            print(c, num, stack1, alpha, stack2)
        return alpha

    # ================================================
    # [Incorrect]
    # Two stacks, clear curString all the time 
    def decodeString2(self, s: str) -> str:
        
        stack1 = [] #number
        stack2 = [] #alphabet
        
        idx = 0
        num = []
        alpha = []
        while idx < len(s):
            c = s[idx]
            if c.isdigit():
                num.append(c)
                if alpha:
                    curAlpha = "".join(alpha)
                    stack2.append(curAlpha)
                    alpha = []
            elif c.isalpha():
                alpha.append(c)
            elif c == "[":
                stack1.append(int("".join(num)))
                num = []
            elif c == "]":
                curAlpha = "".join(alpha)
                if curAlpha:
                    stack2.append(curAlpha)
                lastAlpha = ""
                if stack2:
                    curAlpha = stack2.pop()
                if stack2:
                    lastAlpha = stack2.pop()
                curNum = stack1.pop()
                #print("lastAlpha:", lastAlpha, "curAlpha:", curAlpha)
                stack2.append(lastAlpha + curNum * curAlpha)
                alpha = []
            print(c, num, stack1, alpha, stack2)
            idx += 1

        if alpha:   
            stack2.append("".join(alpha))
        return "".join(stack2)
