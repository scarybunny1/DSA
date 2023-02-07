class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 1 2 3 2 2
        # 0 1 2 3 4
        #   l
        #         r
        # ftype = {2:3, 3:1}
        # max_fruits = 4
        
        ftype = {}
        max_fruits = 0
        left = 0
        for right, fruit in enumerate(fruits):
            ftype[fruit] = ftype.get(fruit, 0) + 1
            
            while len(ftype.keys()) > 2:
                ftype[fruits[left]] -= 1
                if ftype[fruits[left]] == 0:
                    del ftype[fruits[left]]
                left += 1
            
            max_fruits = max(max_fruits, sum(v for v in ftype.values()))
        return max_fruits