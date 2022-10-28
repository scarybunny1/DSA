class Solution:
    def getZeros(self, n, two, five, ten):
        while n % 10 == 0:
            ten += 1
            n = n // 10
        
        while n % 5 == 0:
            five += 1
            n = n // 5
        
        while n % 2 == 0:
            two += 1
            n = n // 2
        
        return (two, five, ten)
    
    def trailingZeroes(self, n: int) -> int:
        # two = five = ten = 0
        # for num in range(2, n+1):
        #     two, five, ten = self.getZeros(num, two, five, ten)
        # return ten + min(two, five)
        
        result = 0
        
        while n:
            n  = n // 5
            result += n
        
        return result