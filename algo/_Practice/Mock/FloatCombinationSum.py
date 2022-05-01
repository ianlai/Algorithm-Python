from typing import (
    List,
)
import math 


'''
https://www.lintcode.com/problem/1800/description

1800 · 浮点数组合和

给出一个小数数组A，一个非负整数target。对A中的每个小数进行向上取整或者向下取整的操作，
最后得到一个整数数组，要求整数数组的所有数字和等于target，并且要求对小数数组的调整和最小。
例如ceil(1.2)，则调整数为0.8；floor(1.2)，则调整数为0.2。返回该整数数组。

样例 1:
输入：A=[1.2,1.7],target=3
输出：[1,2]
解释：1.2->1,1.7->2。

样例 2:
输入：A=[2.4,2.5],target=5
输出：[2,3]
解释：2.4->2,2.5->3.

'''
class Solution:
    """
    @param a: A float array
    @param target: A non-negative integer
    @return: 
    """
    
    def get_array(self, a: List[float], target: int) -> List[int]:

        dp =    [[float('inf')] * (target+1) for _ in range(len(a))]
        steps = [[float('inf')] * (target+1) for _ in range(len(a))]     
    
        # DP loops 
        for i in range(len(a)):
            for j in range(target+1):
                if i == 0:
                    ceilingAdj = math.ceil(a[i]) - a[i]
                    floorAdj = a[i] - math.floor(a[i]) 

                    dp[i][math.ceil(a[i])] = ceilingAdj
                    dp[i][math.floor(a[i])] = floorAdj
                    steps[i][math.ceil(a[i])] = 'c'
                    steps[i][math.floor(a[i])] = 'f'
                else:
                    ceiling = math.ceil(a[i])
                    floor = math.floor(a[i])
                    ceilingAdj = ceiling - a[i]
                    floorAdj = a[i]- floor

                    ceilingCost = float('inf')  
                    floorCost = float('inf')
                    if j - ceiling >= 0:
                        ceilingCost = dp[i-1][j - ceiling] + ceilingAdj
                    if j - floor >= 0:
                        floorCost = dp[i-1][j - floor] + floorAdj

                    if floorCost < ceilingCost:
                        dp[i][j] = floorCost
                        steps[i][j] = 'f'
                    else:
                        dp[i][j] = ceilingCost
                        steps[i][j] = 'c'

        #Traverse back to form the path 
        intA = []
        for i in range(len(a)-1, -1, -1):
            step = steps[i][target]
            val = None
            if step == 'f':
                val = math.floor(a[i])
            else:
                val = math.ceil(a[i])
            intA.append(val)
            target -= val      

        return intA[::-1]