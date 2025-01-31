class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        size = n * n 

        intToXy = {}
        for i in range(size):
            x = i // n            
            y = i % n
            if x % 2 == 1:
                y = n - y - 1
            x = n - x - 1 #calculate this last
            intToXy[i+1] = (x, y)
            
        deq = collections.deque([1])
        distance = collections.defaultdict(int)
        distance[1] = 0
        
        while deq:
            cur = deq.popleft()
            for i in range(6):
                nxt = cur + i + 1 
                if nxt > size:
                    continue
                    
                #Change to new point (not record the old point)
                #x, y = intToXy(nxt)
                x, y = intToXy[nxt]
                if board[x][y] != -1:
                    nxt = board[x][y]
                    
                #Record the point (either original or new point, not included old point)
                if nxt in distance:
                    continue 
                distance[nxt] = distance[cur] + 1
                deq.append(nxt)
                
                #Prune 
                if nxt == size:
                    return distance[size]
                
        #print(distance) 
        return -1