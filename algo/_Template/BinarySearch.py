import bisect

# 找到target的時候，使用他的左區間，也就是他自己的index
# 有複數target的時候，使用最左元素的左區間，也就是第一個target的index 
# 一般insert都使用left search  (e.g. insert sort)
#        [3,  5,   8]
# 區間   0   1    2    3
# idx     0   1    2
# idx和左區間是相同的

def binarySearchLeft(arr, target):
  start, end = 0, len(arr)
  while start < end:
    mid = start + (end - start) // 2
    if arr[mid] < target: 
      start = mid + 1
    else:        # even when found the target (=), end still goes left
      end = mid                  
  return start


# 找到target的時候，使用他的右區間，也就是他自己的index+1
# 有複數target的時候，使用最右元素的右區間，也就是最後一個個target的index+1
#        [3,  5,   8]
# 區間   0   1    2    3
# idx     0   1    2
# 右區間比idx多1 
# 所以right search是找複數target的右邊區間時可以使用（很少這種例子，例如如果有相同元素則排在他後面）
def binarySearchRight(arr, target):
  start, end = 0, len(arr)
  while start < end:
    mid = start + (end - start) // 2
    if arr[mid] <= target:  
      start = mid + 1  # even when found the target (=), start still goes right 
    else:                 
      end = mid 
  return start

targets = [2, 3, 4, 5, 6, 7, 8]
arr = [3, 5, 5, 7]  #search array
print(arr)
for t in targets:
  print(t, "=> L:", binarySearchLeft(arr, t), bisect.bisect_left(arr,t), "---- R:", binarySearchRight(arr, t), bisect.bisect(arr, t))



#Binary Search
# (1) 直接找arr
#   - 找index
#     - 單元素
#     - 重複元素
#   - insert 從左插入
#     - 單元素   [3]  //0 
#     - 重複元素 [3,3]  //0
#   - insert 從右插入
#     - 單元素   [3]  //1
#     - 重複元素 [3,3] //2
# (2) 轉換找值域
#   - xxxxxoooooo 找最後一個x (start-1) 或第一個o (start)
