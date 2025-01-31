'''
  [4,1,8,2,3]  #k=2 -> 3 (idx = 4) 
'''
def findTopK(arr, k):
  return _findTopK(arr, k, 0, len(arr) - 1)

def findMedian(arr):
  median = 0
  if len(arr) % 2 == 0:
    mid = len(arr) // 2
    m1 = _findTopK(arr, mid, 0, len(arr) - 1)
    m2 = _findTopK(arr, mid - 1, 0, len(arr) - 1)
    median = (m1 + m2) / 2
  else:
    median = _findTopK(arr, len(arr) // 2, 0, len(arr) - 1)
  return median 

# Quick Select: O(N)
def _findTopK(arr, k, start, end):
  if not 0 <= k < len(arr):
    return None
  mid = start + (end - start) // 2
  pivot = arr[mid]
  l, r = start, end
  while l <= r:
    while l <= r and arr[l] < pivot:
      l += 1
    while l <= r and arr[r] > pivot:
      r -= 1
    if l <= r:
      arr[l], arr[r] = arr[r], arr[l]
      l += 1
      r -= 1
  if k >= l:
    return _findTopK(arr, k, l, end)
  elif k <= r:
    return _findTopK(arr, k, start, r)
  else:
    #print("r:", r, "k:", k, "l:", l)
    return arr[k]

print(findTopK([4,1,8,2,3], 0))  #1
print(findTopK([4,1,8,2,3], 1))  #2
print(findTopK([4,1,8,2,3], 2))  #3
print(findTopK([4,1,8,2,3], 3))  #4
print(findTopK([4,1,8,2,3], 4))  #8
print(findTopK([4,1,8,2,3], 5))  #None 

print(findMedian([4,1,8,2,3]))     #3
print(findMedian([4,1,2,3]))       #2.5 
print(findMedian([9,1,6,2,8,15]))  #7.0








