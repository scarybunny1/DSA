class Solution:
    def lcs(self, i, j, s, t, memo):
        if i == len(s) or j == len(t):
            return 0
        
        if (i, j) in memo:
            return memo[(i, j)]
        same = not_same = 0
        if s[i] == t[j]:
            same = 1 + self.lcs(i+1, j+1, s, t, memo)
        else:
            not_same = self.lcs(i+1, j, s, t, memo)
        
        memo[(i, j)] = max(same, not_same)
        return memo[(i, j)]
        
    def appendCharacters(self, s: str, t: str) -> int:
        lcs = self.lcs(0, 0, s, t, {})
        return len(t) - lcs
    
    # c o a c h i n g
    #               i
    # c o d i n g
    #     j