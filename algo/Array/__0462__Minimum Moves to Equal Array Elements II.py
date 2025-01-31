class Solution:
    
    # Greedy (heap) [O(nlogn): 30% / O(n): 8%]
    # def minMoves2(self, nums: List[int]) -> int:
    #     print("Code2")
    #     middleIdx = len(nums)//2 
    #     hp = nums[:middleIdx+1]
    #     heapq.heapify(hp)
    #     for i in range(middleIdx, len(nums)):
    #         if hp[0] < nums[i]:
    #             heapq.heappop(hp)
    #             heapq.heappush(hp, nums[i]) 
    #     pivot = hp[0]
    #     res = 0
    #     for v in nums:
    #         res += abs(v - pivot)
    #     return res
    
    # [1,2,9,10]
    #  0,1,8,9    18  //1
    #  1 0 7 8    16  //2
    #  8 7 0 1    16  //9
    
    # Greedy (sorting) [O(nlogn): 30% / O(n): 8%]
    def minMoves2(self, nums: List[int]) -> int:
        print("Code1")
        sortedNums = sorted(nums)
        pivot = sortedNums[len(nums)//2]
        res = 0
        for v in nums:
            res += abs(v - pivot)
        return res