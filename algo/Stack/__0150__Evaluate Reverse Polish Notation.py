class Solution:
    
    # 2022/02/08
    # Stack [O(n): 54%]
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                op2 = stack.pop()
                op1 = stack.pop()
                if token == "+":
                    stack.append(op1 + op2)
                elif token == "-":
                    stack.append(op1 - op2)
                elif token == "*":
                    stack.append(op1 * op2)
                elif token == "/":
                    if op1 * op2 < 0:
                        stack.append(math.ceil(op1 / op2))
                    else:
                        stack.append(op1 // op2)
            else:
                stack.append(int(token))
        return stack[0]
                