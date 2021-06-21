class Solution:
    
    # Union Find [O(n3):29%]
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        
        n = len(isConnected)
        parents = [-1] * n
        self.count = n
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i == j:
                    continue
                if isConnected[i][j] == 0:
                    continue
                # connected case
                self.union(parents, i, j)
        return self.count
    
    def union(self, parents, A, B):
        def find(A):
            if parents[A] == -1:
                return A
            return find(parents[A])
        
        headA = find(A)
        headB = find(B)
        if headA != headB: 
            parents[headB] = headA #union
            self.count -= 1