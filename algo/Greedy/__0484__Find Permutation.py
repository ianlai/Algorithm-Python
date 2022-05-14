class Solution:
    
    # 2022/05/14
    # Greedy (in-place) [O(N): 99% / O(1): 5%]
    def findPermutation(self, s: str) -> List[int]:
        print("Code3")
        res = []
        for i in range(1, len(s) + 2):
            res.append(i)
            
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        prev = None
        dFirstIdx = dLastIdx = 0
        for i, ch in enumerate(s):
            if ch == "I" and prev == "D": #DI
                dLastIdx = i - 1
                reverse(res, dFirstIdx, dLastIdx + 1)
            if ch == "D" and prev == "I": #ID
                dFirstIdx = i
            prev = ch
            
        if s[-1] == "D":
            reverse(res, dFirstIdx, len(s))
        return res
    
    # 2022/05/14
    # Greedy (assign) [O(N2): 5% / O(N): 5%]
    def findPermutation2(self, s: str) -> List[int]:
        print("Code2")
        res = []
        for i in range(1, len(s) + 2):
            res.append(i)
            
        def reverse(arr, i, j):
            return arr[:i] + arr[i:j+1][::-1] + arr[j+1:] 
        
        prev = None
        dFirstIdx = dLastIdx = 0
        for i, ch in enumerate(s):
            if ch == "I" and prev == "D": #DI
                dLastIdx = i - 1
                res = reverse(res, dFirstIdx, dLastIdx + 1)
            if ch == "D" and prev == "I": #ID
                dFirstIdx = i
            prev = ch
            
        if s[-1] == "D":
            res = reverse(res, dFirstIdx, len(s))
        return res
            
    # 2022/05/14
    # Backtracking [TLE]
    def findPermutation1(self, s: str) -> List[int]:
        print("Code1")
        def dfs(idx, cur, visited):
            if len(cur) == len(s) + 1:
                return list(cur)
            
            for i in range(1, n + 1):
                if i in visited:
                    continue
                if idx > 0 and s[idx-1] == "I" and cur[-1] >= i:
                    continue
                if idx > 0 and s[idx-1] == "D" and cur[-1] <= i:
                    continue
                visited.add(i)
                res = dfs(idx + 1, cur + [i], visited)
                visited.remove(i)
                if res is not None:
                    return res
            return None
                
        n = len(s) + 1
        visited = set()
        return dfs(0, [], visited)