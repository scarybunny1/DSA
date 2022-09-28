def reverse(arr, left, right):
    if left < right:
        arr[left], arr[right] = arr[right], arr[left]
        reverse(arr, left+1, right-1)

def reverseSingle(arr, i):
    if i < len(arr) - i - 1:
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
        reverseSingle(arr, i+1)

arr = [1,2,3,4,5]
reverse(arr, 0, len(arr) - 1)
print(arr)
reverseSingle(arr, 0)
print(arr)