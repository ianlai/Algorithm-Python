'''
Normalize Title

Given a rawTitle, and a list(or array) of clean titles. For each clean title,
the raw title can get a "match point". For example, if raw title is "senior software
engineer" and clean titles are "software engineer" and "mechanical engineer", the
"match point" will be 2 and 1. In this case we return "software engineer" because
it has higher "match point".


Example1:
rawTitle = "senior software engineer"
cleanTitles = ["software engineer", "mechanical engineer"] 

matching points = [2, 1] 
Output should be "software engineer" because matching point is higher

'''

#連續相同的個數
''' 
DP: O(MN) / O(MN)
可以處理有相同字或是不同字的情況
'''
def calScore(A, B):
    A = A.split(' ')
    B = B.split(' ')
    dp = [[0] * len(B) for _ in range(len(A))]
    maxScore = 0
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                if i > 0 and j > 0:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 1
            maxScore = max(maxScore, dp[i][j])
    return maxScore

def findHighestTitle(rawTitle, cleanTitles):
    highestScore = 0
    highestTitle = ""
    for ct in cleanTitles:
        score = calScore(rawTitle, ct) 
        #print("ct:", ct, score)
        if score > highestScore:
            highestScore = score
            highestTitle = ct
    return highestTitle

rawTitle = "senior software engineer"
cleanTitles = ["software engineer", "mechanical engineer", "senior software engineer", "technical writer"]
print(findHighestTitle(rawTitle, cleanTitles))