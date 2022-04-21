class Solution:
    
    # 2022/04/21
    # Two pointer [O(N): 49%]
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        
        # Check the order of LR
        removedStart = ""
        for ch in start:
            if ch != "X":
                removedStart += ch
        
        removedEnd = ""
        for ch in end:
            if ch != "X":
                removedEnd += ch
        if removedStart != removedEnd:
            return False
        
        # Check the positions of LR
        lStart, rStart = [], []
        for i, ch in enumerate(start):
            if ch == "L":
                lStart.append(i)
            if ch == "R":
                rStart.append(i)
                
        lStart = lStart[::-1]
        rStart = rStart[::-1]
        for i, ch in enumerate(end):
            if ch == "L":
                if i > lStart.pop():
                    return False
            if ch == "R":
                if i < rStart.pop():
                    return False
        return True
            