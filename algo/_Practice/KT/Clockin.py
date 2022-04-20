'''
Problem-1  找進出紀錄不符的人
Given a list of people who enter and exit, find the people who entered without
their badge and who exited without their badge.

// badge_records = [
//   ["Martha",   "exit"],
//   ["Paul",     "enter"],
//   ["Martha",   "enter"],
//   ["Martha",   "exit"],
//   ["Jennifer", "enter"],
//   ["Paul",     "enter"],
//   ["Curtis",   "enter"],
//   ["Paul",     "exit"],
//   ["Martha",   "enter"],
//   ["Martha",   "exit"],
//   ["Jennifer", "exit"],
// ]

// Expected output: ["Paul", "Curtis"], ["Martha"]

思路：用一個boolean來記錄是否已打卡即可。
'''



'''
Problem-2  一小時內Access多次

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

# a = "1300"
def timeDifference(a, b):
    aHour = a // 100
    bHour = b // 100
    aMinute = a % 100
    bMinute = b % 100
    return aHour * 60 + aMinute - (bHour * 60 + bMinute)

