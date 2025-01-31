class Solution:
    
    # DP [O(n2): 13%]
    def numTeams(self, rating: List[int]) -> int:
        if not rating:
            return 0
        n = len(rating)
        dpsmall = [0] * n
        dplarge = [0] * n
        
        # parse: O(n2)
        for i in range(n):
            for j in range(0, i):
                if rating[j] < rating[i]:
                    dpsmall[i] += 1
                if rating[j] > rating[i]:
                    dplarge[i] += 1
        
        # count: O(n2)
        count = 0
        for p3 in range(n):
            for p2 in range(0, p3):
                if rating[p2] < rating[p3]:
                    count += dpsmall[p2]
                if rating[p2] > rating[p3]:
                    count += dplarge[p2]
        return count
        
    #========================================  
    
    #Brute force [O(n3): TLE]
    def numTeams1(self, rating: List[int]) -> int:
        if not rating:
            return 0
        
        n = len(rating)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if rating[i] < rating[j] < rating[k]:
                        count +=1
                    if rating[i] > rating[j] > rating[k]:
                        count += 1
        return count