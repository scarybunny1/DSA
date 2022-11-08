class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_factor = [0]*(n+1)
        trusting_others = [0]*(n+1)
        for person1, person2 in trust:
            trust_factor[person2] += 1
            trusting_others[person1] += 1
        
        for i in range(1, n+1):
            if trust_factor[i] == n-1 and trusting_others[i] == 0:
                return i
        return -1