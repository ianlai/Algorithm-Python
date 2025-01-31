class Solution:
    
    #2022/01/12
    #Backtracking [36%]
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        print("Code2")
        
        def isMatch(pToS, sSet, p, pi, s, si):
            #print(pToS, sSet, pi, si)
            if pi == len(p) and si == len(s):
                return True
            if si >= len(s) or pi >= len(p):
                return False
            
            if p[pi] in pToS:
                mapString = pToS[p[pi]] 
                lenMapString = len(mapString)
                if s[si:si+lenMapString] != mapString:
                    return False
                return isMatch(pToS, sSet, pattern, pi+1, s, si+lenMapString)
            
            else:
                for ns in range(si, len(s)):                    
                    mapString = s[si:ns+1]
                    if mapString in sSet:
                        continue
                    pToS[p[pi]] = mapString
                    sSet.add(mapString)
                    if isMatch(pToS, sSet, pattern, pi+1, s, ns+1):
                        return True
                    del pToS[p[pi]] #backtracking
                    sSet.remove(mapString) #backtracking
                return False
            
        pToS = {}
        sSet = set()
        return isMatch(pToS, sSet, pattern, 0, s, 0)
        
            
    # ======================================================
        
    # 2021/06/15
    def wordPatternMatch1(self, pattern: str, s: str) -> bool:
        print("Code1")
        p = pattern
        if not p and not s:
            return True
        if not p or not s:
            return False

        pToS = {}
        sSet = set()
        
        return self.wordPatternMatchImpl(p, 0, s, 0, 0, pToS, sSet)
        
    def wordPatternMatchImpl(self, p, p0, s, s0, s1, pToS, sSet):
        
        # End condition
        
        # Validate
        pCur = p[p0]
        sCur = s[s0:s1+1]
        print("p0:{} {} | s0:{} s1:{} {}".format(p0, pCur, s0, s1, sCur), pToS)
        
        if pCur in pToS:
            if pToS[pCur] != sCur:
                #print("False")
                return False
        if sCur in sSet:
            #print("False")
            return False
        

        
        if p0 == len(p) - 1 and s1 + 1 == len(s) - 1:
            print(pToS)
            print(">>>>> T")
            return True
    
        if p0 != len(p) - 1 and s1 + 1 == len(s) - 1:
            print(">>>>> F")
            return False
        
        if p0 == len(p) - 1 and s1 + 1 != len(s) - 1:
            print(">>>>> F")
            return False
        
        
        # Forward track
        #pToS[pCur] = sCur
        #sSet.add(sCur)
        
        # Next round
        #p0_next = p0 + 1 
        s0_next = s1 + 1
        for p0_next in range(p0, len(p)):
            for s1_next in range(s0_next, len(s)):
                p_next = p[p0_next]
                s_next = s[s0_next:s1_next+1]
                pToS[p_next] = s_next
                sSet.add(s_next)
                if self.wordPatternMatchImpl(p, p0_next, s, s0_next, s1_next, pToS, sSet):
                    # print("True p0:{} s0:{} s1:{}".format(p0_next, s0_next, s1_next))
                    return True
                del pToS[p_next] 
                sSet.remove(s_next)
        
        # Backtrack
        # del pToS[pCur] 
        # sSet.remove(sCur)
        
        return False        