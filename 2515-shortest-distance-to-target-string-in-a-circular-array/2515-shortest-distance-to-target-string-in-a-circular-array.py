class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        n = len(words)
        min_steps = inf
        for i in range(startIndex, n+startIndex):
            if words[i%n] == target:
                min_steps = min(min_steps, i - startIndex, n - i + startIndex)
        return min_steps