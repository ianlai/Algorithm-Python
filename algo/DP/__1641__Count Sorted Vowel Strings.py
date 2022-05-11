class Solution:

    # Math 
    '''
    H(5, n) = C(5+n-1, n) = C(n+4, n) = (n+4)(n+3)(n+2)(n+1) / 24 
    '''
    
    # DFS 
    ''' 
    1 - 2  -- 3
           -- 4
           -- 5
      - 3  -- 4
           -- 5
      - 4  -- 5
      - 5
      
    2 - 3 -- 4
          -- 5
      - 4 -- 5
      - 5 
      
    3 - 4
      - 5
      
    4 - 5
    
    5 
    
    '''
    
    #DP 
    '''
        a  e  i  o  u
    1:  1  1  1  1  1 
    2:  1  2  3  4  5
    3:  1  3  6 10 15
    
    '''  
    
    # 2022/05/11
    # Math 重複組合 [O(1): 95% / O(1): 65%]
    def countVowelStrings(self, n: int) -> int:
        print("Code3 Math")
        return (n+1)*(n+2)*(n+3)*(n+4) // 24


    '''
    2022/05/11 
    DP (buttom-up)

    TC: O(5N) = O(N)
    SC: O(5)  = O(1)
    '''
    # 2022/05/11
    # DP (buttom-up) [O(n): 23% / O(1): 27%]
    def countVowelStrings(self, n: int) -> int:
        print("Code2 [BEST]")
        dp = [1] * 5
        for i in range(n - 1):
            for j in range(1, 5):
                dp[j] += dp[j - 1] 
        return sum(dp)
    
    
    # 2022/03/08
    # DP [O(n): 68%]
    # 看起來不難，但需要兩個dp matrix(或省空間的array)，但還是想很久才找出關係式子
    def countVowelStrings1(self, n: int) -> int:
        print("Code1")
        if n == 1:
            return 5
        if n == 2:
            return 5 + 4 + 3 + 2 + 1
        
        dp = [[1 for _ in range(5)] for _ in range(n)]
        pascal = [[1 for _ in range(5)] for _ in range(n)]
        total = sum(dp[0])
        
        for i in range(2, n):
            for j in range(5):
                if j == 0:
                    pascal[i][j] = pascal[i-1][j]
                else:
                    pascal[i][j] = pascal[i][j-1] + pascal[i-1][j]
                dp[i][j] = pascal[i][j] * (5 - j)
                
        return sum(dp[n-1])
            