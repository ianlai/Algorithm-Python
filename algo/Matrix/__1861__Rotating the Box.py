class Solution:
    
    # 2022/06/02
    # Matrix manipulation [O(MN): 45% / O(MN): 23%]
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        def dropToRight(box):
            newBox = [["."] * len(box[0]) for _ in range(len(box))]
            
            for i in range(len(box)):
                count = 0
                for j in range(len(box[0])):
                    if box[i][j] == "*":
                        newBox[i][j] = "*"
                        for k in range(count):
                            newBox[i][j-k-1] = "#"
                        count = 0
                    elif box[i][j] == "#":
                        count += 1
                        
                if count != 0:
                    for k in range(count):
                        newBox[i][j-k] = "#"
                    count = 0
            return newBox
                    
        def transpose(box):
            newBox = [[0] * len(box) for _ in range(len(box[0]))]
            for i in range(len(box)):
                for j in range(len(box[0])):
                    newBox[j][len(box) - 1 - i] = box[i][j]
            return newBox
            
        droppedBox = dropToRight(box)
        transposedBox = transpose(droppedBox)
        return transposedBox 