class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        maxi = 0
        first = 0
        for i in range(n):
            maxi = max(maxi, first + values[i] - i)
            
            first = max(first, values[i] + i)
        return maxi