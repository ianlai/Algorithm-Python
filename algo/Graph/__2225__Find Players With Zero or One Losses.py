class Solution:
    
    # 2022/04/03 Contest
    # In a graph, find the nodes with 0-indegree and 1-indegree [O(VlogV + E): 55%]
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        indegree = collections.defaultdict(int)
        nodeset = set()
        
        # Find all nodes and calculate the indegree of each node
        for v1, v2 in matches:
            nodeset.add(v1)
            nodeset.add(v2)
            indegree[v2] += 1
        
        # Form result by finding the 0-indegree and 1-indegree nodes
        res = [[] for _ in range(2)]
        for v in sorted(list(nodeset)):
            if v in indegree:
                if indegree[v] == 1:
                    res[1].append(v)
            else:
                res[0].append(v)
        return res