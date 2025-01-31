class UndergroundSystem:

    # 2022/04/25 
    # Use map, save a jouney when a in/out pair is completed 
    # [TC: O(1): 54% / SC: O(P+S^2): 31%]
    def __init__(self):
        
        self.checkInTime = {}
        self.journey = collections.defaultdict(lambda: [0] * 2)
    
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInTime[id] = (stationName, t) 

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, checkTime = self.checkInTime[id]
        self.journey[(startStation, stationName)][0] += t - checkTime
        self.journey[(startStation, stationName)][1] += 1 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, totalCount = self.journey[(startStation, endStation)]
        return totalTime / totalCount
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)