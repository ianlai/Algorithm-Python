class Solution:
    
    # 2022/03/27
    # Avoid using mod operand [O(n): 50%]
    def fizzBuzz(self, n: int) -> List[str]:
        print("Code3")
        res = []
        count3, count5 = 3, 5
        for i in range(1, n+1):
            addString = ""
            count3 -= 1
            count5 -= 1
            if count3 == 0:
                addString += "Fizz"
                count3 = 3
            if count5 == 0:
                addString += "Buzz"
                count5 = 5
            if addString:
                res.append(addString)
            else:
                res.append(str(i))
        return res
    # =====================================
    
    # 2022/03/27
    # Form the added string first [O(n): 36%]
    def fizzBuzz(self, n: int) -> List[str]:
        print("Code2")
        res = []
        for i in range(1, n+1):
            addString = ""
            if i % 3 == 0:
                addString += "Fizz"
            if i % 5 == 0:
                addString += "Buzz"
            if addString:
                res.append(addString)
            else:
                res.append(str(i))
        return res
    # =====================================
    
    # 2022/03/26
    # Three separated cases [O(n): 22%]
    def fizzBuzz(self, n: int) -> List[str]:
        print("Code1")
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res