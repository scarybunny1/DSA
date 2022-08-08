# 8th August, 2022
# Ayush S Bhatt

# Leetcode 300. Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or 
# no elements without changing the order of the remaining elements. 
# For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

#Approach DP: We calculate the LIS upto an index and find out if 
def lengthOFLIS(nums):
    n = len(nums)
    dp = [1] * n #1, since every number in itself is an increasing subsequence
    longest = 1 #To keep track of the current LIS
    for i in range(n):
        for j in range(i):
            #Check if it can be included in an increasing subsequence
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        #Update longest upto current index
        longest = max(longest, dp[i])
    return longest

print(lengthOFLIS([0,3,1,6,2,2,7])) #Will print 4 as LIS is [3,6,2,7]