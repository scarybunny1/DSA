class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_l = s.split()
        if len(s_l) != len(pattern):
            return False
        d = {}
        t = {}
        
        for i, word in enumerate(s_l):
            if pattern[i] in d:
                if d[pattern[i]] != word:
                    return False
            d[pattern[i]] = word
            
            if word in t:
                if t[word] != pattern[i]:
                    return False
            t[word] = pattern[i]
        return True