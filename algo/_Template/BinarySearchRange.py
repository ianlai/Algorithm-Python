#找值域(Range) 

# 123456  => start, end = 1, 6
# xxxxOO  => 找第一個O，會得到5 

# 123456  => start, end = 1, 6
# xxxxxO  => 找第一個O，會得到6  //雖然搜索範圍是[1:6)，看似不包含6，但其實是有可能使用end作為答案

# 123456  => start, end = 1, 5
# xxxxxO  => 找第一個o，會得到5  //錯誤 所以end必須要包到答案

# 例如搜尋arr = [3, 5, 5, 7]
# start, end = 0, len(arr) = 4
# 雖然搜尋範圍說是[start:end)
# 但答案是可能出現[0:4]的，例如要找8就會得到4 
# 可以解釋[start:end)是可能的index，但其實BS是找區間的，只是index剛好等於左區間，但區間其實比index多一格，所以可能出現答案4
# 所以重點是找值域的時候，[start:end]要包含到第一個O。


def isTrue(val):
  if val < 6.5:
    return False
  else:
    return True

arr = []
start, end = 1, 6 #搜尋範圍不包含6，但結果是可能選到6的（因為start = mid + 1，所以可以跳到6) 
                  #如果從1~6全部都是X，答案最多只能給到6
for i in range(start, end+1):
  arr.append(i)
for v in arr:
  print(v, isTrue(v))

while start < end :
  mid = start + (end - start) // 2
  if isTrue(mid):
    end = mid 
  else:
    start = mid + 1 
  print(mid, "->", isTrue(mid), start, end)

print("ans:", start)