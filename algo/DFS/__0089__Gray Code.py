class Solution:
    
    # 2021/12/05
    # Backtracking [O(n*2^n), 5%]
    def grayCode(self, n: int) -> List[int]:
        print("Code-2")
        if n == 0:
            return 0
        
        N = 2 ** n
        resBin = []
        res = []
        used = set()
        zeroBin = tuple([0] * n)
        
        self.dfs(n, N, zeroBin, resBin, used)
        for num in resBin:
            numBin = ""
            for n in num:
                numBin += str(n)
            res.append(int(numBin, 2))
        return res
        
    def dfs(self, n, N, cur, res, used):
        res.append(cur)
        used.add(cur)
        if len(res) == N:  #exit
            return True
        for nex in self.getNeighborList(n, cur):
            if nex in used:
                continue
            if self.dfs(n, N, nex, res, used):
                return True
            else:
                return False
        res.remove(cur)
        used.add(cur)
        return False

    def getNeighborList(self, n, cur):        
        neighborList = []
        for i in range(n):
            neighbor = list(cur)
            if cur[i] == 0:
                neighbor[i] = 1
            elif cur[i] == 1:
                neighbor[i] = 0
            neighborList.append(tuple(neighbor)) 
        return neighborList
            
    # ==========================================================    
    # 2021/07/02
    # DFS [O(2^n), 5%]
    def grayCode1(self, n: int) -> List[int]:
        print("Code-1")
        if n == 0:
            return 0
        res = []
        N = pow(2, n)
        used = set([])
        
        if self.dfs1(n, N, 0, res, used):
            return res
        
    def dfs1(self, n, N, cur, res, used):
        
        # ---- Adding ----
        res.append(cur)
        used.add(cur)
        
        if len(res) == N:  #exit
            return True
        
        for nex in self.getNeighborList1(n, cur):
            if nex in used:
                continue
            if self.dfs1(n, N, nex, res, used):
                return True
            
        res.remove(cur)
        used.add(cur)
        # ---- Backtracking ----

        
    def getNeighborList1(self, n, cur):
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
        