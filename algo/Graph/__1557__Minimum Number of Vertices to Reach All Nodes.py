class Solution:
    
    # Find all indegree 0 nodes [O(V+E): 55%]
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegreeMap = collections.defaultdict(int)
        for v1, v2 in edges:
            indegreeMap[v2] += 1
        res = []
        for i in range(n):
            if indegreeMap[i] == 0:
                res.append(i)
        return res