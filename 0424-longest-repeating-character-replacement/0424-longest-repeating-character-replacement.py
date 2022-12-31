class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        d = {}
        n = len(s)
        max_len = 0
        for right in range(n):
            d[s[right]] = d.get(s[right], 0) + 1
            
            while (right - left + 1) - max(d.values()) > k:
                d[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
        
        return max_len