class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive = set(positive_feedback)
        negative = set(negative_feedback)
        n = len(student_id)
        pq = []
        for i in range(n):
            score = 0
            for word in report[i].split():
                if word in positive:
                    score += 3
                if word in negative:
                    score -= 1
            heapq.heappush(pq, (score, -student_id[i]))
            
            if len(pq) > k:
                heapq.heappop(pq)
        return [-id for _, id in sorted(pq, key = lambda x: (-x[0], -x[1]))]