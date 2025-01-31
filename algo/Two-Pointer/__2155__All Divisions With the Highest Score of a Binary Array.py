class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        score = 0
        maxScore = 0
        maxToIndices = collections.defaultdict(list)
        for v in nums:
            if v == 1:
                score += 1
    
        for i in range(len(nums)+1):
            if i == 0:
                maxToIndices[score].append(i)
                maxScore = max(maxScore, score)
                continue
            if nums[i-1] == 0:
                score += 1
                maxScore = max(maxScore, score)
                maxToIndices[score].append(i)
            else:
                score -= 1
        return maxToIndices[maxScore]
        