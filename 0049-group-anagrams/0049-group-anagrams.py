class Solution:
    def getAnagramWordDictionary(self, arr):
        d = defaultdict(list)
        
        for string in arr:
            sortedString = "".join(sorted(string))
            d[sortedString].append(string)
        
        return d
    
    def getAnagramWordDictionary2(self, arr):
        d = defaultdict(list)
        
        for string in arr:
            s = [0]*26
            for char in string:
                index = ord(char) - ord('a')
                s[index] += 1
            hashable_key = "#".join(map(str, s))
            d[hashable_key].append(string)
            
        return d
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = self.getAnagramWordDictionary2(strs)
        
        return d.values()