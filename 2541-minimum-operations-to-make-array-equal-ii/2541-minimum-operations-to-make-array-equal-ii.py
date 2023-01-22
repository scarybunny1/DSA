class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        inc = dec = 0
        for i in range(len(nums1)):
            if nums1[i] > nums2[i]:
                if (nums1[i]-nums2[i]) % k:
                    return -1
                dec += (nums1[i]-nums2[i]) // k
            elif nums1[i] < nums2[i]:
                if (nums2[i]-nums1[i]) % k:
                    return -1
                inc += (nums2[i]-nums1[i]) // k
                
        return -1 if inc != dec else inc