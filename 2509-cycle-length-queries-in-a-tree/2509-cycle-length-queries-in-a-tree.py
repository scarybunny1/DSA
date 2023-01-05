class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        for x, y in queries:
            path = 0
            while x != y:
                if x > y:
                    x //= 2
                    path += 1
                else:
                    y //= 2
                    path += 1
            ans.append(path+1)
        return ans