class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # score.sort(reverse=True, key= lambda x: x[k])
        # return score
    
        arr = []
        for i, l in enumerate(score):
            arr.append([l[k], i])
        arr.sort(reverse=True)
        ans = []
        for _, i in arr:
            ans.append(score[i])
        return ans