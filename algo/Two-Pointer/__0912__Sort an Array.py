class Solution:
    
    # ================================================
    # Merge Sort (Java style) [Time: O(nlogn), 11% / Space: O(n), 47%]
    def sortArray(self, nums: List[int]) -> List[int]:
        print("MergeSort (Java Style)")
        def mergeSort(nums, start, end, temp):
            #print("mergeSort(", start, ",", end, ")")
            if start >= end:
                return 
            mid = start + (end - start) // 2
            
            mergeSort(nums, start, mid, temp)
            mergeSort(nums, mid + 1, end, temp)
            
            merge(nums, start, end, temp) 
            return 
        
        # Merge 2 list starting from "start" and "mid + 1"
        def merge(nums, start, end, temp):
            #print(">> merge(", start, ",", end, ")", nums)
            mid = start + (end - start) // 2
            left = start
            right = mid + 1 
            idx = start
            
            while left <= mid and right <= end:
                if nums[left] <= nums[right]:
                    temp[idx] = nums[left]
                    left += 1
                    idx += 1
                else:
                    temp[idx] = nums[right]
                    right += 1
                    idx += 1  
                    
            # If there is leftover in left
            while left <= mid:
                temp[idx] = nums[left] 
                left += 1
                idx += 1
            # If there is leftover in right
            while right <= end:
                temp[idx] = nums[right] 
                right += 1
                idx += 1
            
            # Pass the element back to nums 
            for i in range(start, end + 1):  # only this interval, not whole nums
                nums[i] = temp[i]

                
        temp = [0] * len(nums)
        mergeSort(nums, 0, len(nums) - 1, temp)
        
        return nums
        
    # ================================================
    # Quick Sort [Time: O(nlogn), 43% / Space: O(1), 47%]
    def sortArray2(self, nums: List[int]) -> List[int]:
        print("QuickSort")
        def partition(nums, start, end):
            #print("start:", start, " end:", end)
            if start >= end:
                return 
            left, right = start, end
            mid = left + (right - left) // 2
            #mid = left  #TLE
            pivot = nums[mid]
            
            while left <= right:
                while left <= right and nums[left] < pivot:
                    left += 1
                while left <= right and nums[right] > pivot:
                    right -= 1
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1 
                    right -= 1
            partition(nums, start, right)
            partition(nums, left, end)
            
        partition(nums, 0, len(nums) - 1)
        return nums
            
    # ================================================
    
    # Built-in Sort [O(nlogn), 75%]
    def sortArray1(self, nums: List[int]) -> List[int]:
        return sorted(nums)