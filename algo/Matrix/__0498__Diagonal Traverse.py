class Solution:
    
    # 2021/12/10 
    # Matrix manipulation [O(mn)]
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        idxSumToList = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                idxSum = i + j
                idxSumToList[idxSum].append(mat[i][j])
        res = []
        for idxSum in sorted(idxSumToList.keys()):
            if idxSum % 2 == 1:
                res.extend(idxSumToList[idxSum])
            else:
                res.extend(idxSumToList[idxSum][::-1])
        return res
        