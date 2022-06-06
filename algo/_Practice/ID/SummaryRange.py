'''
Summary Range

Q1: Sorted, unique element -> return the intervals 

Q2: Duplicated number? 

Q3: No sort?  

'''

'''
Q1: Sorted, Unique 

TC: O(N)
SC: O(N) 
'''
from bisect import bisect_left


def summaryRanges(nums):
    if not nums:
        return []
    intervals = [[nums[0], nums[0]]]
    for i, v in enumerate(nums):
        if i == 0:
            continue
        if nums[i-1] + 1 == nums[i]:
            intervals[-1][1] = nums[i]
        else:
            intervals.append([v, v])
    return intervals

nums1 = [0,1,2,4,5,7,8]
nums2 = [0,1,2,2,2,4,5,7,7,7,8]
print(summaryRanges(nums1))
print(summaryRanges(nums2))  #incorrect: [[0, 2], [2, 2], [2, 2], [4, 5], [7, 7], [7, 7], [7, 8]]


'''
Q2: Sorted, Not Unique 

TC: O(N)
SC: O(N) 
'''
def summaryRangesNotUnique(nums):
    if not nums:
        return []
    intervals = [[nums[0], nums[0]]]
    for i, v in enumerate(nums):
        if i == 0:
            continue
        if nums[i-1] + 1 == nums[i]:
            intervals[-1][1] = nums[i]
        elif nums[i-1] == nums[i]:
            continue
        else:
            intervals.append([v, v])
    return intervals

nums3 = [0,1,2,2,2,4,5,7,7,7,8]
print(summaryRangesNotUnique(nums3))


'''
Q3: Not Sorted, Not Unique 

[1] HashMap //Done 
TC: O(N)
SC: O(N)

[2] Binary Search //Done
TC: O(N^2)  //because of insert and pop
SC: O(N)
'''
def summaryRangesNotSorted(nums):
    sToE = {}
    eToS = {}
    used = set()
    for v in nums:
        if v in used:
            continue
        if v - 1 in eToS and v + 1 in sToE: #[1,3] 4 [5,6]
            s = eToS[v-1]
            e = sToE[v+1]
            sToE[s] = e
            eToS[e] = s
            del eToS[v-1]
            del sToE[v+1]
        elif v - 1 in eToS:                 #[1,3] 4 [7,8]
            s = eToS[v-1] 
            sToE[s] = v
            eToS[v] = s
            del eToS[v-1]
        elif v + 1 in sToE:
            e = sToE[v+1] 
            sToE[v] = e
            eToS[e] = v
            del sToE[v+1]
        else:
            sToE[v] = v
            eToS[v] = v
        used.add(v)
    print(sToE)
    print(eToS)
nums4 = [1,0,4,7,8,4,3,1,2,9,11,30,10,12,15]
print(summaryRangesNotSorted(nums4))


def summaryRangesNotSortedBS(nums):
    arr = []
    used = set()
    for v in nums:
        if not arr:
            arr.append([v, v])
            used.add(v)
            continue
        idx = bisect_left(arr, [v, v])
        # if idx != 0 and idx != len(arr) and v <= arr[idx-1][1]:
        #     continue
        if v in used:
            continue

        if idx != 0 and idx != len(arr) and v - 1 == arr[idx-1][1] and v + 1 == arr[idx][0]:
            end = arr[idx][1]
            arr[idx-1][1] = end
            arr.pop(idx)
        elif idx != 0 and v - 1 == arr[idx-1][1]:
            arr[idx-1][1] = v
        elif idx != len(arr) and v + 1 == arr[idx][0]:
            arr[idx][0] = v
        else:
            arr.insert(idx, [v, v])
        used.add(v)
        #print(arr)
    print(arr)
nums5 = [1,0,4,7,8,4,3,1,2,9,11,30,10,12,15]
print(summaryRangesNotSortedBS(nums5))

