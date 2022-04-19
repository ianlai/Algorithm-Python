
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

words = ["abc", "de", "fgh", "k", "m"]
print(wordWrap(words, 11))
print(wordWrap(words, 12))
print(wordWrap(words, 13))
print(wordWrap(words, 14))