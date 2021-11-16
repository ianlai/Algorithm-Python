# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    # [[1,1,0],[0,1,0],[1,1,1]]
    # [[1,0,1],[1,1,0],[0,1,1]]
    # [[1,1,1],[1,1,0],[0,0,1]]
    
    # Two-Pointer [O(n): 78%]
    def findCelebrity(self, n: int) -> int:
        print("Method-4")
        
        # Find a celebrity candidate
        left, right = 0, n - 1
        while left < right: 
            if knows(left, right):
                left += 1
            else:
                right -= 1
                
        # Verify whether that candiate is really a celebrity
        for i in range(n):
            if i != right and not knows(i, right):
                return -1
            if i != right and knows(right, i):
                return -1
        return right 
    # ============================================    

    # Two-Pointer + BFS [TLE]
    def findCelebrity3(self, n: int) -> int:
        print("Method-3")
        
        def printx(arr):
            print(["o" if n == True else "x" for n in arr])
        
        src = [True] * n 
        dst = [True] * n 
        s, d = 0, 0
        deq = collections.deque([(s, d)])
        visited = set((s, d))
        
        while deq:
            s, d = deq.popleft()
            #print(s, d)
            #pre = src.count(True) + dst.count(True)
            if s == n: 
                s -= n
            if d == n:
                d -= n
            if s == d:
                if (s+1, d) not in visited:
                    deq.append([s+1, d])
                    visited.add((s+1, d))
                if (s, d+1) not in visited:
                    deq.append([s, d+1])
                    visited.add((s, d+1))
                continue
                
            if knows(s, d):
                src[s] = False
                if (s+1, d) not in visited:
                    deq.append([s+1, d])
                    visited.add((s+1, d))
            else: 
                dst[d] = False
                if (s, d+1) not in visited:
                    deq.append([s, d+1])
                    visited.add((s, d+1))
            
            #printx(src)
            #printx(dst)
            #cur = src.count(True) + dst.count(True)
            # if pre == cur:
            #     break
            sCount = src.count(True) 
            dCount = dst.count(True) 
            if sCount == 0:
                return -1
            if dCount == 0:
                return -1
                
        if sCount == 1 and dCount == 1:
            return src.index(True)
        return -1
    
    # ============================================
    
    # Double Loop [TLE]
    def findCelebrity2(self, n: int) -> int:
        print("Method-2")
        src = [True] * n 
        dst = [True] * n 
        srcCount = n
        dstCount = n
        
        for i in range(n):
            # if src[i] == False:
            #     continue
            for j in range(n):
                if i == j:
                    continue
                # if dst[j] == False:
                #     continue
                if knows(i, j):  # i knows j
                    if src[i] == True:
                        src[i] = False
                        srcCount -= 1
                else:            # i doesn't know j 
                    if dst[j] == True:
                        dst[j] = False
                        dstCount -= 1
                #print(i, j, src, dst, srcCount, dstCount)
                if srcCount == 0 or dstCount == 0:
                    return -1
        if srcCount == 1 and dstCount == 1 and src.index(True) == dst.index(True):
            return src.index(True)
        return  -1          
        
    # ============================================
    # Wrong
    def findCelebrity1(self, n: int) -> int:
        celebrities = [True] * n 
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if celebrities[j] == False:
                    continue
                if knows(i, j):  # i knows j
                    celebrities[i] = False
                else:            # i doesn't know j 
                    celebrities[j] = False
                
                if celebrities.count(True) == 0:
                    return -1
        
        for i, v in enumerate(celebrities):
            if v:
                return i
        return -1