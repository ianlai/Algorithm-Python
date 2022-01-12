import xmath
from xmath import e
from xmath import sum

print(xmath.mymin(3, 5))
print(xmath.mymin(8, 5))

print(xmath.pi)
print(e)

print(sum(1,2,3,4))

arr = [3,4,5,6,7]
brr = ["a","b"]

for i in zip(arr, brr):
    print(i)

crr = [14,67,25,75,1,89,93,5,7,23]
res1 = []
for v in crr:
    if v < 10: 
        res1.append(v)
res2 = filter(lambda x: x < 10, crr) #return a generator 
for v in res2:
    print(v, end = " / ")
for v in res2:
    print(v, end = " / ")
print()
print(res1)
print(list(res2))