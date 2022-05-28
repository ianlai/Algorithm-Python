class SummaryRanges:

    # 2022/03/19 
    # Use 2 OrderedDict to find whether we can merge [84%]
    # n: number of input 
    # m: number of range
    def __init__(self):
        print("Code2 - OrderedDict")
        self.sToE = collections.OrderedDict()
        self.eToS = collections.OrderedDict()
        self.used = set()

    # Insert [O(logm)]
    def addNum(self, val: int) -> None:
        #Need check (example: 1->3->2->2)
        if val in self.used:
            return 
        if val - 1 in self.eToS and val + 1 in self.sToE:
            start = self.eToS[val-1]
            end = self.sToE[val+1]
            self.sToE[start] = end
            self.eToS[end] = start
            del self.eToS[val-1]
            del self.sToE[val+1]
        elif val - 1 in self.eToS:
            start = self.eToS[val-1]
            self.eToS[val] = start
            self.sToE[start] = val
            del self.eToS[val-1]
        elif val + 1 in self.sToE:
            end = self.sToE[val+1]
            self.sToE[val] = end
            self.eToS[end] = val
            del self.sToE[val+1]
        else:
            self.sToE[val] = val
            self.eToS[val] = val
        self.used.add(val)
    
    # Return intervals with sorted result [O(m)] 
    def getIntervals(self) -> List[List[int]]:
        res = []
        for start, end in sorted(self.sToE.items()):
            res.append((start, end))
        return res
    
#=====================================================================
class SummaryRanges1:

    # 2022/03/19 
    # Use 2 maps to find whether we can merge in O(1) time [46%]
    def __init__(self):
        print("Code1 - Dict")
        #self.sToE = {}
        #self.eToS = {}
        #self.used = set()

    # Insert [O(1)]
    def addNum(self, val: int) -> None:
        #Need check (example: 1->3->2->2)
        if val in self.used:
            return 
        if val - 1 in self.eToS and val + 1 in self.sToE:
            start = self.eToS[val-1]
            end = self.sToE[val+1]
            self.sToE[start] = end
            self.eToS[end] = start
            del self.eToS[val-1]
            del self.sToE[val+1]
        elif val - 1 in self.eToS:
            start = self.eToS[val-1]
            self.eToS[val] = start
            self.sToE[start] = val
            del self.eToS[val-1]
        elif val + 1 in self.sToE:
            end = self.sToE[val+1]
            self.sToE[val] = end
            self.eToS[end] = val
            del self.sToE[val+1]
        else:
            self.sToE[val] = val
            self.eToS[val] = val
        self.used.add(val)
    
    # Return intervals with sorted result [O(mlogm), m is the range number] 
    def getIntervals(self) -> List[List[int]]:
        res = []
        for start, end in sorted(self.sToE.items()):
            res.append((start, end))
        return res
        
# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()