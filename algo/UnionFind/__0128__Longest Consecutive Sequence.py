class Solution:
    
    # Union-Find [O(n2): 30%]
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numToIdx = collections.defaultdict(int)
        parents = [-1] * len(nums)
        self.count = len(nums)
        
        for i in range(len(nums)):
            if nums[i] in numToIdx:  #avoid redandunts
                continue 
            if nums[i] + 1 in numToIdx:
                self.union(parents, i, numToIdx[nums[i] + 1])
            if nums[i] - 1 in numToIdx:
                self.union(parents, i, numToIdx[nums[i] - 1])
            numToIdx[nums[i]] = i
        print(numToIdx)
        print(parents)
        return -min(parents)
                
    def union(self, parents, a, b):
        headA = self.find(parents, a)  #index 
        headB = self.find(parents, b)  #index
        if headA != headB:
            countA = - parents[headA] if parents[headA] < 0  else 1
            countB = - parents[headB] if parents[headB] < 0  else 1
            parents[headA] = headB
            parents[headB] = - (countA + countB)   #count stored in head
    
    def find(self, parents, idx):
        if parents[idx] < 0:
            return idx
        return self.find(parents, parents[idx])