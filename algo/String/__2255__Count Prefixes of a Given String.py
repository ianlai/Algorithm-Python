class Solution:
    
    # 2022/04/30
    # Create prefix and put in set [O(L+WL): 37% / O(L): 75%]
    def countPrefixes(self, words: List[str], s: str) -> int:
        prefixs = set()
        for i in range(len(s)):
            prefixs.add(s[:i+1])
        res = 0
        for word in words:
            if word in prefixs:
                res += 1
        return res