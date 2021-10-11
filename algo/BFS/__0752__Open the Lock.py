# https://leetcode.com/problems/open-the-lock/
class Solution:
    
    def openLock(self, deadends: List[str], target: str) -> int:
        print("Method-2b: String + improvement")
        deadends = set(deadends)
        start = "0000"
        distance = {start: 0}
        nextMap = {
            "0": ["1", "9"],
            "1": ["2", "0"],
            "2": ["3", "1"],
            "3": ["4", "2"],
            "4": ["5", "3"],
            "5": ["6", "4"],
            "6": ["7", "5"],
            "7": ["8", "6"],
            "8": ["9", "7"],
            "9": ["0", "8"],            
        }
        deq = collections.deque([start])
        while deq:
            curTry = deq.popleft()
            if curTry in deadends:
                continue
            if curTry == target:
                return distance[curTry]
            for idx, val in enumerate(curTry):
                for nextVal in nextMap[val]:
                    nextTry = curTry[:idx] + nextVal + curTry[idx+1:]
                    if nextTry not in distance:
                        deq.append(nextTry)
                        distance[nextTry] = distance[curTry] + 1
        return -1
      
    # =========================================
    
    # BFS, tuple and int [O(n): 42%]
    def openLock3(self, deadends: List[str], target: str) -> int:
        print("Method-3: Tuple and Int")
        
        deadends = set([tuple([int(e) for e in deadend]) for deadend in deadends])
        start = tuple([0, 0, 0, 0])
        visited = set(start)
        distance = {start: 0}
        deq = collections.deque([start])
        targetTuple = tuple([int(e) for e in target])

        while deq:
            curTry = deq.popleft()
            if curTry in deadends:
                continue
            if curTry == targetTuple:
                return distance[curTry]
                
            for idx, val in enumerate(curTry):
                val1 = val + 1 if val + 1 <= 9 else 0
                val2 = val - 1 if val - 1 >= 0 else 9
                
                # Drawback of tuple: doesn't support assignment function
                nextTry1 = tuple(list(curTry[:idx]) + [val1] + list(curTry[idx+1:]))
                nextTry2 = tuple(list(curTry[:idx]) + [val2] + list(curTry[idx+1:]))

                if nextTry1 not in visited:
                    deq.append(nextTry1)
                    visited.add(nextTry1)
                    distance[nextTry1] = distance[curTry] + 1
                if nextTry2 not in visited:
                    deq.append(nextTry2)
                    visited.add(nextTry2)
                    distance[nextTry2] = distance[curTry] + 1
        return -1
    
    # =========================================
    
    # BFS, only use string (convert to int)   [O(n): 80%]
    # BFS, only use string (use a string map) [O(n): 90%]
    def openLock2(self, deadends: List[str], target: str) -> int:
        
        print("Method-2: String")
        deadends = set(deadends)
        start = "0000"
        visited = set(start)
        distance = {start: 0}
        nextMap = {
            "0": ["1", "9"],
            "1": ["2", "0"],
            "2": ["3", "1"],
            "3": ["4", "2"],
            "4": ["5", "3"],
            "5": ["6", "4"],
            "6": ["7", "5"],
            "7": ["8", "6"],
            "8": ["9", "7"],
            "9": ["0", "8"],            
        }
        deq = collections.deque([start])
        while deq:
            
            curTry = deq.popleft()
            if curTry in deadends:
                continue
            if curTry == target:
                return distance[curTry]
            for idx, val in enumerate(curTry):
                
                # Conversion parts
                #val = int(val)
                #val1 = val + 1 if val + 1 <= 9 else 0
                #val2 = val - 1 if val - 1 >= 0 else 9
                val1, val2 = nextMap[val][0], nextMap[val][1]

                # Drawback of string: doesn't support assignment function
                nextTry1 = curTry[:idx] + str(val1) + curTry[idx+1:]
                nextTry2 = curTry[:idx] + str(val2) + curTry[idx+1:]
                #nextTry1[idx], nextTry2[idx] = val1, val2 

                if nextTry1 not in visited:
                    deq.append(nextTry1)
                    visited.add(nextTry1)
                    distance[nextTry1] = distance[curTry] + 1
                if nextTry2 not in visited:
                    deq.append(nextTry2)
                    visited.add(nextTry2)
                    distance[nextTry2] = distance[curTry] + 1
        return -1
    
    # =========================================
    # BFS, mix with string and list [O(n): 20%]
    def openLock1(self, deadends: List[str], target: str) -> int:
        print("Method-1")
        deadends = set(deadends)
        start = [0, 0, 0, 0]
        startStr = "".join([str(e) for e in start])
        visited = set(startStr)
        distance = {startStr: 0}
        
        deq = collections.deque([start])
        while deq:
            curTry = deq.popleft()
            curTryStr =  "".join([str(e) for e in curTry])
            if curTryStr in deadends:
                continue
            if curTryStr == target:
                return distance[curTryStr]
                
            for idx, val in enumerate(curTry):
                val1 = val + 1 if val + 1 <= 9 else 0
                val2 = val - 1 if val - 1 >= 0 else 9
                nextTry1, nextTry2 = list(curTry), list(curTry)
                nextTry1[idx], nextTry2[idx] = val1, val2
                nextTryStr1 = "".join([str(e) for e in nextTry1])
                nextTryStr2 = "".join([str(e) for e in nextTry2])
                if nextTryStr1 not in visited:
                    deq.append(nextTry1)
                    visited.add(nextTryStr1)
                    distance[nextTryStr1] = distance[curTryStr] + 1
                if nextTryStr2 not in visited:
                    deq.append(nextTry2)
                    visited.add(nextTryStr2)
                    distance[nextTryStr2] = distance[curTryStr] + 1
        return -1
        