class Allocator:

    def __init__(self, n: int):
        self.arr = [-1] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        free = 0
        for i in range(self.n):
            if self.arr[i] == -1:
                free += 1
            else:
                free = 0
            if free == size:
                for j in range(i, i-size, -1):
                    self.arr[j] = mID
                break
        if free < size:
            return -1
        return i-size+1

    def free(self, mID: int) -> int:
        count = 0
        for i in range(self.n):
            if self.arr[i] == mID:
                self.arr[i] = -1
                count += 1
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)