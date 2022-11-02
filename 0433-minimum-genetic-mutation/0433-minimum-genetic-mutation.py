class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        bank = set(bank)
        q = collections.deque([start])
        mutations = 0
        visited = set([start])
        while q:
            for _ in range(len(q)):
                gene = q.popleft()
                if gene == end:
                    return mutations
                for i in range(8):
                    for m in ['A', 'C', 'G', 'T']:
                        new_gene = gene[:i] + m + gene[i+1:]
                        if new_gene in bank and new_gene not in visited:
                            q.append(new_gene)
                            visited.add(new_gene)
            mutations += 1
        
        return -1