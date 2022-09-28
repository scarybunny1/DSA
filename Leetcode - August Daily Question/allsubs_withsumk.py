def subssumK(sum, i, arr):
    if i == n:
        if sum == k:
            res.append(arr)
        return
    subssumK(sum+nums[i], i + 1, arr+[nums[i]])

    subssumK(sum, i + 1, arr)

nums = [1, 2, 1]
k = 2
n = len(nums)
res = []
subssumK(0, 0, [])
print(res)