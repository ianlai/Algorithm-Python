'''
Python Validator

1. 開頭indent是0
2. 上一個是control statement（結尾是冒號）的話可以縮排
3. 上一個不是control statement不能縮排 
4. 上一個是一般statement的話，不能縮排，但可以退回或相同


Example1: False
----------------------
  a = 1      #False 因為開頭不是0
def func():  
----------------------


Example2:  False
----------------------
a = 1      
def func(): 
    b = 2      #必須縮排 因為上一個是control
        c = 3  #不可縮排     
----------------------


Example3:  False
----------------------
a = 1      
def func(): 
    b = 2      #必須縮排 因為上一個是control
    if b > 1:
    c = 3      #必須縮排 因為上一個是contorl
----------------------

Example4:  False
----------------------
a = 1      
def func(): 
    b = 2      #必須縮排 因為上一個是control
    if b > 1:
        c = 3  #必須縮排 因為上一個是control  
    d = 4
    if d > 3:  
                e = 5  #必須縮排 (縮排可以任意多) 因為上一個是control
                f = 6  #上一個不是control  可同排
  g = 7        #上一個不是control  可退回 (但退回的indent和前面的所有indent都不同 False)
h = 8          #上一個不是control  可退回
----------------------

'''


def calIndent(line):
    indent = 0
    for ch in line:
        if ch == " ":
            indent += 1
        else:
            break
    return indent

def validatePython(lines):
    if len(lines) == 0:
        return True

    stack = []
    for line in lines:
        indent = calIndent(line)
        if not stack:
            if indent != 0:
                print("[Error] Start indent not 0")
                return False
        elif stack[-1][-1] == ":":  #control statment 
            lastIndent = calIndent(stack[-1])
            if indent <= lastIndent:
                print("[Error] Line after control statment doesn't indent")
                return False
        else:                       #normal 
            while stack and calIndent(stack[-1]) > indent:
                stack.pop() 

            assert stack
            if indent != calIndent(stack[-1]):
                print("[Error] Line after normal statement doesn't match:", line)
                return False
        stack.append(line)
    return True

#False
codes1 = [
"a = 1",
"   def func():",
"      b = 100",
]

#True
codes2 = [
"a = 1",
"def func():",
"         b = 100",
]


#False
codes3 = [
"a = 1",
"def func():",
"         b = 100",
"         if b > 1:",
"        c = 3",
"            d = 4", 
"e = 5"
]

#True
codes4 = [
"a = 1",
"def func():",
"    if a > 0:", 
"         b = 100",
"         if b > 1:",
"              c = 3",
"              d = 4",
"         else:",
"            e = 5,",
"    f = 6",
"    if f > 2:",
"                          g = 7",
"h = 8",
"i = 9"
]

# for line in codes4:
#     print(line)

print(validatePython(codes4))