# 9th August, 2022
# Ayush S Bhatt

# 823. Binary Trees With Factors
# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

# We make a binary tree using these integers, and each number may be used for any number of times. 
# Each non-leaf node's value should be equal to the product of the values of its children.

# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

class Solution:
    def numFactoredBinaryTrees(self, arr) -> int:
        MOD = 10**9+7
        n = len(arr)
        arr.sort()
        dp = [1] * n
        index = {x:i for i, x in enumerate(arr)}

        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0: #Check if arr[j] is a factor of arr[i] i.e. one of the children
                    second = arr[i] // arr[j] #Find the other child
                    if second in index:
                        dp[i] += dp[j] * dp[index[second]]
                        dp[i] %= MOD
        return sum(dp) % MOD

if __name__ == "__main__":
    arr = [4, 2, 5, 10]
    print(Solution().numFactoredBinaryTrees(arr))
