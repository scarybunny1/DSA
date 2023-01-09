class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # 1 2 3 3 4 5
        # l
        #           r
        skill.sort()
        n = len(skill)
        ans = 0
        s = set()
        for i in range(n//2):
            chemistry = skill[i]+skill[n-i-1]
            s.add(chemistry)
            if len(s) > 1:
                return -1
            ans += skill[i]*skill[n-i-1]
        return ans