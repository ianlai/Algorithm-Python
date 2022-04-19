def wordWrap(words, maxLen):
    if not words or maxLen == 0:
        return []
    resList = []
    remain = maxLen 
    for i, word in enumerate(words):
        if remain - len(word) < 0:
            break 
        remain -= (len(word) + 1)
        resList.append(word)
        resList.append("-")
    resList.pop()
    return "".join(resList)

'''
Input: 
text = ["Some modern typesetting programs ",
        "offer four justification",
        "options yoyo" ]

lineLength = 24

Output:
       ["Some--modern-typesetting",
        "programs----offer---four",
        "justification----options",
        "yoyo"]
'''

def generateLine(words, wordsLength, lineLength):
    #special case
    if len(words) == 1:
        return words[0]

    spaces = lineLength - wordsLength
    gaps = [0] * (len(words) - 1)

    # distribute spaces (banana) into gaps (monkey)
    spaceForGap = spaces // len(gaps)
    leftSpace = spaces % len(gaps)

    res = ""
    for word in words[:len(words)-1]:
        res += word + "-" * spaceForGap
        if leftSpace > 0:
            res += "-"
            leftSpace -= 1
    res += words[-1]
    return res

def wordProcessor(text, lineLength):
    words = []
    for line in text:
        line = line.strip().split(" ")
        words.extend(line)

    res = []
    wordsInLine = []
    wordsLength = 0
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
            
    #last line (not more than the lineLength)
    if wordsInLine:
        line = generateLine(wordsInLine, wordsLength, lineLength)
        res.append(line)
    return res

text = ["Some modern typesetting programs ",
        "offer four justification ",
        "options yoyo abcdef" ]
lineLength = 24

justified = wordProcessor(text, lineLength)
for line in justified:
    print(line, "  ", len(line))
