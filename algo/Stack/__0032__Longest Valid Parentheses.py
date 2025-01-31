class Solution:
    
    # 2022/05/24
    # Stack [O(N): 37% / O(N): 25%]
    def longestValidParentheses(self, s: str) -> int:
        print("Code2")
        res = 0
        stack = [-1]
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res 
                

    def longestValidParentheses2(self, s: str) -> int:
        lPresum = [0] * len(s)
        rPresum = [0] * len(s)
        for i, ch in enumerate(s):
            lPresum[i] = lPresum[i-1]
            rPresum[i] = rPresum[i-1]
            if ch == "(":
                if i == 1:
                    lPresum[i] = 1
                else:
                    lPresum[i] += 1
            if ch == ")":
                if i == 1:
                    rPresum[i] = 1
                else:
                    rPresum[i] += 1
    '''
    ()(() 
    '''
    # Sliding window [Incorrect]
    def longestValidParentheses1(self, s: str) -> int:
        print("Code1")
        diff = 0
        left, right = 0, 0
        R = 0
        L = 0 
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                diff += 1
                L += 1
            else:
                R += 1
                diff -= 1
            while diff < 0 :
                if s[left] == "(":
                    diff -= 1
                    L -= 1
                else:
                    diff += 1
                    R -= 1
                left += 1
            res = max(res, min(L, R))
        return res * 2
            