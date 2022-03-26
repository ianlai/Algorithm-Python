class Solution:
    
    # 2022/03/26
    # Greedyly select the smallest and check the remaining strings are after it (iteration) [O(26^s): 5%]
    def removeDuplicateLetters(self, s: str) -> str:
        print("Code3")
        alpha = "abcdefghijklmnopqrstuvwxyz"
        done = [True] * 26
        alphaIndex = [[] for _ in range(26)]
        for i, c in enumerate(s):
            alphaIndex[ord(c) - ord('a')].append(i)
            done[ord(c) - ord('a')] = False
            
        #print("alphaIndex:", alphaIndex)
        #print("done:", done)
        
        res = []
        curIdx = 0
        #print(done)
        while not all(done):
            for i in range(26):
                if done[i]:
                    continue
                #print("i ->", alpha[i], res, alphaIndex[i])
                startFromA = False
                for idx in alphaIndex[i]:
                    isFail = False
                    if res and idx < res[-1][1]:
                        continue
                        
                    #When i is chosen, and then curIdx is chosen
                    #Make sure all other undone chars are there after curIdx
                    for j in range(26):
                        if j == i:
                            continue
                        if done[j]:
                            continue
                        #print(alpha[i], "-----", alpha[j])
                        if alphaIndex[j][-1] < idx:
                            #print("Failed:", alpha[i], idx, "-", alpha[j], alphaIndex[j][-1])
                            isFail = True
                            break 
                    if isFail:
                        continue
                    else:
                        #print("Success:", alpha[i], idx)
                        res.append((alpha[i], idx))
                        done[i] = True
                        startFromA = True
                        break
                if startFromA:
                    break
                #print(done)

        resString = ""
        for alpha, _ in res:
            resString += alpha
        return resString
    
    # =======================================

    # 2022/02/14
    # Incorrect 
    def removeDuplicateLetters2(self, s: str) -> str:
        print("Code2")
        charCounter = collections.defaultdict(int)
        for c in s:
            charCounter[c] += 1
        
        def helper(charCounter, s):
            if len(s) == 0:
                return ""
            idx = 0
            for i, c in enumerate(s):
                if s[i] < s[idx]:
                    idx = i
                charCounter[c] -= 1
                if charCounter[c] == 0:
                    return s[idx] + helper(charCounter, s[idx:].replace(s[idx], ''))
        res = helper(charCounter,s)
        print(res)    
        return res
            
    
    # =======================================
    # Incorrect 
    def removeDuplicateLetters1(self, s: str) -> str:
        print("Code1")
        stack = []
        res = []
        used = set()
        for c in s: 
            while stack and c > stack[-1]:
                tail = stack.pop()
                if tail in res:
                    continue
                res.append(tail)
            stack.append(c)
            print()
        while stack:
            tail = stack.pop()
            if tail in res:
                continue
            res.append(tail)
        return ''.join(res)
    
#         32134323        
#         cbdcacbc
#         a 4
#         b 1 6
#         c 0 3 5 7
#         d 2 
