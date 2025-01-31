class Solution:
    
    # DFS [O(10^turnedOn), 87%]
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn == 0:
            return ["0:00"]
        
        valToTime = [
            1,
            2,
            4,
            8,
            16,
            32,
            60,
            120,
            240,
            480
        ]

        results = []
        self.dfs(valToTime, turnedOn, 0, [], results)
        return sorted(results)
        
    def dfs(self, valToTime, turnedOn, idx, cur, results):
        if len(cur) == turnedOn:
            convertedTime = self.convertTime(cur)
            if convertedTime:
                results.append(convertedTime)
            return
        
        for i in range(idx, len(valToTime)):
            self.dfs(valToTime, turnedOn, i + 1, cur + [valToTime[i]], results)
    
    def convertTime(self, timeList):
        timeVal = 0
        
        # Min part can't carry over
        minPart = 0
        for time in timeList:
            if time < 60: 
                minPart += time
        if minPart >= 60:
            return None 
        
        # Convert the time from minutes to time value (e.g. 123 -> 2:03)
        for time in timeList:
            timeVal += time
        hour = timeVal // 60
        minute = timeVal % 60 
        
        # Remove the values over the boundaries
        if hour >= 12 or minute >= 60:
            return None
        
        # Process the output string
        hourStr = str(hour)
        minuteStr = str(minute)
        # if len(hourStr) == 1:
        #     hourStr = "0" + hourStr
        if len(minuteStr) == 1:
            minuteStr = "0" + minuteStr  
        timeStr = hourStr + ":" + minuteStr
        
        return timeStr