"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

# 2021/11/14
# DFS [72%]  
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        #preprocess to form the map (id -> employee)
        self.idToEmployee = {}
        for e in employees:
            self.idToEmployee[e.id] = e
        return self.getImportanceAll(id)
            
    def getImportanceAll(self, eid):
        e = self.idToEmployee[eid]
        importance = e.importance
        for sid in e.subordinates:
            importance += self.getImportanceAll(sid)
        return importance
            
# =================================================
# 2021/08/06
# DFS [87%]  
class Solution1:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if not employees:
            return 0
        
        emap = collections.defaultdict(list)
        for e in employees:
            eid = e.id
            ei = e.importance
            es = e.subordinates
            emap[eid] = [ei, es]
        
        self.importance = 0
        self.calculate(emap, id)
        return self.importance
            
    def calculate(self, emap, id):
        imp, sub = emap[id][0], emap[id][1]
        self.importance += imp
        for eid in sub:
            self.calculate(emap, eid)