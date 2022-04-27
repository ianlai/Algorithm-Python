class Solution:
    
    # 2022/04/27
    # DFS on graph [54% / 5%]
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        def dfs(i, group):
            if i in group:
                return
            group.add(i)
            for ni in graph[i]:
                dfs(ni, group)
        #graph 
        graph = collections.defaultdict(set)
        for v1, v2 in pairs:
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        #main
        visited = set()
        groupMap = {}
        for i in range(len(s)):
            if i in visited:
                continue
            group = set()
            dfs(i, group)
            visited.update(group)
            groupMap[i] = group

        #form res 
        #print(groupMap)
        res = [0] * len(s)
        for head, group in groupMap.items():
            curStr = []
            idxs = list(group)
            for idx in list(group):
                curStr.append(s[idx])
            curStr.sort(key = lambda x: x[0])
            for i, idx in enumerate(sorted(idxs)):
                res[idx] = curStr[i]
                
        return "".join(res)