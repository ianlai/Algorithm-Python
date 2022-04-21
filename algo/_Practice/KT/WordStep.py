"""
Given two strings s1 and s2, we will call (s1, s2) a "step" if you can form s2 by adding exactly one letter to s1 and possibly rearranging the letters of s1.

For example:
(OF, FOR) is a step
(OF, IF) is not a step
(OF, OCT) is not a step
(ERA, EAR) is not a step
(SHE, SHEEP) is not a step
(TEE, TEST) is not a step

Given a wordlist, produce an index
   w -> {  w1 | (w, w1) is a step } 
that associates to each word all the words in the wordlist that are a step away from it.

index = step_index(wordlist)

# Expected output (pseudocode, unordered):

NO     : [ ONE, NOT, NOW ]
INTO   : [ POINT ]
LEFT   : []
FORM   : [ FORMS ]
ONE    : []
FOUR   : []
FOR    : [ FORM, FOUR, FROM ]
FROM   : [ FORMS ]
OFF    : []
FORMS  : []
NOT    : [ INTO ]
OF     : [ FOR, OFF ]
NOW    : []
POINT  : []
ON     : [ ONE, NOT, NOW ]


"""

counts = [
	"POINT,333858038",
	"NOT,4522732626",
	"INTO,1144226142",
	"ON,4594521081",
	"FOR,6545282031",
	"NOW,679337516",
	"ONE,2148983086",
	"BEHAVIOR,104177552",
	"WAITS,2911079",
	"PEOPLE,658716166",
	"HI,15453893",
	"FORM,352032932",
	"OF,30966074232",
	"THROUGH,647091198",
	"BETWEEN,744064796",
	"FOUR,262968583",
	"LEFT,306802162",
	"OFF,302535533",
	"FROM,3469207674",
	"NO,1400645478",
	"FORMS,136468034",
	"A,45954218"
]
# "A,45916054218"
#"BETWEEN,744064796",
k = 150
c = 5
def get_list(counts, k, c):
    filtered = []
    for record in counts:
        element, count = record.split(',')
        if 2 <= len(element) <= c:
            filtered.append([element, int(count)])
    filtered.sort(key=lambda x:-x[1])
    if k > len(filtered):
        return filtered
    return filtered[:k]
"""    
res = get_list(counts, k, c)
for row in res:
    print(row)
"""



'''
NO     : [ ONE, NOT, NOW ]
INTO   : [ POINT ]
LEFT   : []
FORM   : [ FORMS ]
ONE    : []
FOUR   : []
FOR    : [ FORM, FOUR, FROM ]
FROM   : [ FORMS ]
OFF    : []
FORMS  : []
NOT    : [ INTO ]
OF     : [ FOR, OFF ]
NOW    : []
POINT  : []
ON     : [ ONE, NOT, NOW ]

word -> char_count
NO  -> N: 1, O: 1
ONE -> N: 1, O: 1, E: 1
'''

import collections
def distance(wordCount, A, B):
    countA = wordCount[A] 
    countB = wordCount[B]
    diff = 0
    print(A, B, countA, countB)
    for k, v in countA.items():
        if k not in countB:
            return False

    for k, v in countB.items():
        if k not in countA:
            diff += 1
        else:
            diff += countB[k] - countA[k]

    return diff == 1

wordCount = collections.defaultdict(dict)
def findAnswer():
    words = ["NO", "INTO", "NOW", "NOT", "FOUR", "FOR", "AFO"]
    for word in words:
        for ch in word:
            if ch in wordCount[word]:
                wordCount[word][ch] = wordCount[word][ch] + 1
            else:
                wordCount[word][ch] = 1
    res = []
    for i, word in enumerate(words):
        cur = []
        for j in range(len(words)):
            if i == j:
                continue
            if distance(wordCount, words[i], words[j]):
                cur.append(words[j])
        res.append([words[i], cur])
    return res 

res = findAnswer()
for row in res:
    print(row)