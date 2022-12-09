class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rev_s = s[::-1]
        new_s = s + "*" + rev_s
        
        lps = [0] * len(new_s)
        
        prevLPS, i = 0, 1
        
        while i < len(new_s):
            if new_s[i] == new_s[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]
                
        print(lps)
        return rev_s[:n-lps[-1]] + s
    
    
    # "a a c e c a a a * a a a c e c a a"
    #  0 1 0 0 0 1 2 2 0 1 2 2 3 4 5 6 7
    #                                    i
    #                p