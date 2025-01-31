class Solution:
    
    # 2022/03/27
    # Half palindrome [Time: O(n): 100% / Space: O(1): 100%]
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        digit = (intLength - 1) // 2
        base = 10 ** digit
        res = []
        for q in queries:
            # q-th number from base
            num = base + q - 1 
            strNum = str(num)
            if q > 9 * base:
                res.append(-1)
                continue
            if intLength % 2 == 0:
                # Even:
                #   example1:  10  --> 10+01  = 1001
                #   example2:  23  --> 23+32  = 2332
                res.append(int(strNum + strNum[::-1]))         
            else:
                # Odd:
                #   example1:  100 --> 100+01 = 10001
                #   example2:  204 --> 204+02 = 20402
                res.append(int(strNum + strNum[::-1][1:])) 
        return res