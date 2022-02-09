class Solution:
    
    # 2022/02/09
    # 雙向BFS + pruning (小於-2的不要) [O((|x|+|y|)^2): 67%]
    def minKnightMoves(self, x: int, y: int) -> int:
        print("Code3")
        if x == 0 and y == 0:
            return 0
        if x < 0: x = -x 
        if y < 0: y = -y
        
        offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        deq_s = collections.deque([(0, 0)])
        deq_d = collections.deque([(x, y)])
        distance_s = collections.defaultdict(int)
        distance_d = collections.defaultdict(int)
        while True:
            s = deq_s.popleft()
            d = deq_d.popleft()
            
            if (s[0], s[1]) in distance_d:
                return distance_s[(s[0], s[1])] + distance_d[(s[0], s[1])]
            if (d[0], d[1]) in distance_s:
                return distance_s[(d[0], d[1])] + distance_d[(d[0], d[1])]
            
            for offset_x, offset_y in offsets:
                next_x, next_y = s[0] + offset_x, s[1] + offset_y 
                if (next_x, next_y) in distance_s:
                    continue
                if next_x < -2 or next_y < -2:
                    continue
                deq_s.append((next_x, next_y))
                distance_s[(next_x, next_y)] = distance_s[(s[0], s[1])] + 1
                
            for offset_x, offset_y in offsets:
                next_x, next_y = d[0] + offset_x, d[1] + offset_y 
                if (next_x, next_y) in distance_d:
                    continue
                if next_x < -2 or next_y < -2:
                    continue
                deq_d.append((next_x, next_y))
                distance_d[(next_x, next_y)] = distance_d[(d[0], d[1])] + 1
    
    # ==============================================
    # 2022/02/09
    # 雙向BFS [O((|x|+|y|)^2): 49%]
    def minKnightMoves2(self, x: int, y: int) -> int:
        print("Code2")
        if x == 0 and y == 0:
            return 0
        
        offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        deq_s = collections.deque([(0, 0)])
        deq_d = collections.deque([(x, y)])
        distance_s = collections.defaultdict(int)
        distance_d = collections.defaultdict(int)
        while True:
            s = deq_s.popleft()
            d = deq_d.popleft()
            
            if (s[0], s[1]) in distance_d:
                return distance_s[(s[0], s[1])] + distance_d[(s[0], s[1])]
            if (d[0], d[1]) in distance_s:
                return distance_s[(d[0], d[1])] + distance_d[(d[0], d[1])]
            
            for offset_x, offset_y in offsets:
                next_x, next_y = s[0] + offset_x, s[1] + offset_y 
                if (next_x, next_y) in distance_s:
                    continue
                deq_s.append((next_x, next_y))
                distance_s[(next_x, next_y)] = distance_s[(s[0], s[1])] + 1
                
            for offset_x, offset_y in offsets:
                next_x, next_y = d[0] + offset_x, d[1] + offset_y 
                if (next_x, next_y) in distance_d:
                    continue
                deq_d.append((next_x, next_y))
                distance_d[(next_x, next_y)] = distance_d[(d[0], d[1])] + 1
        
    # ==============================================
    # 2022/02/04
    # 單向 BFS [O((|x|+|y|)^2): 13%] 
    # 因為是走成一個圈，所以有很多冗余的部分。要再優化。
    def minKnightMoves1(self, x: int, y: int) -> int:
        print("Code1")
        
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