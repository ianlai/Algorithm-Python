class Solution:
    
    # [2,5,7,18,24]
    # [6,10,19,30,35,38]
    
    # [2,5,9,11]
    # [6,10,12,30,35,38,42,55]
    
    # Binary Search [O(log(m+n)): 88%]
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # let nums1 be shorter
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1 
        
        total = len(nums1) + len(nums2)
        isEven = True if total % 2 == 0 else False
        
        start, end = 0, len(nums1)
        while start <= end:  #allow equals
            
            mid1 = start + (end - start) // 2
            if isEven:
                mid2 = (total - mid1 * 2) // 2
            else:
                mid2 = (total - mid1 * 2 - 1) // 2
            #print("mid1, mid2: ", mid1, mid2)
            
            maxLeft1  = nums1[mid1-1] if mid1 != 0 else -inf
            minRight1 = nums1[mid1] if mid1 != len(nums1) else inf
            maxLeft2  = nums2[mid2-1] if mid2 != 0 else -inf
            minRight2 = nums2[mid2] if mid2 != len(nums2) else inf
            #print("left1, right1, left2, right2: ", maxLeft1, minRight1, maxLeft2, minRight2)
            
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:    # done
                if total % 2 == 1:
                    return min(minRight1, minRight2)
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            elif maxLeft1 > minRight2:  #move mid1 to left
                #print("move <-")
                end = mid1 
            elif maxLeft2 > minRight1:  #move mid2 to right
                #print("move ->")
                start = mid1 + 1
                
        return None  #Exception 