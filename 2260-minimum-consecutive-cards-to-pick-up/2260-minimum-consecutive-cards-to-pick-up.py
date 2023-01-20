class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = defaultdict(list)
        for i, card in enumerate(cards):
            d[card].append(i)
        
        ans = inf
        for indexes in d.values():
            for i in range(1, len(indexes)):
                ans = min(ans, indexes[i]-indexes[i-1]+1)
        return -1 if ans == inf else ans