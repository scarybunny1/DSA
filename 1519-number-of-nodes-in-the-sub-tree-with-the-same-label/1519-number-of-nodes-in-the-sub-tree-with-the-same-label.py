class Solution:
    def traverse(self, node, parent, tree, label, ans):
        
        d = defaultdict(int)
        d[label[node]] += 1
        child_d = defaultdict(int)
        for nei in tree[node]:
            if nei == parent:
                continue
            child_d = self.traverse(nei, node, tree, label, ans)
            
            for k, v in child_d.items():
                d[k] += v
        
        ans[node] = d[label[node]]
        
        return d
        
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(list)
        for x, y in edges:
            tree[x].append(y)
            tree[y].append(x)
        ans = [0] * n
        self.traverse(0, -1, tree, labels, ans)
        return ans