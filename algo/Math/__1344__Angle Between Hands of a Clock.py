class Solution:
    
    # 2022/03/01
    # Math [O(1): 59%]
    def angleClock(self, hour: int, minutes: int) -> float:
        angleHour = (hour / 12 + (minutes / 60) * 1 / 12) * 360
        angleMin = minutes / 60 * 360
        angle = angleHour - angleMin
        if angle < 0:
            angle = 360 + angle
        if angle >= 180: 
            angle = 360 - angle
        return angle