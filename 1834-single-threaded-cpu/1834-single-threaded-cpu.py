class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #1:06:10
        order = []
        sortedTasks = [[enq, pro, i] for i, (enq, pro) in enumerate(tasks)]
        sortedTasks.sort()
        pq = []
        curr_time = 0
        i = 0
        n = len(tasks)
        while i < n or pq:
            if not pq and curr_time < sortedTasks[i][0]:
                curr_time = sortedTasks[i][0]
            
            while i < n and sortedTasks[i][0] <= curr_time:
                heapq.heappush(pq, (sortedTasks[i][1], sortedTasks[i][2]))
                i += 1
            
            pro_time, taskNumber = heapq.heappop(pq)
            order.append(taskNumber)
            curr_time += pro_time
        
        return order