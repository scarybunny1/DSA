class Solution:
    def traverse(self, node, parent, count, tree, label, ans):
        curr_label_index = ord(label[node]) - ord('a')
        prev = count[curr_label_index]
        count[curr_label_index] += 1
        for nei in tree[node]:
            if nei == parent:
                continue
            self.traverse(nei, node, count, tree, label, ans)
            
        ans[node] = count[curr_label_index] - prev
        
        
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(list)
        for x, y in edges:
            tree[x].append(y)
            tree[y].append(x)
        ans = [0] * n
        count = [0] * 26
        self.traverse(0, -1, count, tree, labels, ans)
        return ans