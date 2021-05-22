class Solution:
    
    # Find the max, flip to the first, then flip it to last [O(n2), 5%]
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        
        ans = []
        for i in range(len(arr) - 1, 0, -1):
            maxVal = max(arr[:i+1])
            k = arr.index(maxVal)
            #print(i, ":", arr, maxVal, k)
            arr = arr[:k+1][::-1] + arr[k+1:] #Flip-1 (flip max to first)
            #print(i, ":", arr, maxVal, k)
            arr = arr[:i+1][::-1]             #Flip-2 (flip first to last which not sorted)
            #print(i, ":", arr, maxVal, k)
            #print("------------")
            ans.append(k + 1)
            ans.append(i + 1)
        return ans