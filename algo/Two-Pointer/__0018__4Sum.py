class Solution:
    
    # Two-Pointer; remove the duplication while searching (O(n3), 40%)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        result = []
        #print(nums)
        
        for a in range(len(nums) - 3):
            if a > 0 and nums[a-1] == nums[a]:
                a += 1
                continue
                
            for b in range(a + 1, len(nums) - 2):
                #print("a, b = ", a, b)
                if b > a + 1 and nums[b-1] == nums[b]:
                    b += 1
                    continue
                    
                c, d = b + 1, len(nums) - 1
                while c < d:
                    fourSum = nums[a] + nums[b] + nums[c] + nums[d]
                        
                    if fourSum == target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1 
                        while c < d and nums[c-1] == nums[c]:
                            c += 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
                    elif fourSum > target:
                        d -= 1 
                    else:
                        c += 1 
                        
        # Use set to remove the duplication:
        # ans = []              
        # for tup in result:
        #     ans.append(list(tup))
        
        return result