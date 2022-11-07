class Solution:
    def maximum69Number (self, num: int) -> int:
        arr = []
        temp = num
        while temp:
            arr.append(temp%10)
            temp //= 10
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 6:
                arr[i] = 9
                break
        new_num = 0
        for i in range(len(arr)-1, -1, -1):
            new_num = new_num * 10 + arr[i]
        return new_num