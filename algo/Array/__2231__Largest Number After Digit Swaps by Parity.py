class Solution:
    def largestInteger(self, num: int) -> int:
        numStr = str(num)
        even = []
        odd = []
        evenIdx = set()
        for i, v in enumerate(numStr):
            if int(v) % 2 == 0:
                even.append(v)
                evenIdx.add(i)
            else:
                odd.append(v)
        even.sort(reverse=True)
        odd.sort(reverse=True)
        res = ''
        pEven, pOdd = 0, 0
        for i in range(len(numStr)):
            if i in evenIdx:
                res += even[pEven]
                pEven += 1
            else:
                res += odd[pOdd]
                pOdd += 1
        return int(res)