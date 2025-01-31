#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxSubarrayLength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY badges as parameter.
#

def maxSubarrayLength(badges):
    negativeCount = 0 
    firstNegativeIdx, lastNegativeIdx = -1, -1
    for i, val in enumerate(badges):
        if val == -1:
            negativeCount += 1
            if firstNegativeIdx == -1:
                firstNegativeIdx = i
            lastNegativeIdx = i
            
    if negativeCount % 2 == 0:
        return len(badges)
    else:
        return max(len(badges) - firstNegativeIdx - 1, lastNegativeIdx)
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    badges_count = int(input().strip())

    badges = []

    for _ in range(badges_count):
        badges_item = int(input().strip())
        badges.append(badges_item)

    result = maxSubarrayLength(badges)

    fptr.write(str(result) + '\n')

    fptr.close()
