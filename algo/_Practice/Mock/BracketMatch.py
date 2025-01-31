
'''
An example of correctly matched String of Brackets  
“(())()”

A noncorrectly matched example will be:
  
  “)(“  can be made correctly matched with 2 other brackets: (, )   --->  
     
     and “((” you can also add maximum of 2 brackets ),) ----> "(())""
     
    Examples:

    input:  text = “(()”
    output: 1

    input:  text = “(())”
    output: 0

    input:  text = “())(”  ---> sol: () () ()
    output: 2
                        
      ( ) {) (}
  L:  1 1 1  3 
  R:  0 1 2  2
          1  1
 
              
      ( ( ( ) ) )
  L   1 2 3 3 3 3
  R   0 0 0 1 2 3
              
      ( ) ) ) (
   L  1 1 2 3 4  
   R  0 1 2 3 3
          1 1 1  <-- TOTAL: 3
        
    increment L when you get "("
        incremnt R when you get ")"
       
'''

def bracket_match(text):
  pass # your code goes here

  if len(text) == 0:
    return 0
  l, r, res = 0, 0, 0
  for ch in text: 
    if ch == '(':
      l += 1 
    else: 
      r += 1
      if l < r: 
        l += 1
        res += 1
  res += (l - r)    
  return res 

# space: O(1)
def bracket_match2(text):

  if len(text) == 0:
    return 0

  diff, res = 0, 0
  for ch in text: 
    if ch == '(':
      diff += 1 
    else: 
      diff -= 1
      if diff < 0: 
        diff += 1
        res += 1
  res += diff    
  return res 

# space: O(n)
def bracket_match3(text):

    if len(text) == 0:
        return 0
    stack = []
    res = 0
    for ch in text: 
        if ch == '(':
            stack.append(ch)
        else: 
            if stack:
                stack.pop()
            else:
                res += 1

    return res + len(stack)

# print(bracket_match("(()))((()")) # 3
# print(bracket_match("))(()(("))   # 5

# print(bracket_match2("(()))((()")) # 3
# print(bracket_match2("))(()(("))   # 5

print(bracket_match3("(()))((()")) # 3
print(bracket_match3("))(()(("))   # 5