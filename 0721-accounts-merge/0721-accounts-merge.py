class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0] * n
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DisjointSet(n)
        emails = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in emails:
                    emails[email] = i
                else:
                    parent = emails[email]
                    ds.union(parent, i)
                
        aux = [[] for _ in range(n)]
        
        for email, index in emails.items():
            new_index = ds.find(index)
            aux[new_index].append(email)
            
        ans = []
        for i, l in enumerate(aux):
            if not l:
                continue
            new_l = [accounts[i][0]]
            new_l += sorted(l)
            ans.append(new_l)
        return ans
        
        
        