# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Time complexity: O(n)
def solution(A):
    if len(A) <= 2:   #special case: 1, 2
        return len(A)
    
    maxLength = 0
    left, right = 0, 2
    while right < len(A):
        if A[right] == A[right - 2] or right - left == 1:
            maxLength = max(maxLength, right - left + 1)
            right += 1
        else:
            left += 1
    return maxLength