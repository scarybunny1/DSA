def sumK(sum, i, arr):
    if i == n:
        if sum == k:
            res.append(arr)
            return True
        return False
    sum += nums[i]
    arr.append(nums[i])
    if sumK(sum, i + 1, arr):
        return True
    sum -= nums[i]
    arr.pop()

    if sumK(sum, i + 1, arr):
        return True
    
    return False

nums = [1,2,1]
k = 2
res = []
n = len(nums)
sumK(0, 0, [])
print(res)