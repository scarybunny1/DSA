class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boom = 0
        n = len(points)
        for i in range(n):
            dist = defaultdict(int)
            for j in range(n):
                d = math.pow(points[i][0] - points[j][0], 2) + math.pow(points[i][1] - points[j][1], 2)
                dist[d] += 1
            for v in dist.values():
                boom += v * (v-1)
        return boom