from sortedcontainers import SortedDict
class Solution:
    def getFlowerCount(self, pos, nums):
        left, right = 0, len(nums)-1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid][0] <= pos:
                ans = nums[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return ans
    
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        positions = SortedDict()
        
        for start, end in flowers:
            positions[start] = positions.get(start, 0) + 1
            positions[end+1] = positions.get(end+1, 0) - 1
        
        flower_pos_cnt = []
        curr_sum = 0
        for pos, count in positions.items():
            curr_sum += count
            flower_pos_cnt.append((pos, curr_sum))
            
        ans = []
        for person in persons:
            ans.append(self.getFlowerCount(person, flower_pos_cnt))
        return ans