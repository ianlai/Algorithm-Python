'''
2022/06/02 

[Question-1: Find 1 balance point in positive array]
/* 
 * Given an array of numbers, find the balance point in it.
 * Provide a function/method that will return balance point(s) for the given input array
 *
 * Examples:
 * [1, 1, 1] -> 2nd element is balance point (0-based indexing)
 *              v
 * [1, 2, 3, 4, 5, 4, 6] -> 5th element (index 4) is balance point
 * [1, 2, 3, 4, 5] -> There is no balance point
 * [1, 1, 1, 2, 3] -> 4th (index 3) elem is balance points
 */
 

[Question-2: Find multiple balance points in arbitrary array]
 /**
 * [1, -1, 1, -1, 1] -> [1st, 2nd, 3rd] are balance points
 */


[Question-3: Find balance points in matrix]
 /**
 * 
 * {1, 1, 1,   1, 3},  #7
 * {1, 1, 1,   1, 3},  #7
 * {1, 1, 1, 999, 3},  #1005
 * {1, 1, 1,   1, 3},  #7
 * {1, 1, 1,   1, 3}   #7
 */#5  5  5    1003  #15  
 
 
 # output:  index
 # no order
'''
 
arr = [1, 2, 3, 3]
 
# totalSum = sum(arr)
# negative also allowed
# T.C. = O(N)
# S.C. = O(1)
def findBalancePoints(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1: 
        return [0]
    
    totalSum = sum(arr)  #9
    leftSum = 0
    rightSum = totalSum - arr[0] #8
    res = []
    for i in range(1, len(arr)):
        leftSum += arr[i-1] #1 3 6
        rightSum -= arr[i]  #6 3 0
        if leftSum == rightSum:
            res.append(i)
    return res #[2]

print(findBalancePoints([1, 2, 3, 4, 5, 4, 6]))
print(findBalancePoints([1, -1, 1, -1, 1]))