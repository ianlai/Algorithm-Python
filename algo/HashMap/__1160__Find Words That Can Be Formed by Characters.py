# class CounterComp(Counter):
#     def __init__(self, string):
#         self.s = string
        
#     def __gt__(self, s2):
#         for k, v in self.s.items():
#             wordCount = collections.Counter(s2)
        
#     def __lt__(self, s2):
        
        
        
class Solution:
    
    # 2022/03/22
    # Hashmap [O(w*L): 76%]
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = collections.Counter(chars)
        res = 0        
        for word in words:
            wordCount = collections.Counter(word)
            isFormable = True
            for k, v in wordCount.items(): 
                if k not in count:
                    isFormable = False
                    break
                elif v > count[k]:
                    isFormable = False
                    break
            if isFormable:
                res += len(word)
        return res