def subs(arr, i):
    if i == n:
        res.append(list(arr))
        return
    arr.append(nums[i])
    subs(arr, i+1)
    arr.pop()
    subs(arr, i+1)

res = []
nums = [3,1,2]
n = len(nums)
subs([], 0)
print(res)