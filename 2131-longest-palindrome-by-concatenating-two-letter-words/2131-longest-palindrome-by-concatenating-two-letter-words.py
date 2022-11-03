class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = {}
        result = 0
        unpaired = 0
        for word in words:
            if word[0] == word[1]:
                if d.get(word, 0) == 0:
                    unpaired += 1
                    d[word[::-1]] = d.get(word[::-1], 0) + 1
                else:
                    result += 4
                    unpaired -= 1
                    d[word[::-1]] -= 1
            elif d.get(word, 0) == 0:
                d[word[::-1]] = d.get(word[::-1], 0) + 1
            else:
                result += 4
                d[word] -= 1
        
        return result if unpaired == 0 else result + 2
    
    
#         d = {oq:1, of:2, qf:0, }
#         word=fo
#         result=4+
        
#         d = {oq,of:0,qf:0,ff,qq,fq:1,fo:3,oo,}
#         result=4+4+4+4
#         unpaired=3
#         d = {oq,of:1,qf:0,fq:3,fo:2,}
#         ff,qq,oo
        
#         fq fo fo                           of of qf
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        