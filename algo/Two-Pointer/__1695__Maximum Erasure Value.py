class Solution:
    
    # 2022/06/12
    # Prefix Sum + Sliding Window [O(N): 35% / O(N): 30%]
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])

        maxScore = 0
        left = 0
        charSet = set()
        for right in range(len(nums)):
            if nums[right] not in charSet:
                charSet.add(nums[right])
            else:
                while nums[right] in charSet:
                    charSet.remove(nums[left])
                    left += 1
                charSet.add(nums[right])
            if left > 0: 
                maxScore = max(maxScore, prefixSum[right] - prefixSum[left - 1])
            else:
                maxScore = max(maxScore, prefixSum[right])
        return maxScore