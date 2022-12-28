class Solution:
    def goToOne(self, num):
        if num == 1:
            return 0
        if num % 2 == 0:
            return 1 + self.goToOne(num // 2)
        return 1 + min(self.goToOne(num+1), self.goToOne(num-1))
    
    def integerReplacement(self, n: int) -> int:
        return self.goToOne(n)