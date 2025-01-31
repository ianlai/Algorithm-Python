class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs[0]) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        for i in range(len(strs[0])):
            idx = i 
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or c != strs[j][i]:
                    return strs[0][:idx]
        return strs[0][:idx+1]