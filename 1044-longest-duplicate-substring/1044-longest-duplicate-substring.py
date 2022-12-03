class Solution:
    def checkDuplications(self, s, length):
        d = defaultdict(int)
        
        for i in range(len(s) - length + 1):
            d[s[i:i+length]] += 1
            
        maxi = 0
        ans = ""
        for key, value in d.items():
            if value > maxi:
                ans = key
                maxi = value
        return ans, maxi
    
    def longestDupSubstring(self, s: str) -> str:
        max_length = 0
        low, high = 0, len(s)
        ans = ""
        while low <= high:
            l = (low + high) // 2
            
            string, repetition = self.checkDuplications(s, l)
            if repetition >= 2 and l > max_length:
                ans = string
                max_length = l
                low = l + 1
            else:
                high = l - 1
                
        return ans
    
#     b a n a n a
#     0 1 2 3 4 5
#     l
#               h
#         m
    
#     i = 0, 1, 2, 3, 4
#     d = {"ba":1, "an":2, "na":2}
        