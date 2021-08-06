import math
MODULO = pow(10, 9
            ) + 7
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
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
                if (min(d1,d2),max(d1,d2)) in used:
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