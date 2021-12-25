class Solution:
    # Divide and Conquer [O(n2): 5%]
    def longestSubstring(self, s: str, k: int) -> int:
        print("Code3")
        countMap = collections.defaultdict(int)
        for c in s:
            countMap[c] += 1
        for i, c in enumerate(s):
            if countMap[c] < k:
                return max(self.longestSubstring(s[:i], k), self.longestSubstring(s[i+1:], k))
        return len(s)
            
    #=================================
    
    # Two-Pointer with differenct char set size [O(26*n): 41%]
    def longestSubstring2(self, s: str, k: int) -> int:
        print("Code2")
        
        def isValidOverK(countMap):
            for char in countMap.keys():
                if countMap[char] < k:
                    return False
            return True

        countMap = collections.defaultdict(int)
        for char in s:
            countMap[char] += 1
        charSize = len(countMap)

        res = 0
        resList = []
        for i in range(1, charSize + 1):
            countMap = collections.defaultdict(int) 
            left, right = 0, 0 
            for right in range(len(s)):
                countMap[s[right]] += 1
                ## countMap size over i => left ++ 
                while len(countMap) > i and left != right:
                    countMap[s[left]] -= 1
                    if countMap[s[left]] == 0:
                        del countMap[s[left]]
                    left += 1
                    
                ## Not valid yet => right ++
                if not isValidOverK(countMap):
                    continue
            
                ## Debug: Add result to resList
                if right - left + 1 >= res:
                    resList.append([i, left, right, right - left + 1])
                res = max(res, right - left + 1)
        print("unique =", charSize, "res = ", res, resList)
        return res
    
    #=================================
    #Brute Force [O(n2): TLE]
    def longestSubstring1(self, s: str, k: int) -> int:
        print("Code1")
        def isValid(countMap):
            for char, count in countMap.items():
                if count < k:
                    return False
            return True
            
        countMap = collections.defaultdict(int)
        longestSubstring = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                countMap[s[j]] += 1
                if isValid(countMap):
                    #print(i, j, countMap, j-i+1)
                    longestSubstring = max(longestSubstring, j - i + 1)
            countMap = collections.defaultdict(int) 
        return longestSubstring 
            
        