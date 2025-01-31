class Solution:
    
    # Greedy [O(n): 22%]
    # Find the index which accumulated gas-cost will be min, then the next idx is the candidate
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remaining = [0] * len(gas)
        for i in range(len(gas)):
            remaining[i] = gas[i] - cost[i]
        
        minIdx, minVal = 0, inf
        print(remaining)
        for i in range(len(gas)):
            remaining[i] += remaining[i-1] 
            if remaining[i] < minVal:
                minIdx, minVal = i, remaining[i]
        print(remaining)
        startingCandidate = minIdx + 1 if minIdx + 1 < len(gas) else 0
        mygas = 0
        print(minIdx, startingCandidate)
        for i in range(len(gas)):
            cur = startingCandidate + i
            if cur >= len(gas):
                cur -= len(gas)
            mygas += gas[cur]
            mygas -= cost[cur]
            if mygas < 0:
                return -1
        return startingCandidate
        
    # ========================================
    
    # Naive (two-loop) [O(n2): TLE]
    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        candidates = []
        for i in range(len(gas)):
            if cost[i] <= gas[i]:
                candidates.append(i)
        print(len(gas))
        print(len(candidates))
        for start in candidates:
            #print("start:", start)
            isSuccessful = True
            mygas = 0
            for i in range(len(gas)):
                cur = start + i 
                if cur >= len(gas):
                    cur -= len(gas)
                mygas += gas[cur]
                mygas -= cost[cur]
                #print(cur, mygas)
                if mygas < 0:
                    isSuccessful = False
                    break
            if isSuccessful:
                return start
        return -1