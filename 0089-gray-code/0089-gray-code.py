class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        visited = set([0])
        self.dfs(0, visited, res, n)
        return res
    
    def dfs(self, num, visited, res, n):
        if len(res) == (1 << n):
            return True
        
        for i in range(n):
            next_num = num ^ (1 << i)
            if next_num not in visited:
                visited.add(next_num)
                res.append(next_num)
                if self.dfs(next_num, visited, res, n):
                    return True
                res.pop()
                visited.remove(next_num)
                