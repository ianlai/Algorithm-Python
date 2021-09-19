class Solution:
    def expand(self, s: str) -> List[str]:
        arr = [[]]
        expandables = []
        isExpand = False
        for c in s:            
            if c.isalpha():
                if isExpand:
                    expandables.append(c)
                else:
                    for cur in arr:
                        cur.append(c)
            elif c == "{":
                isExpand = True
            elif c == "}":
                isExpand = False
                newarr = []
                for cur in arr:
                    for expandable in expandables:
                        new = list(cur) 
                        new.append(expandable)
                        newarr.append(new)
                arr = newarr
                expandables = []
                
        res = []
        for cur in arr:
            res.append("".join(cur))
        return sorted(res)
                        
    
    
    
#     def expand(self, s: str) -> List[str]:
#         if not s:
#             return []
         
#         results = []
#         self.traverse(s, 0, results)
#         return results
                
#     def traverse(self, s, start, results):
#         i = start
#         while i < len(s): 
#             print(i, s[i])
#             if s[i] == "{":
#                 if "}" in s[i:]:
#                     j = s[i:].index("}") + i
#                     print("closed:", j)
#                     chars = s[i+1:j].split(",")
#                     print(chars)
#                     i = j + 1
#                     self.append(results, chars)     
#             elif s[i] == ",":
#                 i += 1
#                 continue
#             else:
#                 for result in results:
#                     result.append(s[i])
#                 print("self append", results)
#                 i += 1
                    
#     def append(self, results, chars):
#         if len(results) == 0:
#             for j in range(len(chars)):
#                 results.append([chars[j]])
#         else:
#             for i in range(len(results)):
#                 #results.insert(i*2, list(results[i*2]))
#                 for j in range(len(chars)):
#                     if j == 0:
#                         results[i].append(chars[j])
#                     else:
#                         results.insert(j, list(results[i]) + [chars[j]])
#                         #results.insert(len(chars) + j, list(results[i]) + [chars[j]])
                        
#         print("append", results)