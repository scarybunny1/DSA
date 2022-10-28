class Solution:
    def getAnagramWords(self, arr):
        d = defaultdict(list)
        
        for string in arr:
            sortedString = "".join(sorted(string))
            d[sortedString].append(string)
        
        return d
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = self.getAnagramWords(strs)
        
        return [l for l in d.values()]