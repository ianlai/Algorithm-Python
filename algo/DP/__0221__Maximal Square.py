DEBUG = False
class Solution:
    
    # Buttom-Up DP [time:O(mn), 36% / space: O(mn), 10%]
    def maximalSquare(self, matrix: List[List[str]]) -> int:            
        if not matrix:
            return 
        m, n = len(matrix), len(matrix[0])
        print("MT:")
        self.printDebug(matrix)
        # HC = self.getHC(matrix, m, n)  
        # VC = self.getVC(matrix, m, n)
        
        HC, VC, FC = self.getHCVCFC(matrix, m, n)
        #FC = self.getFC(matrix, HC, VC, m, n) 
        
        return FC * FC
    def getHCVCFC(self, M, m, n):
        HC = [[0 for _ in range(n)] for _ in range(m)]
        VC = [[0 for _ in range(n)] for _ in range(m)]
        FC = [[0 for _ in range(n)] for _ in range(m)]
        
        maxFC = 0
        for i in range(n):
            if M[0][i] == "1":
                FC[0][i] = 1
                maxFC = max(maxFC, FC[0][i])
        for i in range(m):
            if M[i][0] == "1":
                FC[i][0] = 1
                maxFC = max(maxFC, FC[i][0])
    
        for i in range(m):
            for j in range(n):
                if M[i][j] == "1":
                    VC[i][j] = VC[i-1][j] + 1
                    HC[i][j] = HC[i][j-1] + 1
                    if i and j:
                        FC[i][j] = min(HC[i][j-1], FC[i-1][j-1], VC[i-1][j]) + 1
                        maxFC = max(maxFC, FC[i][j])
        return HC, VC, maxFC
    
    def getHC(self, M, m, n):
        HC = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if M[i][j] == "0":
                    HC[i][j] = 0
                else:
                    HC[i][j] = HC[i][j-1] + 1
        return HC
                    
    def getVC(self, M, m, n):
        VC = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if M[i][j] == "0":
                    VC[i][j] = 0
                else:
                    VC[i][j] = VC[i-1][j] + 1
        return VC
    
    def getFC(self, M, HC, VC, m, n):
        print("HC:")
        self.printDebug(HC)
        print("VC:")
        self.printDebug(VC)
        FC = [[0 for _ in range(n)] for _ in range(m)]
        
        maxFC = 0
        for i in range(n):
            if M[0][i] == "1":
                FC[0][i] = 1
                maxFC = max(maxFC, FC[0][i])
        for i in range(m):
            if M[i][0] == "1":
                FC[i][0] = 1
                maxFC = max(maxFC, FC[i][0])
        
        for i in range(1, m):
            for j in range(1, n):
                if M[i][j] == "0":
                    FC[i][j] = 0
                else:
                    FC[i][j] = min(HC[i][j-1], FC[i-1][j-1], VC[i-1][j]) + 1
                    maxFC = max(maxFC, FC[i][j])
        print("FC:")
        self.printDebug(FC)
        
        return maxFC
    def printDebug(self, A):
        if not DEBUG:
            return 
        
        m, n = len(A), len(A[0])
        for i in range(m):
            print([int(a) for a in A[i]])
            
    # =============================================
    # BFS [TLE]
    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        maxLayer = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                layer = self.bfs(matrix, i, j)
                maxLayer = max(layer, maxLayer)
        #print("MAX:", maxLayer)
        return maxLayer * maxLayer
                
    def bfs(self, matrix, si, sj):
        m, n = len(matrix), len(matrix[0])
        layer = 1 
        deq = collections.deque([(si, sj)])
        visited = [ [0 for _ in range(n)] for _ in range(m)]
        
        while deq:
            #print(si, sj, deq)
            layer += 1
            isSquare = True
            
            for _ in range(len(deq)):
                (i, j) = deq.popleft()
                visited[i][j] = 1
                #print("  ", i, j, "count:", count)
                
                for di, dj in [(0, 1), (1, 0), (1, 1)]:
                    ni = i + di
                    nj = j + dj
                    #print("   ni, nj: ", ni, nj)
                    if not (0 <= ni < m and 0 <= nj < n):
                        #print("   RRR", ni, nj, "OOB")
                        #return 
                        isSquare = False
                        #break
                        return layer - 1 
                    if matrix[ni][nj] == "0":
                        #print("   RRR", ni, nj, "matrix == 0")
                        #return
                        isSquare = False
                        #break
                        return layer -1 
                    if visited[ni][nj] == 1:
                        continue
                    #print(ni, nj, "appended")
                    deq.append((ni, nj))
            #print(si, sj, "level:", layer, isSquare )
            if not isSquare:
                return layer - 1
                