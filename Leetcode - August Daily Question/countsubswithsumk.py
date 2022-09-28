def countSumK(sum, i):
    if i == n:
        if sum == k:
            return 1
        return 0
    
    l = countSumK(sum + nums[i], i + 1)
    r = countSumK(sum, i + 1)
    return l + r

nums = [1,2,1]
n = len(nums)
k = 2
print(countSumK(0, 0))