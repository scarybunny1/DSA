class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        n = len(words)
        for i in range(1, n):
            word = words[i]
            prev_word = words[i-1]
            
            if sorted(word) != sorted(prev_word):
                res.append(word)
            
        return res