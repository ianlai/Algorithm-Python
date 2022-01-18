import math
MODULO = pow(10, 9) + 7

class Solution:

    #2022/01/18 
    # Hashmap Two-Sum extended [O(K+P): 33%]
    def countPairs(self, deliciousness: List[int]) -> int:
        print("Code2")
        def combination(n, a):
            assert n >= a
            #return int(math.factorial(n) / math.factorial(a) / math.factorial(n-a)) #incorrect!
            return int(math.factorial(n) / math.factorial(n-a) / math.factorial(a))  #correct!
        powerList = list()
        
        maxVal = max(deliciousness)
        for i in range(22): 
            powerList.append(2**i)
        #print(powerList)
        
        countMap = collections.defaultdict(int)
        for d in deliciousness:
            countMap[d] += 1
        #print(countMap)
        
        used = set()
        totalCount = 0
        for d1 in countMap.keys():
            for p in powerList:
                d2 = p - d1
                if d2 < 0:
                    continue
                if (min(d1, d2), max(d1, d2)) in used:
                    continue
                count = 0
                if d1 == d2:
                    val = countMap[d1]
                    if val < 2:
                        continue
                    else:
                        count = combination(val, 2) % MODULO
                else:
                    if d2 in countMap:
                        count = countMap[d1] * countMap[d2] % MODULO
                used.add((min(d1,d2),max(d1,d2)))
                #print(d1, d2, count)
                totalCount += count 
        return totalCount
            
            
    # ===============================================
    
    # 2021/08/06 [33%]
    def countPairs1(self, deliciousness: List[int]) -> int:
        print("Code1")
        maxVal = max(deliciousness)
        powerValSet = set()
        upper = math.floor(math.log(maxVal*2, 2)) +1
        #print(math.floor(math.sqrt(maxVal*2)))
        for i in range(0, upper):
            powerValSet.add(2**i)
        # print(sorted(deliciousness))
        # print(sorted(powerValSet))
        
        #count
        count = collections.defaultdict(int)
        for d in deliciousness:
            count[d] += 1
            
        # print(count)
        
        used = set()
        res = 0
        for d1 in count.keys():
            for p in powerValSet:
                d2 = p - d1
                if (min(d1,d2), max(d1,d2)) in used:
                    continue
                if d1 == d2:
                    # print("ddddddd")
                    # print("d1:", d1, count[d1])
                    # print("d2:", d2, count[d2])

                    if count[d1] >= 2:
                        n = count[d1]
                        res += int(math.factorial(n) / math.factorial(n-2) / 2) % MODULO  #nC2
                        used.add((min(d1,d2),max(d1,d2)))
                        # print("added:", count[d1], "res:", res)
                        # print()
                    break
                        
                if d2 in count:
                    res += count[d1] * count[d2] % MODULO 
                    # print("d1:", d1, count[d1])
                    # print("d2:", d2, count[d2])
                    # print("added:", count[d1], "res:", res)
                    # print()
                    used.add((min(d1,d2),max(d1,d2)))
                    
        return res