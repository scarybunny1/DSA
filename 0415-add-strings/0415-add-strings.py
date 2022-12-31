class Solution:
    def convertToInt(self, num):
        ans = 0
        power = 10
        for d in num:
            digit = int(d)
            ans = ans * power + digit
        return ans
        
    def addStrings(self, num1: str, num2: str) -> str:
        num_1 = self.convertToInt(num1)
        num_2 = self.convertToInt(num2)
        return str(num_1+num_2)