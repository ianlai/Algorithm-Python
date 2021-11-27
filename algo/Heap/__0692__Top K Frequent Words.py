class Solution:
    
    # Sorting function [O(nlogn): 22%]
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordToCount = collections.defaultdict(int)
        for word in words:
            wordToCount[word] += 1
        
        res = sorted(wordToCount.items(), key = lambda x: [-x[1], x[0]])[:k]
        return [x[0] for x in res]