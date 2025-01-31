class Solution:
    
    # 2022/01/30
    # HashMap to count [O((N-L)L): 5%]
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        
        substringCount = collections.defaultdict(int)
        for i in range(len(s) - 10 + 1):
            substringCount[s[i:i+10]] += 1
        
        res = []
        for sub, count in substringCount.items():
            if count >= 2:
                res.append(sub)
        return res