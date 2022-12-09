class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k = k % total
        
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            
            k -= chalk[i]
        