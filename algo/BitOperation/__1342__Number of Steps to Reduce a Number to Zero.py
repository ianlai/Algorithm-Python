class Solution:
    
    # 2022/05/27 
    # Bitwise Operation (count) [O(N)]
    def numberOfSteps(self, num: int) -> int:
        print("Code3")
        res = math.floor(math.log(num, 2)) + bin(num)[2:].count('1') if num != 0 else 0
        return res

    # Bitwise Operation [O(N)]
    def numberOfSteps2(self, num: int) -> int:
        print("Code2")
        step = 0 
        while num != 0:
            if num & 1 == 0:
                num = num >> 1
            else:
                num -= 1
            step += 1
        return step
    
    # Simulation [O(N)] 
    def numberOfSteps1(self, num: int) -> int:
        print("Code1")
        step = 0 
        while num != 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            step += 1
        return step