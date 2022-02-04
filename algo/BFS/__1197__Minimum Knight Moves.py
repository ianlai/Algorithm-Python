class Solution:
    
    # 2022/02/04
    # BFS [O((|x|+|y|)^2): 13%] 
    # 因為是走成一個圈，所以有很多冗余的部分。要再優化。
    def minKnightMoves(self, x: int, y: int) -> int:
        
        deq = collections.deque([(0, 0)])
        distance = collections.defaultdict(int)
        distance[(0, 0)] = 0
        skipped = 0
        while deq:
            cur_x, cur_y = deq.popleft()
            if cur_x == x and cur_y == y:
                return distance[(cur_x, cur_y)]
                
            for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                next_x, next_y = cur_x + dx, cur_y + dy
                if (next_x, next_y) in distance:
                    continue
                if abs(next_x - x) >= 2 and abs(next_y - y) >= 2 and abs(next_x - x) >= abs(cur_x - x) and abs(next_y - y) >= abs(cur_y - y):
                    continue
                deq.append((next_x, next_y))
                distance[(next_x, next_y)] = distance[(cur_x, cur_y)] + 1
        return -1