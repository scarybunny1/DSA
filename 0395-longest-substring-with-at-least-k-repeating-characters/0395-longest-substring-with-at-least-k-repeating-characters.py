class Solution:
    def kRepeating(self, count, k):
        return all(c >= k for c in count.values())
    
    def calculateMaxLength(self, uniqueChar, s, k):
        d = {}
        
        left = 0
        length = 0
        n = len(s)
        
        for right, char in enumerate(s):
            d[char] = d.get(char, 0) + 1
            
            while len(d) > uniqueChar:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left += 1
                
            if len(d) == uniqueChar and self.kRepeating(d, k):
                length = max(length, right - left + 1)
        
        return length
            
    
    def longestSubstring(self, s: str, k: int) -> int:
        totalUniqueChar = len(list(Counter(s).keys()))
        max_len = 0
        
        for uniqueChar in range(1, totalUniqueChar + 1):
            max_len = max(max_len, self.calculateMaxLength(uniqueChar, s, k))
            
        return max_len