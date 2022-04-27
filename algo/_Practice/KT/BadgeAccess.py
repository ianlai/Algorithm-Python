'''
======================================
[Problem-1] 找進出紀錄不符的人

Given a list of people who enter and exit, find the people who entered without
their badge and who exited without their badge.

badge_records = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
]

Expected output: ["Paul", "Curtis"], ["Martha"]
output[0]: 只有進沒有出 
output[1]: 只有出沒有進

思路：用一個boolean來記錄是否已打卡即可。
'''
import collections

badge_records = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
]
def findInvalidRecords(records):
    print("(1) findInvalidRecords()")
    res = [[], []]
    inOffice = set()
    for name, event in records:
        if event == "enter":
            if name in inOffice:
                res[0].append(name)
            else:
                inOffice.add(name)
        elif event == "exit":
            if name not in inOffice:
                res[1].append(name)
            else:
                inOffice.remove(name)
        else:
            raise Exception()
    res[0].extend(list(inOffice)) #剩下還沒出來的
    return res

print(findInvalidRecords(badge_records))
print()


'''
======================================
[Problem-2] 一小時內Access多次

给 list of [name, time], time is string format: '1300' //下午一点
return: list of names and the times where their swipe badges within one hour. if there are multiple intervals that satisfy the condition, return any one of them.
name1: time1, time2, time3...
name2: time1, time2, time3, time4, time5...

example:
input: [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']] 
output: {
'Martha': ['1600', '1620', '1530']
}

思路：存入一個Map內，人對時間，再把時間做排序，比較前後看是否有小於一小時。
'''
records = [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']] 
def findMultipleAccessWithinOneHour(records):
    print("(2) findMultipleAccessWithinOneHour")
    nameToTime = collections.defaultdict(list)
    for name, time in records:
        nameToTime[name].append(time)
    
    res = {}
    for name, timelist in nameToTime.items():
        for i in range(1, len(timelist)):
            if timeDifference(timelist[i-1], timelist[i]) < 60:
                res[name] = nameToTime[name]
    return res

# a = "1300"
# return b - a   (b > a)
def timeDifference(a, b):  
    a, b = int(a), int(b)
    aHour = a // 100
    bHour = b // 100
    aMinute = a % 100
    bMinute = b % 100
    return (bHour * 60 + bMinute) - (aHour * 60 + aMinute)

print(findMultipleAccessWithinOneHour(records))
print()