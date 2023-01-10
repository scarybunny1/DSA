class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_len = 0
        for i in range(len(strs)):
            string = strs[i]
            if string.isnumeric():
                max_len = max(max_len, int(string))
            else:
                max_len = max(max_len, len(string))
        return max_len