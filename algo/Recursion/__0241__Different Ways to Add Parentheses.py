class Solution:
    
    # Memoization DP [95%]
    # Divide and Conquer (recursion) [46%]
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        return self.cal(expression, memo)
        
    def cal(self, expression, memo):
        if not expression:
            return []
        #if expression in memo:
        #    return memo[expression]
        
        results = []
        for i in range(len(expression)):
            if expression[i] == "+" or expression[i] == "-" or expression[i] == "*":
                left = self.cal(expression[:i], memo)
                right = self.cal(expression[i+1:], memo)
                for l in left:
                    for r in right:
                        if expression[i] == "+": 
                            results.append(l+r)
                        if expression[i] == "-": 
                            results.append(l-r)
                        if expression[i] == "*": 
                            results.append(l*r)
        if not results:
            results.append(int(expression))
        memo[expression] = results
        return results
                
                