class Solution:
    # 2022/03/27
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
    def fizzBuzz1(self, n: int) -> List[str]:
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