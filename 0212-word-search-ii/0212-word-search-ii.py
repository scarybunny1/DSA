class Trie:
    def __init__(self):
        self.root = {}

class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(row, col, root):
            if (row < 0 or row >= n or
                col < 0 or col >= m or 
                board[row][col] not in root or 
                (row, col) in visited):
                return

            pre = root
            root = root[board[row][col]]
            if '#' in root:
                res.append(root['#'])
                del root['#']
                if not root.keys():
                    del pre[board[row][col]]
                    return

            visited.add((row, col))
            dfs(row+1, col, root)
            dfs(row-1, col, root)
            dfs(row, col+1, root)
            dfs(row, col-1, root)
            visited.remove((row, col))
        
        t = Trie()
        n, m = len(board), len(board[0])
        possible_word_length = n*m
        for word in words:
            if len(word) > possible_word_length:
                continue
            curr = t.root
            for char in word[::-1]:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['#'] = word
        
        res = []
        visited = set()
        for row in range(n):
            for col in range(m):
                if board[row][col] in t.root:
                    dfs(row, col, t.root)
        return res