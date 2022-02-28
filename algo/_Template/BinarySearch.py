import bisect
def binarySearchLeft(arr, target):
  start, end = 0, len(arr)
  while start < end:
    mid = start + (end - start) // 2
    if target <= arr[mid]: # even when found the target, end still goes left 
      end = mid
    else:                  
      start = mid + 1 
  return start

def binarySearchRight(arr, target):
  start, end = 0, len(arr)
  while start < end:
    mid = start + (end - start) // 2
    if target < arr[mid]:  
      end = mid
    else:                 # even when found the target, start still goes right 
      start = mid + 1
  return start

targets = [2, 3, 4, 5, 6, 7, 8]
arr = [3, 5, 5, 5, 7]  #search array
for t in targets:
  print(t, "=> ", binarySearchLeft(arr, t), bisect.bisect_left(arr,t), "--", binarySearchRight(arr, t), bisect.bisect(arr, t))