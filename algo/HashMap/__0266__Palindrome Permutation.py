class Solution:
    
    # Count char [O(N): 53% / O(N): 96%]
    def canPermutePalindrome(self, s: str) -> bool:
        countMap = collections.Counter(s)
        
        isOneCountOdd = False
        for k, count in countMap.items():
            if count % 2 == 1:
                if not isOneCountOdd:
                    isOneCountOdd = True
                else:
                    return False
        return True