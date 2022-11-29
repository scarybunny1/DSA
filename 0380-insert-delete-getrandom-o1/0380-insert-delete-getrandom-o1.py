class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        
        index_to_remove, last_element = self.pos[val], self.nums[-1]
        self.pos[last_element] = index_to_remove
        self.nums[index_to_remove] = last_element
        
        
        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.nums)-1)
        return self.nums[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()