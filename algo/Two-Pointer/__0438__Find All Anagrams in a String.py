class Solution:
    
    # 2022/01/21
    # Sliding window with count array [O(n): 12%]
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        def compareCountMap(base, compare):
            cloneBase = base + []
            res = 0
            for i, v in enumerate(compare):
                cloneBase[i] -= v
                if cloneBase[i] < 0: #s too many
                    res = -1
                    break
                elif cloneBase[i] > 0:
                    res = 1
                    break
            return res
        
        pMap = [0] * 26
        sMap = [0] * 26
        
        for c in p:
            pMap[ord(c) - ord("a")] += 1
            
        res = []
        left = 0
        for right, c in enumerate(s):
            sMap[ord(c) - ord("a")] += 1            
            status = compareCountMap(pMap, sMap) 
            while status == -1: #pMap more than sMap => reduce sMap               
                sMap[ord(s[left]) - ord("a")] -= 1
                left += 1 
                status = compareCountMap(pMap, sMap) 
            if status == 0:
                res.append(left)
            #pMap less or equal to sMap => expand sMap
        return res        