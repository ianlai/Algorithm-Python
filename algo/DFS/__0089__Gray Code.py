class Solution:
    
    # DFS [O(2^n), 5%]
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return 0
        res = []
        N = pow(2, n)
        used = set([])
        
        if self.dfs(n, N, 0, res, used):
            return res
        
    def dfs(self, n, N, cur, res, used):
        
        # ---- Adding ----
        res.append(cur)
        used.add(cur)
        
        if len(res) == N:  #exit
            return True
        
        for nex in self.getNeighborList(n, cur):
            if nex in used:
                continue
            if self.dfs(n, N, nex, res, used):
                return True
            
        res.remove(cur)
        used.add(cur)
        # ---- Backtracking ----

        
    def getNeighborList(self, n, cur):
        cur10 = cur 
        cur2 = bin(cur).replace("0b", "") #transform to bin than remove prefix "0b" 
        if len(cur2) < n:
            cur2 = "".join(["0"] * (n - len(cur2))) + cur2   #padding
        
        neighborList = []
        for i in range(len(cur2)):
            if cur2[i] == "0":
                neighborList.append(int(cur2[:i] + "1" + cur2[i+1:], 2))
            elif cur2[i] == "1":
                neighborList.append(int(cur2[:i] + "0" + cur2[i+1:], 2))
        return neighborList
        