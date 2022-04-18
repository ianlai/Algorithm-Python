class Solution:
    
    # 2022/04/18
    # String manipulation [O(w): 65% / O(w): 93%]
    def fullJustify(self, text: List[str], lineLength: int) -> List[str]:
        
        def generateLine(words, wordsLength, lineLength):
            #special case
            if len(words) == 1:
                return words[0] + " " * (lineLength - len(words[0]))

            spaces = lineLength - wordsLength
            gaps = [0] * (len(words) - 1)

            # distribute spaces (banana) into gaps (monkey)
            spaceForGap = spaces // len(gaps)
            leftSpace = spaces % len(gaps)

            res = ""
            for word in words[:len(words)-1]:
                res += word + " " * spaceForGap
                if leftSpace > 0:
                    res += " "
                    leftSpace -= 1
            res += words[-1]
            return res

        
        words = []
        for line in text:
            line = line.strip().split(" ")
            words.extend(line)

        res = []
        wordsInLine = []
        wordsLength = 0
        #for idx, word in enumerate(words): #can't use for loop because we need to revert back 
        idx = 0
        while idx < len(words):
            word = words[idx]
            if wordsLength + len(word) + len(wordsInLine) > lineLength:
                line = generateLine(wordsInLine, wordsLength, lineLength)
                res.append(line)
                #reset 
                wordsInLine = []
                wordsLength = 0
            else:
                wordsInLine.append(word)
                wordsLength += len(word)
                idx += 1
                
        #last line (left-justified)
        if wordsInLine:
            line = ""
            for word in wordsInLine[:-1]:
                line += word + " "
            line += wordsInLine[-1]
            line += " " * (lineLength - len(line))
            res.append(line)
        return res