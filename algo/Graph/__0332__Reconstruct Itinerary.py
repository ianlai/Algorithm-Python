import heapq
class Solution:
    
    # Backtracking; finish all edges (not nodes) [O(V+E): 38%]
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []
        
        self.numRemainingTickets = 0
        srcToDsts, srcToUseds = self.parse(tickets)
        print(srcToDsts)
        path = ["JFK"]
        self.traverse(srcToDsts, srcToUseds, "JFK", path)
        return path
        
    def parse(self, tickets):
        
        srcToDsts = collections.defaultdict(list)  #JFK -> [SFO, ATL]
        srcToUseds = collections.defaultdict(list) #JFK -> [used, unused]
        
        for src, dst in tickets:  
            if len(srcToDsts[src]) == 0:
                srcToDsts[src].append(dst)
                srcToUseds[src].append(False)
            else:   #keep the lexical order
                isAdded = False
                for i in range(len(srcToDsts[src])):
                    if dst < srcToDsts[src][0] or (i > 0 and srcToDsts[src][i-1] <= dst < srcToDsts[src][i]):
                        srcToDsts[src].insert(i, dst)
                        srcToUseds[src].insert(i, False)
                        isAdded = True
                        break
                        
                if not isAdded:
                    srcToDsts[src].append(dst)
                    srcToUseds[src].append(False)     
            self.numRemainingTickets += 1
        
        return srcToDsts, srcToUseds
    
    def traverse(self, srcToDsts, srcToUseds, src, path):
        if self.numRemainingTickets == 0:
            #print(src, path, self.numRemainingTickets, "###")
            return True
        
        size = len(srcToDsts[src])
        for i in range(size):
            if srcToUseds[src][i]:
                continue

            dst = srcToDsts[src][i]
            srcToUseds[src][i] = True
            path.append(dst)

            self.numRemainingTickets -= 1
            if self.traverse(srcToDsts, srcToUseds, dst, path):
                return True
            
            #path.remove(dst) #remove first one 
            idx = path[::-1].index(dst)  
            path.pop(len(path) - idx - 1)  #remove last one
            
            srcToUseds[src][i] = False
            self.numRemainingTickets += 1