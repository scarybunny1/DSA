class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            count = defaultdict(int)
            for j in range(n):
                if i == j:
                    continue
                den = (points[j][0] - points[i][0])
                if den == 0:
                    angle = inf
                else:
                    angle = (points[j][1] - points[i][1]) / den
                count[angle] += 1
                result = max(result, max(count.values())+1)
        return result