class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
#         p a r k e r
#         m o r r i s
        
#         d = {p:m, m:p, a:o, o:a, r:[r,k,s], k:[r,k,s], e:i, s:[r,k,s]}
        
#         p a r s e r
#         m a k k e k
        
        #Input:- two strings defining the equivalence rules, and a string baseStr
        #Output:- smalles string for baseStr using the equivalence relations
        
        #One strategy:- Disjoint Set with parent as the smallest character in the group
        root = [i for i in range(26)]
        for x, y in zip(s1, s2):
            self.union(ord(x)-ord('a'), ord(y)-ord('a'), root)
            
        ans = ""
        for ch in baseStr:
            smallest_eq = self.find(ord(ch)-ord('a'), root)
            ans += chr(smallest_eq + ord('a'))
        return ans
        
    
    def find(self, x, root):
        if root[x] == x:
            return x
        root[x] = self.find(root[x], root)
        return root[x]
    
    def union(self, x, y, root):
        rootX = self.find(x, root)
        rootY = self.find(y, root)
        if rootX != rootY:
            if rootX < rootY:
                root[rootY] = rootX
            else:
                root[rootX] = rootY