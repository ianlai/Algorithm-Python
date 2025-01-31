class Solution:
    
    # 2022/02/07
    # Greedy + Binary Search [Incorrect]
    def findLongestChain2(self, pairs: List[List[int]]) -> int:
        print("Code2")
        pairs = [[v[1], v[0]] for v in sorted(pairs, key = lambda x: x[1])]
        chain = []
        idx = 0
        print(pairs)
        while idx < len(pairs):
            print(idx, [pairs[idx][1]])
            chain.append(pairs[idx])
            idx = bisect.bisect(pairs, [pairs[-1][0], inf])    
        print(chain)
        return len(chain)
    
    # =============================================
    # 2022/02/07 
    # Greedy + Linear Search [O(n): 58%]
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        print("Code1")
        pairs.sort(key = lambda x: x[1])
        chain = []
        for i in range(len(pairs)):
            if not chain or chain[-1][1] < pairs[i][0]:
                chain.append(pairs[i])
        return len(chain)