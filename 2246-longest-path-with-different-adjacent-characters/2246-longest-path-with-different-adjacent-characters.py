class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        #01:48:00
        #Input: Tree, Root - 0, Nodes - n, Array parent - parent[i] is parent of node i, String s - s[i] is character assigned to i
        
        #Output: length of longest path, Condition - adjacent nodes on same path do not have same character
        n = len(parent)
        children = defaultdict(list)
        for i in range(1, n):
            children[parent[i]].append(i)
        
        return max(self.getLongestChain(0, s, children))
        
    def getLongestChain(self, node, s, children):
        longest_chain = 1    #Single Node
        longest_path = 1
        pq = []
        for child in children[node]:
            child_chain, child_path = self.getLongestChain(child, s, children)
            longest_path = max(longest_path, child_path)
            if s[child] != s[node]:
                heapq.heappush(pq, child_chain)
                if len(pq) > 2:
                    heapq.heappop(pq)
        
        if len(pq) == 2:
            longest_chain = max(pq[0], pq[1]) + 1
            longest_path = max(longest_path, pq[0] + pq[1] + 1)
        elif len(pq) == 1:
            longest_chain = pq[0] + 1
            longest_path = max(longest_path, pq[0] + 1)
        return longest_chain, longest_path