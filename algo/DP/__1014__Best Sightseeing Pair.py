class Solution:
    
    
    # DP (One pass) [O(n): 46%]
    # Use the fact that i-1 will always left to the i to guarentee the order of two pointer
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        print("Code3")
        
        leftMax = -inf
        allMax = -inf
        for i in range(1, len(values)):
            leftMax = max(leftMax, values[i-1] + (i-1))
            allMax = max(allMax, values[i] - i + leftMax)
        return allMax
    
    # =======================================

    # Brute force [O(n2): TLE]
    def maxScoreSightseeingPair2(self, values: List[int]) -> int:
        print("Code2")
        res = -inf
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                res = max(res, values[i] + values[j] - (j - i))
        return res
    
    # =======================================
    # Two pointer [Error]
    def maxScoreSightseeingPair1(self, values: List[int]) -> int:
        print("Code1")
        #print("maxScoreSightseeingPair", values)
        
        def calculateScore(left, right): 
            return values[left] + values[right] - (right - left)
            
        left, right = 0, len(values) - 1
        print("---------------")
        score = calculateScore(left, right)
        #print(left, right, score)
        while left + 1 < right:  
            if values[left] > values[right]:
                right -= 1
                score = max(score, calculateScore(left, right))
            elif values[left] < values[right]:
                left += 1
                score = max(score, calculateScore(left, right))
            else:
                score = max(score, calculateScore(left, right))
                score = max(score, self.maxScoreSightseeingPair(values[left:right]), self.maxScoreSightseeingPair(values[left+1:right+1]))
                break
            print(left, ":", values[left], right, ":", values[right], score)
        print(values,"->",score)
        score = max(score, calculateScore(left, right)) 
        return score