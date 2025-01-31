'''
Guess Word

Guess Word, 给一个dictionary全是四个字母的词类似{"cash","cast","bill","able"} 
然后每轮游戏开始random一个target word让猜最多五次，如果猜的词不在dicitionary里面就提示不在并且不算在5次内。
如果正确字母在正确位置就是1，字母在不正确位置就是0，词没有的字母就是-。 有一些edge case要cover比如有两个重复字母

例如：
target: cast

guess:  cash
return: 111-‍‌‌‍‌‍‍‌‍‍‌‌‌‍‌‍‌‍‍‌

guess:  able
return: 0---
'''

import random 
class GuessWord:

    def __init__(self, maxTime = 5):
        self.target = self.createTarget()
        self.start(maxTime)

    def createTarget(self):
        word = ""
        for _ in range(4):
            chint = random.randint(0, 25)
            ch = chr(chint + ord('a'))
            word += ch
        return word

    def start(self, maxTime):
        while maxTime > 0:
            guessWord = input("Input a word to guess (4 chars): ")
            res = self.compareWords(guessWord)
            if res == "1111" : 
                return "Successful! Target is \" " + self.target + " \" " 
            print("Result: ", res)
            maxTime -= 1

    def compareWords(self, word):
        res = ""
        for i, ch in enumerate(word):
            if ch == self.target[i]:
                res += "1"
            else:
                if ch in self.target:
                    res += "0"
                else:
                    res += "-"
        return res
                
guessWord = GuessWord()

