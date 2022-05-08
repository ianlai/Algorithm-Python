class Solution:
    # 2022/05/08 
    # DFS (backtracking); from two ends  [O(N*5^(N/2)): 45% / O(N*5^(N/2)): 92%]
    # 集中在for裡面做，因此可以少掉一些dfs函數內的判斷，但因此for迴圈內的跳出條件順序就不可互換
    def findStrobogrammatic(self, n: int) -> List[str]:
        print("Code4")
        intMap = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        
        def dfs(start, end, cur, res): 
            if start > end:
                res.append("".join(cur))
                return 
            for v1, v2 in intMap.items():
                if start == end and v1 in ["6", "9"]:
                    continue
                if start != end and start == 0 and v1 == "0":
                    continue
                    
                cur[start] = v1
                cur[end] = v2
                dfs(start + 1, end - 1, cur, res)
        res = []
        dfs(0, n - 1, [None] * n, res)
        return res
    
    
    # 2022/05/08 
    # DFS (backtracking); from two ends  [O(N*5^(N/2)): 45% / O(N*5^(N/2)): 92%]
    # 常用的backtracking都是一個一個append進cur，這邊是先把cur建好，
    # 就可以每回不只塞下一個值，也可以塞相對應的後面的值
    def findStrobogrammatic3(self, n: int) -> List[str]:
        print("Code3 (best)")
        
        intMap = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        
        def dfs(start, end, cur, res): 
            if start > end:
                res.append("".join(cur))
                return 
            if start == end:
                for v in ["0", "1", "8"]:
                    cur[start] = v
                    res.append("".join(cur))
                return 
            for v1, v2 in intMap.items():
                if start == 0 and v1 == "0":
                    continue
                cur[start] = v1
                cur[end] = v2
                dfs(start + 1, end - 1, cur, res)
        res = []
        dfs(0, n - 1, [None] * n, res)
        return res
    
    # 2022/05/08 
    # DFS (backtracking); from one end [O(N*5^(N/2)): 45% / O(N*5^(N/2)): 92%]
    def findStrobogrammatic2(self, n: int) -> List[str]:
        print("Code2")
        intMap = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        
        def dfs(idx, cur, res):
            if idx == n // 2: #arrive at the end (middle)
                if n % 2 == 1:
                    for middle in ["0", "1", "8"]:
                        full = list(cur)
                        full.append(middle)
                        for i in reversed(cur):
                            full.append(intMap[i])
                        res.append("".join(full))
                    return 
                else:
                    full = list(cur)
                    for i in reversed(cur):
                        full.append(intMap[i])
                    res.append("".join(full))
                    return  
                
            for ni in intMap.keys():
                if idx == 0 and ni == "0":
                    continue
                dfs(idx+1, cur + [ni], res)
            
        res = []
        dfs(0, [], res)
        
        return res
        
    
    # 2022/05/08 
    # DFS (backtracking) [O(N*5^(N/2)): 45% / O(N*5^(N/2)): 92%]
    def findStrobogrammatic1(self, n: int) -> List[str]:
        print("Code1")
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
        