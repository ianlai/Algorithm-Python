'''
You are running a classroom and suspect that some of your students are passing around the answers to multiple choice questions disguised as random strings.

Your task is to write a function that, given a list of words and a string, finds and returns the word in the list that is scrambled up inside the string, if any exists. There will be at most one matching word. The letters don't need to be in order or next to each other. The letters cannot be reused.

Example:
words = ['cat', 'baby', 'dog', 'bird', 'car', 'ax']
string1 = 'tcabnihjs'
find_embedded_word(words, string1) -> cat (the letters do not have to be in order)

string2 = 'tbcanihjs'
find_embedded_word(words, string2) -> cat (the letters do not have to be together)

string3 = 'baykkjl'
find_embedded_word(words, string3) -> None / null (the letters cannot be reused)

string4 = 'bbabylkkj'
find_embedded_word(words, string4) -> baby

string5 = 'ccc'
find_embedded_word(words, string5) -> None / null

string6 = 'breadmaking'
find_embedded_word(words, string6) -> bird

Complexity analysis variables:

W = number of words in `words`
S = maximal length of each word or string
'''

words = ["cat", "baby", "dog", "bird", "car", "ax"]
string1 = "tcabnihjs"
string2 = "tbcanihjs"
string3 = "baykkjl"
string4 = "bbabylkkj"
string5 = "ccc"
string6 = "breadmaking"

import collections
def find_embedded_word(words, target):
    wordCount = collections.defaultdict(lambda: collections.defaultdict(int))
    for word in words:
        for ch in word:
            wordCount[word][ch] += 1
    #print(wordCount)
    
    targetCount = collections.defaultdict(int)
    for ch in target:
        targetCount[ch] += 1
        # compare 
        for word, wordMap in wordCount.items():
            isValid = True
            for c, count in wordMap.items():
                #print(c, count, targetCount)
                if count > targetCount[c]:
                    isValid = False
                    break
            if isValid: 
                return word
        #print(targetCount)
    return None
    
print(find_embedded_word(words, string1))
print(find_embedded_word(words, string2))
print(find_embedded_word(words, string3))
print(find_embedded_word(words, string4))
print(find_embedded_word(words, string5))
print(find_embedded_word(words, string6))