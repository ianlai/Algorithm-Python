import time
import random
from UnrolledLinkedList import UnrolledLinkedList
from LinkedList import LinkedList
from ArrayList import ArrayList

ul4 = UnrolledLinkedList(4)
ul100 = UnrolledLinkedList(100)
ul1000 = UnrolledLinkedList(1000)

ll = LinkedList()
ar = ArrayList()

myarray = []

def verifyResult(): 
    print()
    print()
    if ul4.getArray() == ll.getArray() == ar.getArray() == ul1000.getArray() == ul100.getArray():
        print("Verification succssful (ul_small == ul_medium == ul_large == ll == ar)")
        return 
    
    if ul4.getArray() != ll.getArray():
        print("Verification failed (ul_small != ll)") 
    if ul4.getArray() != ar.getArray():
        print("Verification failed (ul_small != ar)")
    if ul4.getArray() != ul100.getArray():
        print("Verification failed (ul_small != ul_medium)")
    if ul4.getArray() != ul1000.getArray():
        print("Verification failed (ul_small != ul_large)")

    print("len of ul_large:" , len(ul1000.getArray()))
    print("len of ul_medium:", len(ul100.getArray()))
    print("len of ul_small:" , len(ul4.getArray()))
    print("len of ll      :" , len(ll.getArray()))
    print("len of ar      :" , len(ar.getArray()))

number = 80000
idxMax = 1000
valMax = 10000
randIdxArray = []
randValArray = []
timeArray = []

for i in range(number):
    randIdx = random.randrange(0, idxMax)
    randVal = random.randrange(0, valMax)
    randIdxArray.append(randIdx)
    randValArray.append(randVal)

def benchmarkUL_small():

    # Insert 
    s = time.time()
    
    for i in range(number):
        ul4.insert(randIdxArray[i], randValArray[i])
    e = time.time()
    timeArray.append((e - s, "Unrolled LL (4)", "insert"))
    
    # Get 
    s = time.time()
    for i in range(number):
        ul4.get(randIdxArray[i])
    e = time.time()
    timeArray.append((e - s, "Unrolled LL (4)", "get"))

    # PushLeft
    s = time.time()
    for i in range(number):
        ul4.insert(0, randValArray[i])
    e = time.time()
    timeArray.append((e - s, "Unrolled LL (4)", "pushLeft"))


def benchmarkUL_medium():

    # Insert 
    s = time.time()
    randIdx = random.randrange(0, idxMax)
    randVal = random.randrange(0, valMax)
    for i in range(number):
        ul100.insert(randIdxArray[i], randValArray[i])
    e = time.time()
    timeArray.append((e - s, "Unrolled LL (100)", "insert"))

    # Get 
    s = time.time()
    for i in range(number):
        ul100.get(randIdxArray[i])
    e = time.time()
    timeArray.append((e - s, "Unrolled LL (100)", "get"))

    # PushLeft
    s = time.time()
    for i in range(number):
        ul100.insert(0, randValArray[i])
    e = time.time()
    timeArray.append((e - s, "Unrolled LL (100)", "pushLeft"))

def benchmarkUL_large():

    # Insert 
    s = time.time()
    randIdx = random.randrange(0, idxMax)
    randVal = random.randrange(0, valMax)
    for i in range(number):
        ul1000.insert(randIdxArray[i], randValArray[i])
    e = time.time()
    timeArray.append((e - s, "Unrolled LL (1000)", "insert"))

    # Get 
    s = time.time()
    for i in range(number):
        ul1000.get(randIdxArray[i])
    e = time.time()
    timeArray.append((e - s, "Unrolled LL (1000)", "get"))

    # PushLeft
    s = time.time()
    for i in range(number):
        ul1000.insert(0, randValArray[i])
    e = time.time()
    timeArray.append((e - s, "Unrolled LL (1000)", "pushLeft"))

def benchmarkLL():

    # Insert
    s = time.time()
    randIdx = random.randrange(0, idxMax)
    randVal = random.randrange(0, valMax)
    for i in range(number):
        ll.insert(randIdxArray[i], randValArray[i])
    e = time.time()
    timeArray.append((e - s, "LinkedList", "insert"))

    # Get
    s = time.time()
    randIdx = random.randrange(0, number)
    for i in range(number):
        ll.get(randIdxArray[i])
    e = time.time()
    timeArray.append((e - s, "LinkedList", "get"))

    # PushLeft
    s = time.time()
    for i in range(number):
        ll.insert(0, randValArray[i])
    e = time.time()
    timeArray.append((e - s, "LinkedList", "pushLeft"))

def benchmarkAR():

    # Insert
    s = time.time()
    randIdx = random.randrange(0, idxMax)
    randVal = random.randrange(0, valMax)
    for i in range(number):
        ar.insert(randIdxArray[i], randValArray[i])
    e = time.time()
    timeArray.append((e - s, "ArrayList", "insert"))

    # Get
    s = time.time()
    randIdx = random.randrange(0, number)
    for i in range(number):
        ar.get(randIdxArray[i])
    e = time.time()
    timeArray.append((e - s, "ArrayList", "get"))

    # PushLeft
    s = time.time()
    for i in range(number):
        ar.insert(0, randValArray[i])
    e = time.time()
    timeArray.append((e - s, "ArrayList", "pushLeft"))


for i in range(1000):
    rand = random.randrange(0, valMax)
    ul4.append(rand)
    ul100.append(rand)
    ul1000.append(rand)
    ll.append(rand)
    ar.append(rand)

# for i in range(100):
#     randIdx = random.randrange(0, idxMax)
#     randVal = random.randrange(0, valMax)
#     ul.insert(randIdx, randVal)
#     ul1000.insert(randIdx, randVal)
#     ll.insert(randIdx, randVal)
#     ar.insert(randIdx, randVal)


print("========== Verification ==========")
ul4.printArray()
#ul1000.printArray()
ll.printArray()
#ar.printArray()
verifyResult()

print("========== Benchmark ==========")

benchmarkLL()
benchmarkUL_small()
benchmarkUL_medium()
benchmarkUL_large()
benchmarkAR()

print()

for i in range(len(timeArray)):
    exp = timeArray[i]
    if i % 3 == 0:
        print('{:<18} | {:<10} | Round: {} | Time: {:.5f}'.format(exp[1], exp[2], number, exp[0]))

print()

for i in range(len(timeArray)):
    exp = timeArray[i]
    if i % 3 == 1:
        print('{:<18} | {:<10} | Round: {} | Time: {:.5f}'.format(exp[1], exp[2], number, exp[0]))

print()

for i in range(len(timeArray)):
    exp = timeArray[i]
    if i % 3 == 2:
        print('{:<18} | {:<10} | Round: {} | Time: {:.5f}'.format(exp[1], exp[2], number, exp[0]))

print()