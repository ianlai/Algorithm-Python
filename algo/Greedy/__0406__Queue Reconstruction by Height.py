class Solution:
    
    # 2022/06/30
    # Greedy: Sort people, then scan from smaller to large to insert [O(nlogn+n2): 9% / O(n): 64%]
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        hToIdx = defaultdict(list)
        res = [None] * len(people)
        
        for i, (h, k) in enumerate(people):
            hToIdx[h].append(i)
        
        accumulatedCount = 0
        for h in sorted(hToIdx.keys()):
            for pplIdx in hToIdx[h]:
                _, k = people[pplIdx]
                idx = 0 
                for i in range(len(people)):
                    if res[i] is None or res[i][0] == h:
                        if idx == k:
                            res[i] = people[pplIdx]
                            break
                        idx += 1
        return res