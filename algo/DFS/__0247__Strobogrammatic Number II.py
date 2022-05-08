class Solution:
    
    # 2022/05/08 
    # DFS (backtracking) [O(N*5^(N/2)): 45% / O(N*5^(N/2)): 92%]
    def findStrobogrammatic(self, n: int) -> List[str]:
        intMap = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        
        def dfs(n, idx, cur, res):
            if n % 2 == 0:
                if idx == n // 2:
                    full = list(cur)
                    for i in reversed(cur):
                        full.append(intMap[i])
                    res.append("".join(full))
                    return 
            else:
                if idx == n // 2:
                    for middle in ["0", "1", "8"]:
                        full = list(cur)
                        full.append(middle)
                        for i in reversed(cur):
                            full.append(intMap[i])
                        res.append("".join(full))
                    return 
                
            for ni in intMap.keys():
                if idx == 0 and ni == "0":
                    continue
                dfs(n, idx+1, cur + [ni], res)
            
        res = []
        dfs(n, 0, [], res)
        
        return res
        