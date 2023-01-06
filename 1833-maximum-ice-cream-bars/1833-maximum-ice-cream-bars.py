class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        icecream = 0
        costs.sort()
        for cost in costs:
            if coins >= cost:
                icecream += 1
                coins -= cost
            else:
                break
        return icecream