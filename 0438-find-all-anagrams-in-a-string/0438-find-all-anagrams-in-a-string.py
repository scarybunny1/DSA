class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
#         c b a e b a b a c d
#         0 1 2 3 4 5 6 7 8 9
        
#         l
#             r
        # count_s = {c:1, b:1, a:1}
            
        n_s, n_p = len(s), len(p)
        count_s = {}
        count_p = Counter(p)
        
        left = 0
        indexes = []
        for right in range(n_s):
            count_s[s[right]] = count_s.get(s[right], 0) + 1
            
            if count_s == count_p:
                indexes.append(left)
            
            if right - left + 1 == n_p:
                count_s[s[left]] -= 1
                if count_s[s[left]] == 0:
                    del count_s[s[left]]
                left += 1
                
        return indexes