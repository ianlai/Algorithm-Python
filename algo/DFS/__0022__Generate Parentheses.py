class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []
        
        results = []
        self.dfs(n, 0, 0, True, [False], [], results)
        return results
    
    def dfs(self, n, left, right, isLeft, isDone, cur, results):
        #if isDone[0]:
        #    return 
        
        if right >= n:
            #print("END")
            isDone[0] = True
            results.append(''.join(cur))
            return 
        
        #print(left, right)
        if left >= n and right < n:
            #print(">> ")
            #print(cur)
            self.dfs(n, left, right + 1, False, isDone, cur + [")"], results)   
        else:
            #print(cur)
            if left > right:
                self.dfs(n, left + 1, right, True, isDone, cur + ["("], results)
                self.dfs(n, left, right + 1, False, isDone, cur + [")"], results)
            else:
                self.dfs(n, left + 1, right, True, isDone, cur + ["("], results)
                
                
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         if n <= 0:
#             return []
        
#         results = []
#         self.dfs(n, 0, 0, True, [False], [], results)
#         return results
    
#     def dfs(self, n, left, right, isLeft, isDone, cur, results):
#         if isDone[0]:
#             return 
        
#         if right >= n:
#             print("END")
#             isDone[0] = True
#             results.append(''.join(cur))
#             #return 
        
#         print(left, right)
#         if left >= n and right <= n:
#             print(">> ")
#             cur.append(")")
#             print(cur)
#             self.dfs(n, left, right + 1, False, isDone, cur, results)   
#             cur.pop()
#         else:
#             if isLeft:
#                 #cur.append("(")
#                 print(cur)
#                 if left > right:
#                     self.dfs(n, left + 1, right, True, isDone, cur + ["("], results)
#                     self.dfs(n, left, right + 1, False, isDone, cur + [")"], results)
#                 else:
#                     self.dfs(n, left + 1, right, True, isDone, cur + ["("], results)
#                 #cur.pop()
#             else:
#                 #cur.append(")")
#                 print(cur)
#                 if left > right:
#                     self.dfs(n, left + 1, right, True, isDone, cur + ["("], results)
#                     self.dfs(n, left, right + 1, False, isDone, cur + [")"], results)
#                 else:
#                     self.dfs(n, left + 1, right, True, isDone, cur + ["("], results)
#                 #cur.pop()