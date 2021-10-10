# https://leetcode.com/problems/open-the-lock/
class Solution:
    
    # BFS [O(n): 20%]
    def openLock(self, deadends: List[str], target: str) -> int:
        
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
        