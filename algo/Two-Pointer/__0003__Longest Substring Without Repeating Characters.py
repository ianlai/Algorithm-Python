class Solution:

    # 2022/01/22
    # Sliding window [O(n): 68%]
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        charSet = set()
        left = 0 
        res = 0
        for right in range(len(s)):
            if s[right] not in charSet:
                charSet.add(s[right])
                res = max(res, right - left + 1)
                continue
                
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
                
            charSet.add(s[right])
                
        return res

    #===================================================

    # 2021/04/17
    # Two-pointer, O(n), 38%
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        charToCount = {}
        maxLength = 0
        curLength = 0
        left, right = 0, 0 
        print("O(1)")
        print(s)
        while right < len(s):
            #print(left, right)
            target = s[right]
            while target in charToCount and charToCount[target] > 0:
                removing = s[left]
                charToCount[removing] -= 1
                left += 1
                curLength -= 1
                
            if target in charToCount:
                charToCount[target] += 1
            else:
                charToCount[target] = 1
            curLength += 1 
            
            #print(charToCount)
                
            maxLength = max(maxLength, curLength)
            right += 1

        return maxLength 
    
    #===================================================
    
    # Two-loop, O(n2), 6%
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        charToCount = {}
        maxLength = 0
        curLength = 0
        #print(len(s))
        for i in range(len(s)):
            curLength = 0
            charToCount = {}

            for j in range(i, len(s)):
                if s[j] in charToCount and charToCount[s[j]] > 0:
                    maxLength = max(maxLength, curLength)
                    charToCount[s[j]] -= 1
                    break
                else:
                    if s[j] in charToCount:
                        charToCount[s[j]] += 1
                    else:
                        charToCount[s[j]] = 1
                    curLength += 1
                maxLength = max(maxLength, curLength)
            #print("start:", s[i], "map:", charToCount, " curLength:", curLength, " maxLength:", maxLength)

        return maxLength 