class Solution:
    
    # Using HashMap [O(n): 21%]
    # The order are determined so we don't need to do backtracking 
    def originalDigits(self, s: str) -> str:
        
        digitToString = {
            0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"
        }
        
        # 0: defaultdict(<class 'int'>, {'z': 1, 'e': 1, 'r': 1, 'o': 1}), 
        # 1: defaultdict(<class 'int'>, {'o': 1, 'n': 1, 'e': 1}), 
        # 2: defaultdict(<class 'int'>, {'t': 1, 'w': 1, 'o': 1}), 
        # 3: defaultdict(<class 'int'>, {'t': 1, 'h': 1, 'r': 1, 'e': 2}), 
        # 4: defaultdict(<class 'int'>, {'f': 1, 'o': 1, 'u': 1, 'r': 1}), 
        # 5: defaultdict(<class 'int'>, {'f': 1, 'i': 1, 'v': 1, 'e': 1}), 
        # 6: defaultdict(<class 'int'>, {'s': 1, 'i': 1, 'x': 1}), 
        # 7: defaultdict(<class 'int'>, {'s': 1, 'e': 2, 'v': 1, 'n': 1}), 
        # 8: defaultdict(<class 'int'>, {'e': 1, 'i': 1, 'g': 1, 'h': 1, 't': 1}), 
        # 9: defaultdict(<class 'int'>, {'n': 2, 'i': 1, 'e': 1})
    
        digitToCount = collections.defaultdict(lambda: collections.defaultdict(int))
        for digit in digitToString:
            for c in digitToString[digit]:
                digitToCount[digit][c] += 1 
        #print(digitToCount)
                
        alphaToDigitList = {
            "e": [0, 1, 3, 5, 7, 8, 9],
            "g": [8],
            "f": [4, 5],
            "i": [5, 8, 9],
            "h": [3, 8],
            "o": [0, 1, 2, 4],
            "n": [1, 7, 9],
            "s": [6, 7],
            "r": [0, 3, 4],
            "u": [4],
            "t": [2, 3, 8],
            "w": [2],
            "v": [5, 7],
            "x": [6],
            "z": [0]
        }
        
        alphaToDigit = {
            #1st
            "g": [8],
            "u": [4],
            "x": [6],
            "z": [0],
            "w": [2],
            #2nd
            "f": [5],
            "h": [3],
            "s": [7],
            "t": [3],
            "r": [3],
            #3rd
            "i": [9],
            "o": [1],
            #4th
            "n": [7],
            "v": [7]
            #"e": [0, 1, 3, 5, 7, 8, 9],
        }
            
        inputCount = collections.defaultdict(int)
        for c in s:
            inputCount[c] += 1

        resCount = collections.defaultdict(int)
        res = []
        
        
        # print("=========1========")
        # print("input:", inputCount, dict(inputCount))
        # print("res:", resCount)
        for target in "guwxz":
            count = inputCount.get(target, 0)
            number = alphaToDigit[target][0]
            #print(target, count)
            resCount[number] += count
            for _ in range(count):
                for d, c in digitToCount[number].items():
                    inputCount[d] -= c
    
        # print("=========2========")
        # print("input:", inputCount, dict(inputCount))
        # print("res:", resCount)
        for target in "fhstr":
            count = inputCount.get(target, 0)
            number = alphaToDigit[target][0]
            #print(target, count)
            resCount[number] += count
            for _ in range(count):
                for d, c in digitToCount[number].items():
                    inputCount[d] -= c
                    
        # print("=========3========")
        # print("input:", inputCount, dict(inputCount))
        # print("res:", resCount)
        for target in "io":
            count = inputCount.get(target, 0)
            number = alphaToDigit[target][0]
            #print(target, count)
            resCount[number] += count
            for _ in range(count):
                for d, c in digitToCount[number].items():
                    inputCount[d] -= c
        
        # print("=========4========")
        # print("input:", inputCount, dict(inputCount))
        # print("res:", resCount)
        for target in "nv":
            count = inputCount.get(target, 0)
            number = alphaToDigit[target][0]
            #print(target, count)
            resCount[number] += count
            for _ in range(count):
                for d, c in digitToCount[number].items():
                    inputCount[d] -= c
        
        for a, count in sorted(resCount.items()):
            res.extend([str(a)] * count)
        return "".join(res)
