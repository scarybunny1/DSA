def nextGreater(nums, n):
    stack = []
    result = [-1] * n
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)
    return result



if __name__ == "__main__":
    nums = [2,7,3,5,4,6,8]
    result = nextGreater(nums, len(nums))
    print(result)