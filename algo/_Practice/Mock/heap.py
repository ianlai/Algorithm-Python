import heapq
def findMedian(arr):
    if len(arr) == 0:
        return -1 
    n = len(arr)  #n=5
    half = n // 2	
    heap = arr[:half]  #0, 1
    heapq.heapify(heap) 
    for v in arr[half:]:  #2,3,4
        if v > heap[0]:  #min 
            heapq.heappop(heap)
            heapq.heappush(heap, v)
    return heap[0]

print(findMedian([5,6,3,1,7]))