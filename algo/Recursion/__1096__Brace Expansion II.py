class AST:
    
    def tokenize(exp):
        tokens = collections.deque()
        for c in exp:
            if tokens and tokens[-1].isalpha() and c.isalpha():
                tokens[-1] += c
            else:
                tokens.append(c)
        #tokens.appendleft("{")
        #tokens.append("}")
        return list(tokens)
    
    def parse(tokens):
        print(">> tokens  ", tokens)
        level = 0
        groups = [[]]
        start = 0
        for idx, token in enumerate(tokens):
            if token == "{":
                if level == 0:
                    start = idx + 1 
                level += 1
            elif token == "}":
                level -= 1
                if level == 0:
                    groups[-1].append(AST.parse( tokens[start:idx]))
            elif token == "," and level == 0:
                groups.append([])
            elif level == 0:  #literal 
                groups[-1].append(token)
        
        word_set = set()
        #print("<< groups:", groups)
        for group in groups:
            while len(group) > 1:
                last = group.pop()
                
                second_last = group.pop()
                temp = [i+j for j in last for i in second_last]
                group.append(temp)
            
            word_set.update(group.pop())
            
            # if isinstance(group[0], str):
            #     word_set.add(group.pop())
            # else:
            #     word_set.update(group.pop())
                
        #print(word_set)
        res = (word_set)
        #print("<< tokens:", tokens, "groups:", groups, "res:", res)
        return res
        
class Solution:
    
    def braceExpansionII(self, expression: str) -> List[str]:
        #tokens = AST.tokenize(expression)
        #print("tokens:", tokens)
        res = AST.parse(expression)
        print("res:", res)
        return sorted(res)
    
    def braceExpansionII2(self, expression: str) -> List[str]:
        print(">> expression  ", expression)

        groups = [[]]
        level = 0
        for i, c in enumerate(expression):
            if c == '{':
                if level == 0:
                    start = i+1
                level += 1
            elif c == '}':
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(expression[start:i]))
            elif c == ',' and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append(c)
        word_set = set()
        for group in groups:
            word_set |= set(map(''.join, itertools.product(*group)))
        res = sorted(word_set)
        print("<< expression:", expression, "groups:", groups, "res:", res)
        return res
    
# class AST:
    
#     def tokenize(exp):
#         tokens = collections.deque()
#         for c in exp:
#             if tokens and tokens[-1].isalpha() and c.isalpha():
#                 tokens[-1] += c
#             else:
#                 tokens.append(c)
#         tokens.appendleft("{")
#         tokens.append("}")
#         return tokens
    
#     def parse(tokens):
#         print(tokens)
#         tokens.pop()
#         tokens.popleft()
        
#         coreDeq = collections.deque()
#         coreArr = []
#         left, right = 0, 0
#         isUnion = False
#         lastClose = 0
#         for i, token in enumerate(tokens):
            
#             print(token , left, right, isUnion)
#             if token == "{":
#                 left += 1 
#             elif token == "}":
#                 right += 1
#                 if left == right:
#                     print("======== L==R ========")
#                     coreDeq.append(token)
#                     if coreArr:
#                         curArr = AST.parse(coreDeq)
#                         nxt = tokens[lastClose+1]
#                         if nxt == ",":
#                             isUnion = True
#                         else:
#                             print("coreArr:", coreArr, "curArr:", curArr, "isUnion:", isUnion)
#                             if isUnion:
#                                 coreSet = set(coreArr)
#                                 for cur in curArr:
#                                     coreSet.add(cur)
#                                 coreArr = list(coreSet)
#                             else:
#                                 tmpArr = list(coreArr)
#                                 coreArr = []
#                                 for tmp in tmpArr:
#                                     for cur in curArr:
#                                         # newtmp = list(tmp)
#                                         # newtmp.append(cur)
#                                         # coreArr.append(newtmp)
#                                         newtmp = "".join(tmp)
#                                         newtmp += cur
#                                         coreArr.append(newtmp)
#                     else:
#                         coreArr = AST.parse(coreDeq)
#                     isUnion = False
#                     left, right = 0, 0
#                     coreDeq = collections.deque()
#                     lastClose = i
#                     continue
#             # elif token == ",":
#             #     print("SET TRUE")
#             #     isUnion = True
                
#             if token != ",":
#                 coreDeq.append(token)
#         if not coreArr:  #not expandable
#             coreArr = list(coreDeq)
            
#         print("coreArr:", coreArr)
#         return coreArr
    
# class Solution:
    
#     # literal := [a-z]+ 
#     # number  := [0-9]+
#     # comma   := ','
#     # left    := '{'
#     # right   := '}'
#     # exp     := <left> <literal>? (<comman>? <left><exp> (<comma><exp>)? <right> <exp>?)?<right>
    
#     def braceExpansionII(self, expression: str) -> List[str]:
#         tokens = AST.tokenize(expression)
#         res = AST.parse(tokens)
#         print(res)
#         return sorted(res)