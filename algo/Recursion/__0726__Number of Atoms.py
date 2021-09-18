
# "Ka4(ONa(SO3)2)3A4"
# "(H)"
# "Mg(H2O)N"

class AST:
    def __init__(self, num = 1, prefix = None, core = None, suffix = None):
        self.prefix = prefix  #not expandable 
        self.num = num
        self.core = core
        self.suffix = suffix
        self.atom_count = collections.defaultdict(int)
        
    def __str__(self):
        return "AST: " + str(self.num) + "\n  prefix:" + str(self.prefix) + "\n  core:" + str(self.core) + "\n  suffix:" + str(self.suffix) 
    
    @staticmethod
    def tokenize(s):
        tokens = collections.deque()
        num = ""
        for c in s:
            if c.isdigit():
                num += c
            else:
                if num:
                    tokens.append(num)
                    num = ""
                if c.islower():
                    tokens[-1] += c
                else:
                    if tokens and tokens[-1].isalpha() and not c.isdigit(): #add 1 after alpha if no number
                        tokens.append('1')
                    if tokens and tokens[-1] == ")" and not c.isdigit():    #add 1 after ")" if no number
                        tokens.append('1')
                    tokens.append(c)
        if num:
            tokens.append(num)
                    
        return tokens
    
    @staticmethod
    def parse(tokens):
        #print(tokens)
        if not tokens:
            return None
        token = tokens.popleft()
        if token.isalpha():
            prefix = token
            num = 1
            if tokens:
                num = int(tokens.popleft())
            suffix = AST.parse(tokens)
            return AST(num, prefix, None, suffix)
        elif token == "(":
            right, left = 1, 0
            core = ""
            core_deq = collections.deque([])
            num = 0
            #for i, t in enumerate(tokens):
            i = 0
            while tokens:
                t = tokens.popleft()   
                core_deq.append(t)
                if t == "(":
                    right += 1
                if t == ")":
                    left += 1
                if right == left:
                    core_deq.pop()
                    core = AST.parse(core_deq)  #remove last right bracket
                    #core = AST.parse(tokens[:i])  #remove last right bracket
                    #suffix = AST.parse(tokens[i+1:])
                    num = 1
                    if tokens:
                        num = int(tokens.popleft())
                    suffix = AST.parse(tokens)
                i += 1
            return AST(num, None, core, suffix)
        else:
            return None            
            
    def decode(self):
        if self is None:
            return 
        
        if self.prefix:
            self.atom_count[self.prefix] += 1
            
        if self.core:
            self.core.decode()
            if self.core.atom_count:
                for k, v in self.core.atom_count.items():
                    self.atom_count[k] += v
        
        # Number only affects prefix and core, but not suffix
        for k, v in self.atom_count.items():
            self.atom_count[k] = v * self.num
            
        if self.suffix:
            self.suffix.decode()
            if self.suffix.atom_count:
                for k, v in self.suffix.atom_count.items():
                    self.atom_count[k] += v

        #print(self.num, self.prefix, self.atom_count)
        return 
    
    def getCountString(self) -> str:
        res = ""
        for k in sorted(self.atom_count):
            v = self.atom_count[k] 
            if v == 1:
                res += k
            else:
                res += k + str(v)
        return res
    
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        tokens = AST.tokenize(formula)
        #print("Tokens:", tokens)
        ast = AST.parse(tokens)
        ast.decode()
        return ast.getCountString()
    
    



# Incorrect way to write parse function:

        # core_deq = collections.deque()
        # left, right = 0, 0
        # on = False
        # prefix = ""
        # while tokens:
        #     token = tokens.popleft() 
        #     if token == "(":
        #         left += 1
        #         on = True
        #     elif token == ")":
        #         right += 1
        #         if right > 0 and left == right:
        #             on = False
        #     elif token.isdigit():
        #         num = int(token)
        #         if left > 0:
        #             core = AST.parse(core_deq)
        #             suffix = AST.parse(tokens)
        #             return AST(num, prefix, core, suffix)
        #         else:
        #             suffix = AST.parse(tokens)
        #             return AST(num, prefix, None, suffix)
        #     else:
        #         prefix = token 
        #     if on:
        #         core_deq.append(token)
        # return None