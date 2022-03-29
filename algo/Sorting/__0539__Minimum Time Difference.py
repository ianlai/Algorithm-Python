class Solution:
    
    # Sorting + Concatenate 2 array to avoid cycled distance [O(nlogn): 83%]
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for timeString in timePoints:
            time = timeString.split(":")
            times.append(int(time[0]) * 60 + int(time[1]))
        times.sort()
        times += [t + 24 * 60 for t in times]
        minDiff = inf
        for i, t in enumerate(times):
            if i == 0:
                continue
            minDiff = min(minDiff, times[i] - times[i-1])
        return minDiff