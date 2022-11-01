class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        # ratings -     3 3 2 1 4 8 2 1
        # index -       0 1 2 3 4 5 6 7
        # left -        1 1 1 1 2 3 1 1
        # right -       1 3 2 1 1 3 2 1
        # ans -         1 3 2 1 2 3 2 1
        # sum - 1+3+2+1+2+3+2+1 = 15
        
        # 0 -> n-1 - 0
        # 1 -> n-1 - 1
        # 2 -> n-1 - 2
        
        n = len(ratings)
        left, right = [1] * n, [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
            
            j = n - 1 - i
            if ratings[j] > ratings[j+1]:
                right[j] = right[j+1] + 1
                
        return sum(max(left[i], right[i]) for i in range(n))