class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        words_d = defaultdict(list)
        
        for word in words:
            words_d[word[0]].append(word)
        
        count = 0
        for ch in s:
            words_starting_with_ch = words_d[ch]
            words_d[ch] = []
            
            for word in words_starting_with_ch:
                if len(word) == 1:
                    count += 1
                else:
                    words_d[word[1]].append(word[1:])
    
        return count