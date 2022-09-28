def perm(arr, i):
    if i == n:
        res.append(arr)
        return
    
    for num in nums:
        if num not in visited:
            visited.add(num)
            perm(arr+[num], i+1)
            visited.remove(num)

visited = set()
nums = [1,2,3]
n = len(nums)
res = []
perm([], 0)
print(res)
