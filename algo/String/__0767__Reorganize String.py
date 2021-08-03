class Solution:
    
    # Linearly get the max count (except itself)  [O(s*26): 22%]
    # We can try to use heap to improve it
    def reorganizeString(self, s: str) -> str:
        
        countMap = collections.defaultdict(int)
        for c in s:
            countMap[c] += 1
        
        res = [0]
        
        for i in range(len(s)):
            c1, c2 = self.getTwoMax(countMap)
            if c1 == res[-1]:
                new = c2
            else:
                new = c1
            if new:
                res.append(new)
                countMap[new] -= 1
        
        print(res) 
        if len(res) - 1 == len(s): 
             return "".join(res[1:])
        return ""
    
    def getTwoMax(self, m):
        max1 = 0
        c1 = None
        max2 = 0
        c2 = None
        for key in m.keys():
            if m[key] > max1:
                max1 = m[key]
                c1 = key
                
        for key in m.keys():
            if key == c1:
                continue
            if m[key] > max2:
                max2 = m[key]
                c2 = key
        return c1, c2
        
            