class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        n = len(s)
        order = [[] for _ in range(n+1)]
        for char, count in freq.items():
            order[count].append(char)
        
        res = ""
        for l in range(n, -1, -1):
            if order[l] != []:
                res += "".join([order[l][i] * l for i in range(len(order[l]))])
        return res