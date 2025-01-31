class Solution:
    
    # Iterate intervals [O(NlogN + N): 28% / O(1): 42%]
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        total = max(special[0] - bottom, top - special[-1])
        for i, p in enumerate(special):
            if i > 0:
                total = max(total, p - special[i-1] - 1)
        return total
            

#     def maxConsecutive1(self, bottom: int, top: int, special: List[int]) -> int:
#         sset = set(special)        
#         total, count = 0, 0
#         for i in range(bottom, top+1):
#             if i in sset:
#                 count = 0
#             else:
#                 count += 1
#                 total = max(total, count)
#         return total 