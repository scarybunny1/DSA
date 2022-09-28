def path(i, j):
    if (i, j) == (0, 0):
        return 1
    result = 0
    if j - 1 >= 0:
        result += path(i, j-1)
    if i - 1 >= 0:
        result += path(max(i-1, 0), j)
    return result

print(path(5,5))

def pathmemo(i, j):
    if (i, j) == (0, 0):
        return 1
    if (i, j) in memo:
        return memo[(i, j)]
    result = 0
    if j - 1 >= 0:
        result += path(i, j-1)
    if i - 1 >= 0:
        result += path(max(i-1, 0), j)
    memo[(i, j)] = result
    return result

memo = {}
print(pathmemo(5,5))

m, n = 6,6
dp = [[0] * n for _ in range(m)]
dp[0][0] = 1
for i in range(m):
    for j in range(n):
        if i-1 >= 0:
            dp[i][j] += dp[i-1][j]
        if j-1 >= 0:
            dp[i][j] += dp[i][j-1]
print(dp[m-1][n-1])

m, n = 6, 6
prev = [0] * n
for i in range(m):
    curr = [0] * n
    for j in range(n):
        if i == 0 and j == 0:
            curr[j] = 1
        else:
            curr[j] += curr[j-1] if j > 0 else 0
            curr[j] += prev[j] if i > 0 else 0
    prev = list(curr)

print(prev[n-1])