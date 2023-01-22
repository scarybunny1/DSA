class Solution:
    def isPalindrome(self, string):
        return string == string[::-1]
    
    def part(self, i, s, arr, res):
        n = len(s)
        if i == n:
            res.append(list(arr))
            return
        string = ""
        for j in range(i, n):
            string += s[j]
            if self.isPalindrome(string):
                arr.append(string)
                self.part(j+1, s, arr, res)
                arr.pop()
            
        
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.part(0, s, [], res)
        return res