
def convertIntoMonotonicStack(nums):
    stack = []
    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    return stack


if __name__ == "__main__":
    nums = [2,3,7,11,5,17,19]
    result = convertIntoMonotonicStack(nums)
    print(result)