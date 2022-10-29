class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * n
        
        p = 2
        
        while p * p < n:
            
            if primes[p]:
                
                for i in range(p*p, n, p):
                    primes[i] = False
            
            p += 1
            
        return sum(1 for i in range(2, n) if primes[i])