def binarySearch(arr, target):
  start, end = 0, len(arr)
  while start < end:
    mid = start + (end - start) // 2
    if target <= arr[mid]:  # "<=" needs to be end part  
      end = mid
    else:
      start = mid + 1
    # else:
    #   return mid
  return start, end

print(-3, "->", binarySearch([2,5,8], -3))
print(2, "->", binarySearch([2,5,8], 2))
print(3, "->", binarySearch([2,5,8], 3))
print(5, "->", binarySearch([2,5,8], 5))
print(7, "->", binarySearch([2,5,8], 7))
print(8, "->", binarySearch([2,5,8], 8))
print(9, "->", binarySearch([2,5,8], 9))