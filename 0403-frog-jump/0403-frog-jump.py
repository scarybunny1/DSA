class Solution:
    def dfs(self, stone, step, stones, available_units, visited, memo):
        n = len(stones)
        if stone == stones[n-1]:
            return True
        if (stone, step) in memo:
            return memo[(stone, step)]
        for next_step in [step+1, step, step-1]:
            next_stone = stone + next_step
            if next_stone in available_units and next_stone not in visited:
                visited.add(next_stone)
                memo[(next_stone, next_step)] = self.dfs(next_stone, next_step, stones, available_units, visited, memo)
                if memo[(next_stone, next_step)]:
                    return True
                    
                visited.remove(next_stone)
                
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        return self.dfs(1, 1, stones, set(stones), set(), {})