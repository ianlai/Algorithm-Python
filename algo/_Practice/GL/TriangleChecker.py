# Input: array of numbers (lengths of potential triangle sides)
# Output: True if you can build a triangle out of every triple in array, False otherwise

input: [3,5,2,7,1]
output : True /False
3,5,2
3,5,7
3,5,1

O(1) a + b > c
c = 1, a = 5, b = 7 

TC = C(n, 3) * 1  = n! / (n-3) ! * 3! 

a b      c 
[1,2,3,5,7]

[3,5,2,7,1]
find 1st, 2nd smallest and 1st greatest 
O(N)

def checkTriangleTuple(arr):
  largest = 0 
  smallest1 = inf
  smallest2 = inf
  for num in arr:
    largest = max(largest, num)    
    if smallest1 < smallest2:   #smallest2 greater 
      if num < smallest2:  
        smallest2 = num
    else:
      if num < smallest1:
        smallest1 = num 
  return smallest1 + smallest2 > largest


a + b > c
non-decreasing order
# Input: stream (.getNext() - returns numbers in non-decreasing order, or -1 when the stream is depleted; .hasNext())
# Output: True if there is at least 1 triple that builds a triangle

True: any pair 

def checkTriangleTuple2():
  a = getNext()
  b = getNext()
  c = getNext()
  while c != -1:
    if a + b > c:
      return True
    a = b
    b = c
    c = getNext()
  return False