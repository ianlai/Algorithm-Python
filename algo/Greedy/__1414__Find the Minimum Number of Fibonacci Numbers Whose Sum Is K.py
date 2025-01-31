class Solution:

    # 2022/03/09
    # Greedy [O(n): 27%] 
    def findMinFibonacciNumbers(self, k: int) -> int:
        print("Code2")
        
        #Generate fib list
        def generateFibList(k):
            fibs = [1, 1]
            cur = fibs[-1] + fibs[-2]
            while cur <= k:
                fibs.append(cur)
                cur = fibs[-1] + fibs[-2]
            return fibs[1:]
        fibs = generateFibList(k)  #sorted ascending  
        print(fibs)
        
        #Greedy to deduct by the largest one
        count = 0
        while k > 0:
            k -= fibs.pop()
            count += 1
            while fibs and k < fibs[-1]:
                fibs.pop()
        return count
        
    # =======================================
    # 2022/03/09
    # DFS [TLE]
    def findMinFibonacciNumbers1(self, k: int) -> int:
        print("Code1")
        def generateFibList(k):
            fibs = [0, 1]
            for i in range(k):
                cur = fibs[-1] + fibs[-2]
                if cur <= k:
                    fibs.append(cur)
            return fibs[::-1][:-2]
        
        def dfs(fibs, k, idx, cur):
            if k < 0:
                return inf
            if k == 0:
                return len(cur)
            for i in range(idx, len(fibs)):
                res = dfs(fibs, k - fibs[i], i, cur + [fibs[i]])
                if res != inf:  #prune 
                    return res
                
        fibs = generateFibList(k)  #sorted descending   
        return dfs(fibs, k, 0, [])
    
    