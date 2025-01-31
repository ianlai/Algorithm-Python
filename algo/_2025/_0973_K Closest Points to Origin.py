class Solution:
    # Time: klog(n) / Space: n
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distancePoints = [(p[0]**2 + p[1]**2, p) for p in points]
        heapq.heapify(distancePoints)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(distancePoints)[1])
        return res
