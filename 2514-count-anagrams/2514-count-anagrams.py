class Solution:
    def countAnagrams(self, s: str) -> int:
        arr = s.split()
        ans = 1
        MOD = 10**9+7
        for word in arr:
            d = Counter(word)
            product = factorial(len(word))
            for v in d.values():
                product = product // factorial(v)
            ans = (ans * product) % MOD
        return ans