class Solution:
    
    # Bottom-Up DP [93%] 
    # Min diff of two sum of groups 
    def lastStoneWeightII(self, stones: List[int]) -> int:
        print("set update")
        sumStones = sum(stones) 
        halfStones = sumStones //2 
        possibleSums = set([0])
        for stone in stones: 
            temp = set([])
            for p in possibleSums:
                #temp.add(p)
                if p + stone <= halfStones:
                    temp.add(p + stone)
            possibleSums.update(temp)
        return sumStones - 2 * max(possibleSums)
    
    
    def lastStoneWeightII1(self, stones: List[int]) -> int:
        print("set assignment")
        sumStones = sum(stones) 
        halfStones = sumStones //2 
        possibleSums = set([0])
        for stone in stones: 
            temp = set([])
            for p in possibleSums:
                temp.add(p)
                if p + stone <= halfStones:
                    temp.add(p + stone)
            possibleSums = temp
        return sumStones - 2 * max(possibleSums)