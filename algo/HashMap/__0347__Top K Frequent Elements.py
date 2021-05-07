class Solution:
    
    #Hashmap [O(nlogn), 67%]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        #Count 
        numTocount = {}
        for e in nums:
            if e in numTocount:
                numTocount[e] += 1
            else:
                numTocount[e] = 1     
                
        #Store to tuples into list to sort
        countToNum = []
        for key in numTocount.keys():
            countToNum.append((numTocount[key], key))

        #Sort the list in descending 
        countToNum.sort(reverse=True)
        return [x[1] for x in countToNum[:k]] 