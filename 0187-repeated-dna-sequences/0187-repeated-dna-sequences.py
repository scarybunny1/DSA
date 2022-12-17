class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        
        left = 0
        right = 10
        d = defaultdict(int)
        
        for i in range(len(s)-10+1):
            d[s[left+i:right+i]] += 1
        
        return [string for string, count in d.items() if count > 1]