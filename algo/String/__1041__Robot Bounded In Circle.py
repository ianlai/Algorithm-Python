class Solution:
    
    # Two layer loop [O(n2): 5%]
    def isRobotBounded(self, instructions: str) -> bool:
        
        dirIdxInit = 0 
        positionInit = (0, 0)
        dirIdxCur = 0 
        positionCur = (0, 0)
        directionList = [(0, 1), (-1, 0), (0, -1), (1, 0)]
            
        for i in range(len(instructions) * 4):
            #print(positionCur, dirIdxCur)
            if i != 0 and positionCur == positionInit and dirIdxCur == dirIdxInit:
                return True
            
            for ins in instructions: 
                if ins == "G":
                    positionCur = positionCur[0] + directionList[dirIdxCur][0], positionCur[1] + directionList[dirIdxCur][1]
                elif ins == "L":
                    dirIdxCur -= 1
                    if dirIdxCur < 0:
                        dirIdxCur += 4
                elif ins == "R":
                    dirIdxCur += 1
                    if dirIdxCur == 4:
                        dirIdxCur -= 4
                else:
                    print("Error")
        return False