class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = []
        n = len(timePoints)
        for t in timePoints:
            hours, minutes = map(int, t.split(":"))
            timestamp = hours*60+minutes
            time.append(timestamp)
        
        time.sort()
        mini = 1440
        
        for i in range(1, n):
            if time[i] - time[i-1] < mini:
                mini = time[i] - time[i-1]
        mini = min(mini, 1440-time[n-1]+time[0])
        return mini