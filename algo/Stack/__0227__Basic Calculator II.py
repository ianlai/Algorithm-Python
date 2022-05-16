class Solution:
    
    # 2022/05/17
    # Tokenize then calculate (twice) [O(N): 10% / O(N): 5%]
    def calculate(self, s: str) -> int:

        def parse(s):
            ops = []
            num = ""
            for ch in s:
                if ch.isdigit():
                    num += ch
                else:
                    if ch == " ":
                        continue
                    if len(num) != 0:
                        ops.append(num)
                    ops.append(ch)
                    num = ""
                    
            if len(num) != 0:
                ops.append(num)
            return ops
        
        def cal(ops):
            if len(ops) == 0:
                return 0
            if len(ops) == 1:
                return int(ops[0])
            
            #stack = [int(ops[0])]  
            stack = []
            for i, op in enumerate(ops):
                if op.isdigit():
                    op = int(op)
                    if len(stack) == 0:
                        stack.append(op)
                        continue
                        
                    if stack[-1] == "*":
                        stack.pop()
                        stack.append(stack.pop() * op)
                    elif stack[-1] == "/":
                        stack.pop()
                        stack.append(stack.pop() // op)
                    else:
                        stack.append(op)
                else:
                    stack.append(op)
                # if i == 0:
                #     continue
                # if ops[i-1] == "*":
                #     sub = int(stack.pop()) * int(op)
                #     stack.append(sub)
                # elif ops[i-1] == "/":
                #     sub = int(stack.pop()) // int(op)
                #     stack.append(sub)
                # else:
                #     stack.append(ops[i-1])
            
            res = int(stack[0])
            sign = 1
            for i in range(1, len(stack)):
                if stack[i] == "+":
                    sign = 1
                elif stack[i] == "-":
                    sign = -1
                else:
                    res += sign * int(stack[i])
            return res
                    
        ops = parse(s)
        res = cal(ops)
        return res 