class Solution:
    def isSafe(self, row, col, n, m):
        return (0 <= row < n and 0 <= col < m)
    
    def foundWord(self, i, row, col, word, board, visited):
        n, m = len(board), len(board[0])
        
        if i == -1:
            return True
        
        if not self.isSafe(row, col, n, m):
            return False
        
        if (row, col) in visited:
            return False
        
        if board[row][col] != word[i]:
            return False
        
        visited.add((row, col))
        
        for dr, dc in [[0,1], [1,0], [-1,0], [0,-1]]:
            if self.foundWord(i-1, row+dr, col+dc, word, board, visited):
                return True
            
        visited.remove((row, col))
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = set()
        for row in range(n):
            for col in range(m):
                if self.foundWord(len(word)-1, row, col, word, board, visited):
                    return True
        return False