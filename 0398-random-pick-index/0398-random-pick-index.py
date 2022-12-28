class Solution:

    def __init__(self, nums: List[int]):
        self.index = defaultdict(list)
        for i, num in enumerate(nums):
            self.index[num].append(i)

    def pick(self, target: int) -> int:
        index_list = self.index[target]
        
        return index_list[random.randint(0, len(index_list)-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)