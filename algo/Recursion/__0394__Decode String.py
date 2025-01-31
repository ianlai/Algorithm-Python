# https://leetcode.com/problems/decode-string/
# 
# Test: 
# "a3[b2[cd]e2[f]]g12[h]ijk"
# "100[leetcode]"
    

# BNF:
#  literal := [A-Z][a-z]*
#  number  := [0-9]+
#  left    := "["
#  right   := "]"
#  exp     := <literal>? [<number><left><exp><right> <exp>?] 
# class AST:
#     def __init__(self, prefix, num=0, core=None, suffix=None):
#         self.prefix = prefix
#         self.num = num
#         self.core = core
#         self.suffix = suffix
        
#     @staticmethod 
#     def tokenize(s):
#         tokens = deque()
#         str_token = ''
#         num_token = ''
#         def flush_num():
#             nonlocal num_token
#             nonlocal tokens
#             if num_token:
#                 tokens.append(int(num_token))
#                 num_token = ''
#         def flush_str():
#             nonlocal str_token
#             nonlocal tokens
#             if str_token:
#                 tokens.append(str_token)
#                 str_token = ''

#         for c in s:
#             if c == '[':  # The number always follows '[', so skip the '[' token.
#                 flush_num()
#             elif c == ']':
#                 flush_str()
#                 tokens.append(c)
#             elif c.isdigit():
#                 flush_str()
#                 num_token += c
#             else:
#                 str_token += c

#         flush_str()
#         return tokens
        
#     @staticmethod
#     def parse(tokens): # return AST
#         prefix = ''
#         while tokens:
#             token = tokens.popleft()
#             if token == ']':
#                 break
#             elif isinstance(token, int):
#                 num = token
#                 core = AST.parse(tokens)
#                 suffix = AST.parse(tokens)
#                 return AST(prefix, num, core, suffix)
#             else:
#                 prefix = token
#         return AST(prefix)
    
#     def decode(self):
#         ans = self.prefix
#         if self.core is not None:
#             ans += self.core.decode() * self.num
#         if self.suffix is not None:
#             ans += self.suffix.decode()
#         return ans
    
#     def __str__(self):
#         return (" <" + "\n" 
#                 + "Prefix:" + str(self.prefix) + "\n  " 
#                 + "Num   :" + str(self.num)    + "\n  " 
#                 + "Core  :" + str(self.core)   + "\n  " 
#                 + "Suffix:" + str(self.suffix) + "\n >")

# def decodeString(self, s: str) -> str:
#     print("AST")
#     token = AST.tokenize(s)
#     print(token)
#     ast = AST.parse(token)
#     print(ast)
#     return ast.decode()
    
class AST:
    def __init__(self, prefix, num = None, core = None, suffix = None):
        self.prefix = prefix
        self.num = num
        self.core = core
        self.suffix = suffix
        
    @staticmethod 
    def tokenize(s):
        tokens = deque()
        num_token = ""
        str_token = ""
        for c in s:
            if c == "[":
                tokens.append(num_token)
                tokens.append(c)
                num_token = ""
            elif c == "]":
                if str_token:
                    tokens.append(str_token)
                    str_token = ""
                tokens.append(c)
            elif c.isdigit():
                num_token += c
                if str_token:
                    tokens.append(str_token)
                    str_token = ""
            else:
                str_token += c 
        if str_token:
            tokens.append(str_token)
        return tokens
    
    @staticmethod       
    def parse(tokens):
        print(tokens)
        prefix = ""
        while tokens:
            token = tokens.popleft()
            if token == "[":
                continue
            elif token == "]":
                break
            elif token.isdigit():
                num = int(token)
                tokens.popleft() #left
                core = AST.parse(tokens)
                suffix = AST.parse(tokens)
                return AST(prefix, num, core, suffix)
            else:
                prefix = token
        return AST(prefix)
    
    def decode(self):
        decoded_str = self.prefix
        if self.core:
            decoded_str += self.num * self.core.decode()
        if self.suffix:
            decoded_str += self.suffix.decode()
        return decoded_str
    
    def print(self, layer):
        print("+ " * layer + "prefix:" + self.prefix)
        print("+ " * layer + "num:" + str(self.num))
        
        print("+ " * layer + "core:")
        if self.core:
            self.core.print(layer + 1)
            
        print("+ " * layer + "suffix:")
        if self.suffix:
            self.suffix.print(layer + 1)
    
class Solution:
    
    # Divide to steps: tokenize, parse to form AST, decode 
    def decodeString(self, s: str) -> str:
        print("Tokenize -> parse -> decode")
        tokens = AST.tokenize(s)
        ast = AST.parse(tokens)
        #ast.print(1)
        ast_decoded = ast.decode()
        return ast_decoded 
        
    # ===============================================
    def decodeString2(self, s: str) -> str:
        print("2 stack")
        res,num = "",0
        st = []
        for c in s:
            if c.isdigit():
                num = num*10+int(c)    
            elif c=="[":
                st.append(res)
                st.append(num)
                res=""
                num=0
            elif c=="]":
                pnum = st.pop()
                pstr = st.pop()
                res = pstr + pnum*res
            else:
                res+=c    
        return res
  
    # Recursion [9%]
    def decodeString1(self, s: str) -> str:
        print("Recursive")
        #print("  s:", s)
        
        numList = []
        numIdxList = []
        quoteList = []
        
        left, right = 0, 0
        leftIdx, rightIdx, numIdx = -1, -1, -1 #left quote, right quote, first digit
        
        for i, c in enumerate(s):
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
                    numList.append(int(s[numIdx:leftIdx]))
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
