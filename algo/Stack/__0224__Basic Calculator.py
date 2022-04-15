class Solution:
    
    # 2022/04/15
    # Implement simple plus/minus calculate function first
    # Use stack to store the results [O(n):56% / O(n):78%]
    def calculate(self, s: str) -> int:
        
        # [12, "+", 17, "-", 8] -> 21 
        def cal(expression):
            subtotal = 0
            sign = 1
            for op in expression:
                if op == "+":
                    sign = 1
                elif op == "-":
                    sign = -1
                else:
                    subtotal += sign * int(op)
            return subtotal
                    
        stack = []
        number = ""
        for op in s:
            if op.isdigit():
                number += op
            else:
                if number: 
                    stack.append(int(number))
                    number = ""
                if op == " ":
                    continue
                elif op == ")":
                    expression = []
                    while stack[-1] != "(":
                        expression.append(stack.pop())
                    stack.pop()
                    subtotal = cal(reversed(expression))
                    stack.append(subtotal)
                else:
                    stack.append(op)
        if number:
            stack.append(int(number))
        return cal(stack)
                
                
                