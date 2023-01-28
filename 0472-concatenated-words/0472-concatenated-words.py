class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        ans = []
        
        for word in words:
            word_set.remove(word)
            if self.checkConcatenated(0, word, word_set):
                ans.append(word)
            word_set.add(word)
            
        return ans
    
    def checkConcatenated(self, i, word, word_set):
        if i == len(word):
            return True
        
        string = ""
        for j in range(i, len(word)):
            string += word[j]
            
            if string in word_set:
                if self.checkConcatenated(j+1, word, word_set):
                    return True
                
        return False
    