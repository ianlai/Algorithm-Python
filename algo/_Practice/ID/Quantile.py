'''
Quintile 

Input (val, count): 
   [(7,2), (5,2), (6,2)]  //7有2個，5有2個，6有2個

--> [5, 5, 6, 6, 7, 7]

Implement kth q-Quintile  e.g. first 4  

Output: 
(q, k) = (3, 0) -> 5
(q, k) = (3, 1) -> 5 
(q, k) = (3, 2) -> 6 
(q, k) = (3, 3) -> 7 

'''
import bisect

pairs1 = [(7,2), (5,2), (6,2)] 
pairs2 = [(20,2), (10,3), (30,4)]

def preprocess(pairs):
    pairs.sort(key = lambda x: x[0])
    sums = []
    for val, count in pairs:
        if sums:
            sums.append(sums[-1] + count)
        else:
            sums.append(count)
    return sums

# accums = [2, 4, 6]
def findQuantile(q, k, accums, pairs):
    totalCount = accums[-1]
    idx = (totalCount * k // q) - 1
    print("q, k:", q, k, "->", idx)
    accumIdx = bisect.bisect(accums, idx)  #bisect_right 
    return pairs[accumIdx][0]

accums = preprocess(pairs1)
print(findQuantile(3, 0, accums, pairs1))
print(findQuantile(3, 1, accums, pairs1))
print(findQuantile(3, 2, accums, pairs1))
print(findQuantile(3, 3, accums, pairs1))


