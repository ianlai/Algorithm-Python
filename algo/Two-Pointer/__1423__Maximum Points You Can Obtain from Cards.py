class Solution:
    
    # 2022/06/26
    # Sliding Window [O(N): 23% / O(1): 95%]
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        windowSize = len(cardPoints) - k
        windowSum = sum(cardPoints[:windowSize])
        minWindowSum = windowSum
        for i in range(windowSize, len(cardPoints)):
            windowSum += cardPoints[i]
            windowSum -= cardPoints[i - windowSize]
            minWindowSum = min(minWindowSum, windowSum)
        return sum(cardPoints) - minWindowSum