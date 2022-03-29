# 2022/03/29
# One maps [55%]
class DetectSquares:
    def __init__(self):
        print("Code2")
        self.countMap = collections.defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        self.countMap[tuple(point)] += 1
        
    # Input point1
    def count(self, point: List[int]) -> int: 
        count = 0
        # (x, y) is point3 
        for x, y in self.countMap.keys():
            
            # Remove zero-size square
            if x == point[0] or y == point[1]:
                continue
                
            # Not found point2
            if (x, point[1]) not in self.countMap:
                continue
                
            # Not found point4
            if (point[0], y) not in self.countMap:
                continue
                
            # Remove non-square rectangle
            if abs(x - point[0]) != abs(y - point[1]):
                continue
            
            c1 = self.countMap[(x, y)]
            c2 = self.countMap[(x, point[1])]
            c3 = self.countMap[(point[0],y)]
            count += c1 * c2 * c3
        return count 

# ============================================
# 2022/03/29
# Two maps [55%]
class DetectSquares1:
    def __init__(self):
        print("Code1")
        self.mapx = collections.defaultdict(lambda: collections.defaultdict(int))
        self.mapy = collections.defaultdict(lambda: collections.defaultdict(int))
        
    def add(self, point: List[int]) -> None:
        self.mapx[point[0]][point[1]] += 1
        self.mapy[point[1]][point[0]] += 1
        
    def count(self, point: List[int]) -> int:
        y_arr = self.mapx[point[0]]
        x_arr = self.mapy[point[1]]
        count = 0
        for x in x_arr:
            for y in y_arr:
                # Remove non-square rectangle
                if abs(x - point[0]) != abs(y - point[1]):
                    continue
                # Remove zero-size square
                if x == point[0] or y == point[1]:
                    continue
                c1 = self.mapx[x][y]
                c2 = self.mapx[x][point[1]]
                c3 = self.mapx[point[0]][y]
                count += c1 * c2 * c3
                #print(x,y,"->", c1,c2,c3)        
        return count 


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)