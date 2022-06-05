'''
- getNow()
- record(input)
- getAvg() 
'''
import time

from matplotlib import collections


def getNow():
    return int(time.time())


cur = 0


def getNow():
    global cur
    mockTime = [1, 3, 4, 6, 6, 8, 15, 35, 112,
                159, 200, 203, 207, 231, 310, 325, 388]
    assert cur < len(mockTime)

    resTime = mockTime[cur]
    cur += 1
    return resTime


# v1 最基本 舊資料不刪掉 (使用array)
class StreamAverage1:
    def __init__(self):
        self.arr = []

    #O(1)
    def record(self, input):
        self.arr.append((getNow(), input))

    #O(N)  //所有資料
    def getAvg(self):
        nowTime = 400  # mock
        valCount = 0
        valSum = 0
        for record in self.arr:
            if record[0] < nowTime - 300:
                continue
            valCount += 1
            valSum += record[1]
        return valSum / valCount
    def __str__(self):
        return str(self.arr)


# v2 舊資料刪除 (使用deque)
import collections
class StreamAverage2:
    def __init__(self):
        self.q = collections.deque()

    #O(1)
    def record(self, input):
        self.q.append((getNow(), input))

    #O(T)  //上次呼叫getAvg，刪減過後的全部資料（可能比300秒的資料更多）
    def getAvg(self):
        nowTime = 400  # mock
        valCount = 0
        valSum = 0
        for pair in list(self.q):  #avoid manipulating deque while traversing it 
            if pair[0] < nowTime - 300:
                self.q.popleft()
                continue
            valCount += 1
            valSum += pair[1]
        return valSum / valCount

    def __str__(self):
        return str(self.q)


# v3 舊資料刪除 並且 先計算好sum 
import collections
class StreamAverage3:
    def __init__(self):
        self.q = collections.deque()
        self.sum = 0
    #O(1)
    def record(self, input):
        self.q.append((getNow(), input))
        self.sum += input 

    #O(T)  //上次呼叫getAvg，刪減過後的全部資料（可能比300秒的資料更多）
    def getAvg(self):
        nowTime = 400  # mock
        for pair in list(self.q):  #avoid manipulating deque while traversing it 
            if pair[0] < nowTime - 300:
                self.q.popleft()
                self.sum -= pair[1]
                continue
        return self.sum / len(self.q)

    def __str__(self):
        return str(self.q)


# v4 舊資料刪除 並且 先計算好sum 並且 把removeOutdate() 取出 避免burst
import collections
class StreamAverage4:
    def __init__(self):
        self.q = collections.deque()
        self.sum = 0

    #O(1) + removeOutdate()
    def record(self, input):
        self.q.append((getNow(), input))
        self.sum += input 
        self.removeOutdate()

    #O(1) + removeOutdate()
    def getAvg(self):
        self.removeOutdate()
        return self.sum / len(self.q)
    
    #removeOutdate()兩次被呼叫的間隔秒數內的數據，所以這個函數可以被另外一個thread來定期呼叫
    def removeOutdate(self):
        nowTime = 400  # mock
        for pair in list(self.q):  #avoid manipulating deque while traversing it 
            if pair[0] < nowTime - 300:
                self.q.popleft()
                self.sum -= pair[1]

    def __str__(self):
        return str(self.q)

'''
Median 
  上次清  M              W
    v            t-300       t
    [.........], [...........]

使用QuickSelect: 
  - removeOutdate() 需要 O(M) 
  - getMedian()     需要 O(W)

使用Two-Heaps: 
  - removeOutdate() 需要 O(M*(M+W))  //Heap size是 M+W，每一步刪除都是新的heapify的話，就是O(N)時間  
  - getMedian()     需要 O(1)
'''
# v1 QuickSelect
import collections
class StreamMedian1:
    def __init__(self):
        self.q = collections.deque()

    #O(1) + removeOutdate()
    def record(self, input):
        self.q.append((getNow(), input))
        self.removeOutdate()

    #O(W) + removeOutdate()  //W是在300秒interval內的資料點個數
    def getMedian(self):
        self.removeOutdate()
        median = 0
        if len(self.q) % 2 == 0:
            m1 = self._findTopK(self.q, len(self.q) // 2, 0, len(self.q) - 1)
            m2 = self._findTopK(self.q, len(self.q) // 2 - 1, 0, len(self.q) - 1)
            median = (m1 + m2) / 2
        else:
            median = self._findTopK(self.q, len(self.q) // 2, 0, len(self.q) - 1)
        return median  
    
    #removeOutdate()兩次被呼叫的間隔秒數內的數據，所以這個函數可以被另外一個thread來定期呼叫
    def removeOutdate(self):
        nowTime = 400  # mock
        for pair in list(self.q):  #avoid manipulating deque while traversing it 
            if pair[0] < nowTime - 300:
                self.q.popleft()

    def _findTopK(self, arr, k, start, end):
        mid = start + (end - start) // 2
        pivot = arr[mid][1] # time, val
        l, r = start, end 
        while l <= r:
            while l <= r and arr[l][1] < pivot:
                l += 1
            while l <= r and pivot < arr[r][1]:
                r -= 1
            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        if k >= l:
            return self._findTopK(arr, k, l, end)
        elif k <= r:
            return self._findTopK(arr, k, start, r)
        else:  #found 
            return arr[k][1]

    def __str__(self):
        return str(self.q)


'''
Find Average
'''
# sa4 = StreamAverage4()
# data = [5, 4, 8, 7, 10, 10, 10, 30, 50, 70, 120, 5, 15, 70]
# for d in data:
#     sa4.record(d)
# print(sa4)
# print(sa4.getAvg())


'''
Find Median
'''
sm1 = StreamMedian1()
data = [5, 4, 8, 7, 10, 10, 10, 30, 50, 70, 120, 5, 15, 70]
for d in data:
    sm1.record(d)
print(sm1)
print(sm1.getMedian())
