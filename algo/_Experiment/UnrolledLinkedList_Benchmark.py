import time
import random
from UnrolledLinkedList import UnrolledLinkedList
from LinkedList import LinkedList
from ArrayList import ArrayList

ul = UnrolledLinkedList(4)
ullarge = UnrolledLinkedList(1000)
ll = LinkedList()
ar = ArrayList()

myarray = []

def verifyResult(): 
    if ul.getArray() != ll.getArray():
        print("Verification failed (ul != ll)")
    if ul.getArray() != ar.getArray():
        print("Verification failed (ul != ar)")
    else:
        print("Verification succssfu (ul == ll == ar)")

number = 10000
def benchmarkUL_small():
    s1 = time.time()

    randIdx = random.randrange(0,50)
    randVal = random.randrange(0,100)

    for i in range(number):
        ul.insert(randIdx, randVal)
    e1 = time.time()
    print("UL-small, insert", number, ": ", e1 - s1)

    s2 = time.time()
    randIdx = random.randrange(0,number)
    for i in range(number):
        ul.get(randIdx)
    e2 = time.time()
    print("UL-small, get   ", number, ": ", e2 - s2)

def benchmarkUL_large():
    s1 = time.time()

    randIdx = random.randrange(0,50)
    randVal = random.randrange(0,100)

    for i in range(number):
        ullarge.insert(randIdx, randVal)
    e1 = time.time()
    print("UL-large, insert", number, ": ", e1 - s1)

    s2 = time.time()
    randIdx = random.randrange(0,number)
    for i in range(number):
        ullarge.get(randIdx)
    e2 = time.time()
    print("UL-large, get   ", number, ": ", e2 - s2)

def benchmarkLL():
    s1 = time.time()

    randIdx = random.randrange(0,50)
    randVal = random.randrange(0,100)

    for i in range(number):
        ll.insert(randIdx, randVal)
    e1 = time.time()
    print("LL      , insert", number, ": ", e1 - s1)


    s2 = time.time()
    randIdx = random.randrange(0,number)
    for i in range(number):
        ul.get(randIdx)
    e2 = time.time()
    print("LL      , get   ", number, ": ", e2 - s2)

def benchmarkAR():
    s1 = time.time()

    randIdx = random.randrange(0,50)
    randVal = random.randrange(0,100)

    for i in range(number):
        ar.insert(randIdx, randVal)
    e1 = time.time()
    print("AR      , insert", number, ": ", e1 - s1)


    s2 = time.time()
    randIdx = random.randrange(0,number)
    for i in range(number):
        ar.get(randIdx)
    e2 = time.time()
    print("AR      , get   ", number, ": ", e2 - s2)



for i in range(50):
    rand = random.randrange(0,100)
    ul.append(rand)
    ullarge.append(rand)
    ll.append(rand)
    ar.append(rand)

for i in range(50):
    randIdx = random.randrange(0,50)
    randVal = random.randrange(0,100)
    ul.insert(randIdx, randVal)
    ullarge.insert(randIdx, randVal)
    ll.insert(randIdx, randVal)
    ar.insert(randIdx, randVal)


print("========== Verification ==========")
ul.printArray()
ullarge.printArray()
ll.printArray()
ar.printArray()
verifyResult()

print("========== Benchmark ==========")

benchmarkUL_small()
benchmarkUL_large()
benchmarkLL()
benchmarkAR()


# ========== Benchmark ==========
# UL-small, insert 10000 :  0.04581499099731445
# UL-small, get    10000 :  3.9679510593414307
# UL-large, insert 10000 :  0.024754047393798828
# UL-large, get    10000 :  0.8472318649291992
# LL      , insert 10000 :  0.04113316535949707
# LL      , get    10000 :  25.027461767196655
# AR      , insert 10000 :  0.0367739200592041
# AR      , get    10000 :  0.0036211013793945312