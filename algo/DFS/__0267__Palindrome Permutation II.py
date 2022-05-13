class Solution:
    
    # Counter to judge + Permutation with counter 
    # [TC: O( (N/2)! * (N/2) + (N/2)! * N): 73%  / SC: O( (N/2)! * (N/2) ): 25%]
    def generatePalindromes(self, s: str) -> List[str]:
        
        def formPermutation(countMap, cur, res):
            if len(cur) == numOfChar:
                res.append(list(cur))
                return 
            for ch, count in countMap.items():
                if count == 0:
                    continue
                countMap[ch] -= 1
                formPermutation(countMap, cur + [ch] , res)
                countMap[ch] += 1
            
        countMap = collections.Counter(s)
        res = [None] * len(s)
        
        isOddChance = True
        oddChar = None
        numOfChar = len(s) // 2
        if len(s) % 2 == 0:
            for ch, count in countMap.items():
                if count % 2 == 1:
                    return []
                countMap[ch] = count // 2
        else:
            for ch, count in countMap.items():
                if count % 2 == 1:
                    oddChar = ch
                    if isOddChance:
                        isOddChance = False
                    else:
                        return []
                countMap[ch] = count // 2

        halfRes = []
        formPermutation(countMap, [], halfRes)
        res = []
        if len(s) % 2 == 0:
            for l in halfRes:
                res.append("".join(l[::-1] + l))
        else:
            for l in halfRes:
                res.append("".join(l[::-1] + [oddChar] + l))
        return res