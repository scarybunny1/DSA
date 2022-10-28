class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        curr = 0
        total = 0
        n = len(gas)
        start = 0
        for i in range(n):
            if curr < 0:
                start = i
                curr = 0
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            
        return -1 if total < 0 else start