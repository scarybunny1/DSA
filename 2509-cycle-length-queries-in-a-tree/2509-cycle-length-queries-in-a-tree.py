class Solution:
    def getDist(self, x, y):
        if x == y:
            return 0
        elif x > y:
            return 1 + self.getDist(x//2, y)
        else:
            return 1 + self.getDist(x, y//2)
        
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        for x, y in queries:
            ans.append(1 + self.getDist(x, y))
        return ans