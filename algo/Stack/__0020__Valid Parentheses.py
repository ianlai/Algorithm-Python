class Solution:
    
    # Stack [O(n), 57%]
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        stack = []
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                pop = stack.pop()
                if pop == "(" and ch != ")":
                    return False
                if pop == "{" and ch != "}":
                    return False
                if pop == "[" and ch != "]":
                    return False
        return len(stack) == 0