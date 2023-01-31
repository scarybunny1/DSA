class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ageScore = sorted(zip(ages, scores))
        n = len(ages)
        # memo = {}
        # return self.bestTeam(0, -1, ageScore, memo)
    
        dp = [ageScore[i][1] for i in range(n)]
        
        for i in range(1, n):
            for j in range(i):
                if ageScore[i][1] >= ageScore[j][1]:
                    dp[i] = max(dp[i], ageScore[i][1] + dp[j])
        return max(dp)
        
    def bestTeam(self, i, lastIndex, ageScore, memo):
        if i == len(ageScore):
            return 0
        
        if (i, lastIndex) in memo:
            return memo[(i, lastIndex)]
        
        if lastIndex == -1 or ageScore[i][1] >= ageScore[lastIndex][1]:
            memo[(i, lastIndex)] = max(ageScore[i][1] + self.bestTeam(i+1, i, ageScore, memo), self.bestTeam(i+1, lastIndex, ageScore, memo))
        else:
            memo[(i, lastIndex)] = self.bestTeam(i+1, lastIndex, ageScore, memo)
        return memo[(i, lastIndex)]
    
    