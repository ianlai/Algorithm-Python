class Solution:
    
    # 2022/04/03 Contest
    # Math [O(1): 50%]
    def convertTime(self, current: str, correct: str) -> int:
        currentInt = int(current.split(":")[0]) * 60 + int(current.split(":")[1])
        correctInt = int(correct.split(":")[0]) * 60 + int(correct.split(":")[1])
        correctInt2 = correctInt + 24 * 60
        diff = min(abs(correctInt2 - currentInt), abs(correctInt - currentInt))
        
        op = 0
        for adjust in [60, 15, 5, 1]:
            op += diff // adjust
            diff %= adjust
        return op