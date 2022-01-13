class Solution:
    
    # 2022/01/13 
    # Using reverse(), join() [O(n): 99%]
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        
        arr = []
        cur = ""
        for i, ch in enumerate(s):
            if ch == " ":
                if cur:
                    arr.append(cur)
                    cur = ""
            else:
                cur += ch
        if cur:
            arr.append(cur)
        return " ".join(arr[::-1])
                
    # ==========================================
    # 2021/06/09 
    # Using split(), reverse(), and join() [O(n): 18%]
    def reverseWords1(self, s: str) -> str:
        print("Code1")
        if not s:
            return s
        
        arr = s.split()
        return ' '.join(arr[::-1])