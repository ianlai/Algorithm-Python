class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        isCollide = True
        while isCollide:
            res = []
            isCollide = False
            #print(asteroids)
            for idx, asteroid in enumerate(asteroids):
                if len(res) > 0:
                    if res[-1] > 0 and asteroid < 0:
                        isCollide = True
                        if abs(res[-1]) > abs(asteroid):
                            continue
                        elif abs(res[-1]) < abs(asteroid): 
                            res.pop()
                            res.append(asteroid)
                        else:
                            res.pop()
                    else:
                        res.append(asteroid)
                else:
                    res.append(asteroid)
            asteroids = res
        return res
