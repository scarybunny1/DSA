class Solution:
    def getTripsInTime(self, time, bus_times):
        trips = 0
        for bus_time in bus_times:
            trips += time // bus_time
        return trips
    
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        mini = min(time)
        left, right = mini, mini*totalTrips
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            
            if self.getTripsInTime(mid, time) >= totalTrips:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans