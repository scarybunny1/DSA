class Solution:
    def gridPosFromNumPos(self, num, n):
        row = n - 1 - (num-1) // n
        col = num - (n-1-row) * n - 1
        
        if (n-1-row) % 2:
            col = n - 1 - col
        
        return row, col
        
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        q = collections.deque()
        n = len(board)
        
        q.append((1, 0))
        dist = [-1]*(n*n+1)
        
        while q:
            for _ in range(len(q)):
                pos, steps = q.popleft()
                for next_pos in range(pos+1, min(pos+6, n*n)+1):
                    row, col = self.gridPosFromNumPos(next_pos, n)
                    if board[row][col] != -1:
                        next_pos = board[row][col]
                        
                    if dist[next_pos] == -1:
                        dist[next_pos] = steps + 1
                        q.append((next_pos, dist[next_pos]))
        return dist[n*n]
    
# [[-1,-1,-1,46,47,-1,-1,-1]
# ,[51,-1,-1,63,-1,31,21,-1]
# ,[-1,-1,26,-1,-1,38,-1,-1]
# ,[-1,-1,11,-1,14,23,56,57]
# ,[11,-1,-1,-1,49,36,-1,48]
# ,[-1,-1,-1,33,56,-1,57,21]
# ,[-1,-1,-1,-1,-1,-1,2,-1]
# ,[ss,ss,ss,8,3,-1,6,56]]