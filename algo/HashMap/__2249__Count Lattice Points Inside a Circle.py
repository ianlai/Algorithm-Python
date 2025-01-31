class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        
        s = set()
        for x, y, mc in circles:
            s.add((x, y))
            for nx in range(x-mc+1, x+mc):
                for ny in range(y-mc+1, y+mc):
                    if (nx, ny) in s:
                        continue
                    if (nx - x) ** 2 + (ny - y) ** 2 <= mc ** 2:        
                        s.add((nx, ny))

            for nx, ny in [(x, y+mc), (x, y-mc), (x+mc, y), (x-mc, y)]:
                s.add((nx, ny))
        
        return len(s)