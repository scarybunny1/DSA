class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        # 3 3 2 1 4 8 2 1
        # 0 1 2 3 4 5 6 7
        
        n = len(ratings)
        left, right = [1] * n, [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
                
        return sum(max(left[i], right[i]) for i in range(n))