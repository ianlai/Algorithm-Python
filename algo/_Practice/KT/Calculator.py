'''
Problem-1 Simple (no paranthese)

input: " 2-1 + 2 "
output: 3 
'''


'''
Problem-2 With paranthese

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''


input1 = " 2-1 + 2 "
input2 = "  (1+(4+5+2)-3)+(6+8) "


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

def calulate1(input):
    curNumber = ""
    expression = []
    for char in input:
        if char.isdigit():
            curNumber += char
        else:
            if curNumber:
                expression.append(int(curNumber))
                curNumber = ""
            if char == " ":
                continue
            else:
                expression.append(char)  # "+" or "-"
    return cal(expression)

print(calulate1(input1))

# ============================================================================

def calulate2(input):
    curNumber = ""
    stack = []
    for ch in input:
        if ch.isdigit():
            curNumber += ch
        else:
            if curNumber:
                stack.append(int(curNumber))
                curNumber = ""
            if ch == " ":
                continue
            elif ch == ")":
                expression = []
                while stack[-1] != "(":
                    expression.append(stack.pop())
                stack.pop() # remove "("
                subtotal = cal(expression[::-1])
                stack.append(subtotal)
                #print(expression[::-1], stack)
            else:
                stack.append(ch)  # "+" or "-" or "("
    return cal(stack)
print(calulate2(input2))
