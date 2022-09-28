def sumN(i, n):
    if i == n:
        return n
    return i + sumN(i+1, n)

def sumNto0(n):
    if n == 0:
        return 0
    return n + sumNto0(n-1)

def sumNwithSum(sum, n):
    if n == 0:
        return sum
    return sumNwithSum(sum+n, n-1)

print(sumN(0, 5))
print(sumNto0(5))
print(sumNwithSum(0, 5))