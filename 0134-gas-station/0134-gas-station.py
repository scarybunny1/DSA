class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        curr = 0
        start = 0
        n = len(gas)
        
        for i in range(n):
            if curr < 0:
                start = i
                curr = 0
            curr += gas[i] - cost[i]
        return start